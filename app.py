from gevent import monkey
monkey.patch_all()

from gevent.pool import Pool

import json
import logging
import os
import uuid

import flask
import pymongo
from flask import request

import kiva_client


logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)

connection = pymongo.MongoClient(os.environ['MONGOLAB_URI'])
db = connection.get_default_database()


@app.route('/users', methods=['POST'])
def create_user():
    """Store access token and secret"""
    payload = json.loads(request.data)

    if 'oauth_token' not in payload or 'oauth_token_secret' not in payload:
        logging.warn(
            '/login hit without providing oauth_token or oauth_token_secret')
        return flask.jsonify({
            'error': 'oauth_token and oauth_token_secret must be provided'
        }), 400

    oauth_token = payload['oauth_token']
    oauth_token_secret = payload['oauth_token_secret']
    id = str(uuid.uuid4())

    user = {
        '_id': id,
        'oauth_token': oauth_token,
        'oauth_token_secret': oauth_token_secret,
    }

    db.users.insert_one(user)
    logging.info("created user {}".format(json.dumps(user)))

    return flask.jsonify(user)


@app.route('/profile', methods=['GET'])
def profile():
    id = request.headers.get('Authorization', None)

    if not id:
        logging.warn(
            '/profile hit without providing id as Authorization header')
        return flask.jsonify({
            'error': 'id must be provided'
        }), 400

    user = db.users.find_one({'_id': id})
    if not user:
        logging.warn("no user found with id='{}'".format(id))
        return flask.jsonify({
            'error': 'user does not exist'
        }), 404

    logging.info("getting profile for user {}".format(user))

    client = kiva_client.KivaClient(
        user['oauth_token'], user['oauth_token_secret'])

    num_workers = 20
    pool = Pool(num_workers)

    account_raw, expected_repayments_raw, stats_raw, my_lender_raw = pool.map(
        executor,
        [
            client.my_account,
            client.my_expected_repayments,
            client.my_stats,
            client.my_lender,
        ],
    )

    profile_data = {}

    account = account_raw['content']
    for k, v in account['user_account'].iteritems():
        profile_data['account_%s' % k] = v
    #
    # expected_repayments = expected_repayments_raw['content']
    # profile_data['expected_repayments'] = []
    # for loan_id, loan_data in expected_repayments.iteritems():
    #     loan_data['id'] = loan_id
    #     profile_data['expected_repayments'].append(loan_data)

    stats = stats_raw['content']
    for k, v in stats.iteritems():
        profile_data['stats_%s' % k] = v

    my_lender = my_lender_raw['content']['lenders'][0]
    for k, v in my_lender.iteritems():
        if k == 'image':
            k = 'image_id'
            v = v['id']
        profile_data['lender_%s' % k] = v

    logging.debug(json.dumps(profile_data))
    logging.debug(json.dumps(profile_data, indent=True))

    return flask.jsonify(profile_data)


def executor(func_to_execute):
    return func_to_execute()


@app.errorhandler(404)
def page_not_found(error):
    return flask.jsonify({'error': 'not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
