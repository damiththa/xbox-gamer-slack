import json
import os

import requests

#xbox
XBOX_PROFILE_ID = os.environ['XBOX_PROFILE_ID']

#xboxapi
XBOX_API_BASE_URL = os.environ['XBOX_API_BASE_URL']
XBOX_API_KEY = os.environ['XBOX_API_KEY']

def get_xboxgamer_info(event, context):

    print (event)
    # TODO: should do a auth code check

    # url
    url = XBOX_API_BASE_URL + XBOX_PROFILE_ID

    res = get_gamercard(url) # Getting my gamercard from XBOXAPI
    print (res.status_code)
    print (res.content)

    # TODO: Need to better handle non-200 response
    if res.status_code != 200:
        print ('something went wrong in api return')
    
    xboxapi_return = json.loads(res.content) # getting json in as python data
    # print (xboxapi_return)

    # print (xboxapi_return['gamertag']) # gamertag

    # NOTEME: This is the message reply message body
    body = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hello " + str(xboxapi_return['name']) + " here is your gamercard."
                }
            },
            {
			    "type": "divider"
		    },
            {
                "type": "section",
                "block_id": "section567",
                "text": {
                    "type": "mrkdwn",
                    "text": "\n *gamertag: *" +  str(xboxapi_return['gamertag']) + "\n *motto: *" + "_"+str(xboxapi_return['motto'])+"_" + "\n *gamerscore: *" + str(xboxapi_return['gamerscore'])
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://image-ssl.xboxlive.com/global/t.fffe07d1/tile/0/21046",
                    "alt_text": str(xboxapi_return['gamertag']) + " gamer pic."
                }
            }
        ]
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
