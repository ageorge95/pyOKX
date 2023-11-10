from logging import getLogger
from typing import AnyStr
from OKX.network_wrappers import API_call
from OKX.utils import (check_API_key,
                       prepare_header)
from datetime import (datetime,
                      UTC)
from requests import delete,\
    post

class AccountEndpoints():
    _log: getLogger
    base_endpoint: AnyStr
    API_key: AnyStr
    API_secret: AnyStr
    API_passphrase: AnyStr

    def __init__(self):
        super(AccountEndpoints, self).__init__()

    @check_API_key
    def account_information(self,
                            ccy: AnyStr = '',
                            max_retries: int = 1):
        added_url = r'api/v5/account/balance'

        data={}
        if ccy: data['ccy'] = ccy

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=prepare_header(requestPath=added_url,
                                               body=data,
                                               API_secret=self.API_secret,
                                               API_key=self.API_key,
                                               passphrase=self.API_passphrase),
                        max_retries=max_retries).send()