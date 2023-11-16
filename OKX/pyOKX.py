from logging import getLogger
from typing import AnyStr
from OKX.endpoints.public import PublicEndpoints
from OKX.endpoints.market import MarketEndpoints
from OKX.endpoints.account import AccountEndpoints

base_endpoint: AnyStr = 'https://okx.com'

class pyOKX(PublicEndpoints,
            MarketEndpoints,
            AccountEndpoints):

    def __init__(self,
                 API_key: AnyStr = None,
                 API_secret: AnyStr = None,
                 API_passphrase: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key
        self.API_secret = API_secret
        self.API_passphrase = API_passphrase

        self.base_endpoint = base_endpoint

        super(pyOKX, self).__init__()
