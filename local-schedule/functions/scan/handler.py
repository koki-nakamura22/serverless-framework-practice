import os
import boto3


if os.getenv('IS_LOCAL'):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
    dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(f"TestScheduleTable-{os.environ['STAGE']}")


def scan(event, context):
    response = {
        "statusCode": 200,
        "body": table.scan()
    }

    return response
