from urllib.parse import urlencode
from hashlib import sha256
from hmac import digest

def check_API_key(func):
    def inner(*args, **kwargs):
        if not args[0].API_key or not args[0].API_secret:
            args[0]._log.error(f'{func.__name__} requires an API key and API secret!')
        return func(*args, **kwargs)
    return inner

def hmac_signature(data,
                   API_secret):
    queryString = urlencode(data)
    return digest(API_secret.encode('utf-8'),
                  queryString.encode('utf-8'),
                  sha256).hex()