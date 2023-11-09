from logging import getLogger
from typing import (AnyStr,
                    List,
                    Literal)
from OKX.network_wrappers import API_call

class PublicEndpoints():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicEndpoints, self).__init__()

    def get_instruments(self,
                        instId: AnyStr = '',
                        max_retries: int = 1,
                        instType: Literal['SPOT', 'MARGIN', 'SWAP', 'FUTURES', 'OPTION'] = 'SPOT'):

        added_url = r'api/v5/public/instruments'

        data = {'instType': instType}

        if instId: data |= {'instId': instId}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        max_retries=max_retries).send()
