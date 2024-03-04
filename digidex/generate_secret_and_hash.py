import uuid
import hashlib

def generate_secret_and_hash():
    secret = uuid.uuid4().hex
    secret_hash = hashlib.sha256(secret.encode()).hexdigest()
    return secret, secret_hash
