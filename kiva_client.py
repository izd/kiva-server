
import time
import json
import oauth2 as oauth

consumer = oauth.Consumer(consumer_key, consumer_secret)

base = 'https://api.kivaws.org/v1/'


class KivaClient(object):

    def __init__(self, oauth_token, oauth_token_secret):
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret

    def get(self, url):
        url = base + url

        params = {
            'oauth_version': "1.0",
            'oauth_nonce': oauth.generate_nonce(),
            'oauth_timestamp': int(time.time())
        }

        # Set our token/key parameters
        token = oauth.Token(self.oauth_token, self.oauth_token_secret)
        params['oauth_token'] = self.oauth_token
        params['oauth_consumer_key'] = consumer.key

        # Create our request. Change method, etc. accordingly.
        req = oauth.Request(method="GET", url=url, parameters=params)

        # Sign the request.
        signature_method = oauth.SignatureMethod_HMAC_SHA1()
        req.sign_request(signature_method, consumer, token)
        client = oauth.Client(consumer, token)
        resp, content = client.request(url, "GET")

        return {'status': resp['status'], 'content': json.loads(content)}

    def my_account(self):
        return self.get('my/account.json')

    def my_stats(self):
        return self.get('my/stats.json')

    def my_expected_repayments(self):
        return self.get('my/expected_repayments.json')

    def my_loans(self):
        return self.get('my/loans.json')
