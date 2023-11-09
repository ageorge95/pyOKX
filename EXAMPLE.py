from ag95 import configure_logger
from OKX.pyOKX import pyOKX
from pprint import pprint
from os import getenv

if __name__ == '__main__':
    configure_logger()
    # ########### public examples ###########
    # initialize the APi wrapper
    # API_obj = pyOKX()

    # get all SPOT instruments data
    # pprint(API_obj.get_instruments(instType='SPOT'))

    # get the XCH-USDT SPOT instrument data
    # pprint(API_obj.get_instruments(instType='SPOT',
    #                                instId='XCH-USDT'))

    # ########### public examples ###########
    # initialize the APi wrapper
    # API_obj = pyOKX()

    # get orderbook for XCH-USDT with the default 10 entries
    # pprint(API_obj.get_orderbook(instId='XCH-USDT'))