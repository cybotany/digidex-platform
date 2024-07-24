from django.conf import settings

def build_uri(path):
    """
    Build a complete URI using the base URL and a given path.
    """
    host_scheme = settings.HOST_SCHEME
    parent_host = settings.PARENT_HOST.rstrip('/')
    if parent_host == 'localhost':
        parent_host += ':8000'
    path = path.lstrip('/')
    return f"{host_scheme}://{parent_host}/{path}"
