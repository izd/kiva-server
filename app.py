
import os
import json

import flask
import pymongo

import kiva_client

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

mongo_client = pymongo.MongoClient(os.environ['MONGOLAB_URI'])
mongo_db = mongo_client['main_db']

# accept in post from client and store eventually

@app.route('/profile')
def profile():
    profile_data = {}

    # TODO: take tokens from POST body
    client = kiva_client.KivaClient(oauth_token, oauth_token_secret)

    # step 1

    account = client.my_account()['content']
    for k, v in account['user_account'].iteritems():
        profile_data['account_%s' % k] = v

    expected_repayments = client.my_expected_repayments()['content']
    profile_data['expected_repayments'] = []
    for loan_id, loan_data in expected_repayments.iteritems():
        loan_data['id'] = loan_id
        profile_data['expected_repayments'].append(loan_data)

    stats = client.my_stats()['content']
    for k, v in stats.iteritems():
        profile_data['stats_%s' % k] = v

    print json.dumps(client.my_loans(), indent=True)

    # step 2

    return flask.jsonify(profile_data)


@app.errorhandler(404)
def page_not_found(error):
    return flask.jsonify({'error': 'not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
