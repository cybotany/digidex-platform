import boto3
import json
from decouple import config
import os

def get_secret(secret_name, environment=None, region_name=None):
    """
    Fetch the secret value from AWS Secrets Manager or .env depending on the environment.
    """
    # Determine environment
    if not environment:
        environment = os.environ.get('DJANGO_ENV', 'development')

    # Fetching secret for production
    if environment == 'production':
        if not region_name:
            raise ValueError("AWS region must be specified when fetching secrets in production.")
        
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

    # Fetching secret for non-production environments
    else:
        secret_str = config(secret_name, default="{}")
        try:
            return json.loads(secret_str)
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON for secret {secret_name}") from None
