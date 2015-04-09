import json

import requests


base_url = 'http://127.0.0.1:5000'
response = requests.post(
    '{}/users'.format(base_url),
    data=json.dumps(
        {
            'oauth_token': 'OAUTH_TOKEN',
            'oauth_token_secret': 'OAUTH_TOKEN_SECRET'
        }
    )
)
print "Code: {}, json: {}".format(response.status_code, response.json())
