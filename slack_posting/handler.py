import json

def slack_posting_webhook(event, context):

    print ('If I see this, set up is done correctly!')

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
