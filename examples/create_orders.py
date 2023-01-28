from pybitget import Client
from pybitget.utils import random_string
from pybitget.enums import *
from pybitget import logger

# ==========
api_key = "your-api-key"
api_secret = "your-secret-key"
api_passphrase = "your-api-passphrase"
iClient = Client(api_key, api_secret, api_passphrase, use_server_time=False)

# ====
symbol = "SBTCSUSDT_SUMCBL"
marginCoin = "SUSDT"


# ====
def place_order(orderType):
    size = "0.01"
    side = NEW_BUY
    price = 15000
    s = iClient.mix_place_order(symbol, marginCoin, size, side, orderType, price=price, clientOrderId=random_string("Cuongitl"))
    logger.debug(s)
    """
    # {'code': '00000', 'msg': 'success', 'requestTime': 1674875751521, 'data': {'clientOid': 'Cuongitl_g9dl0artxawgpqa', 'orderId': '1003067092170850306'}}
    """


def place_tp():
    """ create take-profit """
    planType = "pos_profit"
    triggerPrice = "25000.5"
    triggerType = "fill_price"  # market_price
    holdSide = PS_BUY
    s = iClient.mix_place_PositionsTPSL(symbol, marginCoin, planType, triggerPrice, triggerType, holdSide=holdSide)
    logger.debug(s)
    """
    # Place TP:
    {'code': '00000', 'msg': 'success', 'requestTime': 1674877422768, 'data': {'clientOid': '1003074101962153984', 'orderId': '1003074101962153985'}}
    """


def place_sl():
    """ create stop-loss """
    planType = "pos_loss"
    triggerPrice = "13000.5"
    triggerType = "fill_price"  # market_price
    holdSide = PS_BUY
    s = iClient.mix_place_PositionsTPSL(symbol, marginCoin, planType, triggerPrice, triggerType, holdSide=holdSide)
    logger.debug(s)
    """
    # Place SL:
    {'code': '00000', 'msg': 'success', 'requestTime': 1674877475451, 'data': {'clientOid': '1003074322897117184', 'orderId': '1003074322897117185'}}
    """


# place_order("limit")
place_order("market")
# place_tp()
# place_sl()
