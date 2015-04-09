import requests

base_url = 'http://127.0.0.1:5000'
response = requests.get(
    '{}/profile'.format(base_url),
    headers={
        'Authorization': '2250e0e7-bc69-4e96-80fa-5f0913b06a1b'
    },
)
print "Code: {}, json: {}".format(response.status_code, response.json())
