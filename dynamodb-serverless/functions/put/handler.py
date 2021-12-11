import json
import os
import boto3
from faker import Faker


# DynamoDB object
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(f"TestUsersTable-{os.environ['STAGE']}")


def __truncate():
    response = table.scan()
    key_names = [ x["AttributeName"] for x in table.key_schema ]
    delete_keys = [ { k:v for k,v in x.items() if k in key_names } for x in response["Items"] ]
    with table.batch_writer() as batch:
        for key in delete_keys:
            batch.delete_item(Key = key)


def __put(id, name):
    table.put_item(
        Item = {
            "id" : id,
            "name" : name,
        }
    )


def put(event, context):
    __truncate()
    fake = Faker()
    for n in range(1, 10 + 1):
        __put(str(n).zfill(3), fake.name())

    response = {
        "statusCode": 200,
    }

    return response
