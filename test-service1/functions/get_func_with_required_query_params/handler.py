import json

def get_func_with_required_query_params(event, context):
    body = {
        "param1": event.get('queryStringParameters').get('param1'),
        "param2": event.get('queryStringParameters').get('param2'),
        "param3": event.get('queryStringParameters').get('param3')
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
