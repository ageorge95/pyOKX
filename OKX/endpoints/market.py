from logging import getLogger
from typing import (AnyStr,
                    List,
                    Literal)
from OKX.network_wrappers import API_call

class MarketEndpoints():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(MarketEndpoints, self).__init__()

    def get_orderbook(self,
                      instId: AnyStr,
                      sz: AnyStr = '10',
                      max_retries: int = 1):

        added_url = r'api/v5/market/books'

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data={'instId': instId,
                              'sz': sz},
                        max_retries=max_retries).send()
