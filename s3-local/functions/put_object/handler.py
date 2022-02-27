import json
import os
import boto3


if os.getenv("IS_LOCAL"):
    bucket_name = "local-bucket"
    s3 = boto3.resource(
        "s3",
        aws_access_key_id="S3RVER",
        aws_secret_access_key="S3RVER",
        endpoint_url="http://localhost:4569")
else:
    bucket_name = "s3-local-test-bucket"
    s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)


def put_object(event, context):
    file_name = "test.txt"
    text_body = """Hello World
hoge
fuga
"""
    r = bucket.put_object(Key=file_name, Body=text_body.encode("utf-8"))

    body = {
        "result": str(r)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
