from decimal import Decimal
import os
import time
import boto3


if os.getenv('IS_LOCAL'):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
else:
    dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(f"TestScheduleTable-{os.environ['STAGE']}")


def put(event, context):
    t = time.time()
    table.put_item(
        Item = {
            "timestamp" : Decimal(t)
        }
    )

    response = {
        "statusCode": 200
    }

    return response
