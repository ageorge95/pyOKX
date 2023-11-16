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

    # get the price ticket snapshot for XCH-USDT
    # pprint(API_obj.get_ticker(instId='XCH-USDT'))

    # ########### account examples ###########
    # initialize the APi wrapper
    # API_obj = pyOKX(API_key=getenv('OKX_API_KEY'),
    #                 API_secret=getenv('OKX_API_SECRET'),
    #                 API_passphrase=getenv('OKX_API_PASSPHRASE'))

    # account information for all pairs
    # pprint(API_obj.account_information())

    # account information for XCH only
    # pprint(API_obj.account_information(ccy='BTC'))

    # opened positions for all assets
    # pprint(API_obj.get_positions())

    # opened positions for XCH_USDT
    # pprint(API_obj.get_positions(instId='XCH-USDT'))

    # closed positions for all assets
    # pprint(API_obj.get_positions_history())

    # closed positions for XCH_USDT
    # pprint(API_obj.get_positions_history(instId='XCH-USDT'))

    # opened orders for all assets
    # pprint(API_obj.pending_orders())

    # opened orders for XCH-USDT
    # pprint(API_obj.pending_orders(instId='XCH-USDT'))

    # specific order details
    # pprint(API_obj.order_details(instId='XCH-USDT',
    #                              ordId='645353830926131213'))