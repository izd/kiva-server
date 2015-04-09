import requests

local_url = 'http://127.0.0.1:5000'
heroku_url = 'http://kiva-server.herokuapp.com'

response = requests.get(
    '{}/profile'.format(heroku_url),
    headers={
        'Authorization': '1ec3dbed-a82f-474c-a1df-ed5514ec4cdc'
    },
)
print "Code: {}, json: {}".format(response.status_code, response.json())
