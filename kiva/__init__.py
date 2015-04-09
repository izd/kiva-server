
import time
import json
import oauth2 as oauth


def request(oauth_token, oauth_token_secret):
    consumer_key = 'com.kiva.dotdot2'
    consumer_secret = 'lgvkDDBFtRximElyzqytqAvclDxFzpqu'
    consumer = oauth.Consumer(consumer_key, consumer_secret)

    params = {
        'oauth_version': "1.0",
        'oauth_nonce': oauth.generate_nonce(),
        'oauth_timestamp': int(time.time())
    }

    # Set our token/key parameters
    token = oauth.Token(oauth_token, oauth_token_secret)
    params['oauth_token'] = oauth_token
    params['oauth_consumer_key'] = consumer.key

    # This is the URL of the protected resource you want to access
    resource_url = 'https://api.kivaws.org/v1/my/account.json'

    # Create our request. Change method, etc. accordingly.
    req = oauth.Request(method="GET", url=resource_url, parameters=params)

    # Sign the request.
    signature_method = oauth.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)
    client = oauth.Client(consumer, token)
    resp, content = client.request(resource_url, "GET")

    return {'status': resp['status'], 'content': json.loads(content)}
