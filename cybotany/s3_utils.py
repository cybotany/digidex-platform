import boto3


def get_s3_client():
    return boto3.client('s3')


def list_bucket_objects(bucket_name):
    s3 = get_s3_client()
    response = s3.list_objects(Bucket=bucket_name)
    return response
