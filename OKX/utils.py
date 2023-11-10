from urllib.parse import urlencode
from hashlib import sha256
from hmac import digest
from base64 import b64encode
from datetime import datetime

def check_API_key(func):
    def inner(*args, **kwargs):
        if not args[0].API_key or not args[0].API_secret:
            args[0]._log.error(f'{func.__name__} requires an API key and API secret!')
        return func(*args, **kwargs)
    return inner

def prepare_header(requestPath,
                   body,
                   API_secret,
                   API_key,
                   passphrase,
                   method='GET'):

    timestamp = datetime.utcnow().isoformat("T", "milliseconds") + 'Z'
    body = '?' + urlencode(body) if body else ''
    prehash = timestamp + method + f"/{requestPath}" + body

    print(prehash)

    return {'OK-ACCESS-KEY': API_key,
            'OK-ACCESS-SIGN': b64encode(digest(API_secret.encode('utf-8'),
                                        prehash.encode('utf-8'),
                                        sha256)),
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': passphrase}