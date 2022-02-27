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


def get_object(event, context):
    file_name = "test.txt"
    obj = bucket.Object(file_name)

    response = obj.get()
    response_body = response['Body'].read()

    body = {
        "content": response_body.decode("utf-8")
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
