import boto3
import json
import os

def get_secret(secret_name, region_name=None):
    """
    Fetch the secret value from AWS Secrets Manager.
    """
    # Set default region if not provided
    if not region_name:
        region_name = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        response = client.get_secret_value(SecretId=secret_name)
        # Check if SecretString exists in the response
        if 'SecretString' in response:
            secret = response['SecretString']
            return json.loads(secret)
        else:
            raise ValueError("SecretString not found in the response from Secrets Manager")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch secret {secret_name} from AWS: {str(e)}") from e
