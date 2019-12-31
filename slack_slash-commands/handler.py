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

    get_gamercard(url) # Getting my gamercard from XBOXAPI

    # TODO: This should be more meaningful
    # aws lambda return response
    body = {
        "COME_BACK_TO_THIS": "Come back to this message"
    }

    response = {
        "statusCode": 200,
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
    print ('XboxAPI get status: {}' .format(res.status_code))
    
    print (res.content)
