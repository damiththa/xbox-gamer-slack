import json
import os

import requests

#xbox
XBOX_PROFILE_ID = os.environ['XBOX_PROFILE_ID']

#xboxapi
XBOX_API_BASE_URL = os.environ['XBOX_API_BASE_URL']
XBOX_API_KEY = os.environ['XBOX_API_KEY']

def get_xboxgamer_info(event, context):

    # url
    url = XBOX_API_BASE_URL + XBOX_PROFILE_ID

    r = get_gamercard(url) # Getting my gamercard from XBOXAPI
    print (r.status_code)
    print (r.content)

    # TODO: Need to better handle non-200 response
    if r.status_code != 200:
        print ('something went wrong in api return')

    # NOTEME: This is the message reply message body
    body = {
        "returnBody": "Come back to this message"
    }

    response = {
        "statusCode": 200, # CHECKME: see whether this status code can be dynamic
        "body": json.dumps(body)
    }

    return response

# Getting my gamercard from XBOXAPI
def get_gamercard(url):
    url = url + '/gamercard'
    # print (url)
    headers = {
        'Content-Type' : 'application/json',
        "X-Auth" : XBOX_API_KEY
    }
    payload = {
        'message': 'This is just a dummy message, probably not needed'
    }

    res = requests.get(url, headers=headers, data=json.dumps(payload))

    # print ('XboxAPI get status: {}' .format(res.status_code))
    # print (res.content)

    return res
