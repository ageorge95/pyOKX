from logging import getLogger
from typing import AnyStr
from OKX.endpoints.public import PublicEndpoints

base_endpoint: AnyStr = 'https://www.okx.com'

class pyOKX(PublicEndpoints):

    def __init__(self,
                 API_key: AnyStr = None,
                 API_secret: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key
        self.API_secret = API_secret

        self.base_endpoint = base_endpoint

        super(pyOKX, self).__init__()
