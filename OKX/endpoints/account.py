from logging import getLogger
from typing import (AnyStr,
                    Literal)
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

    @check_API_key
    def get_positions(self,
                      instId: AnyStr = '',
                      posId: AnyStr = '',
                      max_retries: int = 1):
        added_url = r'api/v5/account/positions'

        data={}
        if instId: data['instId'] = instId
        if posId: data['posId'] = posId

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=prepare_header(requestPath=added_url,
                                               body=data,
                                               API_secret=self.API_secret,
                                               API_key=self.API_key,
                                               passphrase=self.API_passphrase),
                        max_retries=max_retries).send()

    @check_API_key
    def get_positions_history(self,
                              instId: AnyStr = '',
                              limit: int = 10,
                              max_retries: int = 1):
        added_url = r'api/v5/account/positions-history'

        data={'limit': limit}
        if instId:
            data['instId'] = instId

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=prepare_header(requestPath=added_url,
                                               body=data,
                                               API_secret=self.API_secret,
                                               API_key=self.API_key,
                                               passphrase=self.API_passphrase),
                        max_retries=max_retries).send()

    @check_API_key
    def pending_orders(self,
                       instType: AnyStr = 'SPOT',
                       instId: AnyStr = '',
                       limit: int = 10,
                       max_retries: int = 1):
        added_url = r'api/v5/trade/orders-pending'

        data={'limit': limit,
              'instType': instType}
        if instId: data['instId'] = instId

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=prepare_header(requestPath=added_url,
                                               body=data,
                                               API_secret=self.API_secret,
                                               API_key=self.API_key,
                                               passphrase=self.API_passphrase),
                        max_retries=max_retries).send()

    @check_API_key
    def order_details(self,
                      instId: AnyStr,
                      ordId: AnyStr,
                      max_retries: int = 1):
        added_url = r'api/v5/trade/order'

        data={'instId': instId,
              'ordId': ordId}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=prepare_header(requestPath=added_url,
                                               body=data,
                                               API_secret=self.API_secret,
                                               API_key=self.API_key,
                                               passphrase=self.API_passphrase),
                        max_retries=max_retries).send()

    @check_API_key
    def cancel_order(self,
                     instId: AnyStr,
                     ordId: AnyStr,
                     max_retries: int = 1):
        added_url = r'api/v5/trade/cancel-order'

        data = {'instId': instId,
                'ordId': ordId}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=prepare_header(requestPath=added_url,
                                               body=data,
                                               API_secret=self.API_secret,
                                               API_key=self.API_key,
                                               passphrase=self.API_passphrase,
                                               method='POST'),
                        max_retries=max_retries,
                        call_method=post).send()

    @check_API_key
    def post_order(self,
                   instId: AnyStr,
                   side: Literal['sell', 'buy'],
                   sz: AnyStr,
                   px: AnyStr,
                   tdMode: AnyStr = 'cash',
                   ordType: AnyStr = 'limit',
                   max_retries: int = 1):
        added_url = r'api/v5/trade/order'

        data = {'instId': instId,
                'side': side,
                'sz': sz,
                'px': px,
                'tdMode': tdMode,
                'ordType': ordType}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=prepare_header(requestPath=added_url,
                                               body=data,
                                               API_secret=self.API_secret,
                                               API_key=self.API_key,
                                               passphrase=self.API_passphrase,
                                               method='POST'),
                        max_retries=max_retries,
                        call_method=post).send()