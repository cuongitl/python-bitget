from pybitget import Client
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
def cancel_orders(orderId):
    s = iClient.mix_cancel_order(symbol, marginCoin, orderId)
    logger.debug(s)
    """
    # {'code': '00000', 'msg': 'success', 'requestTime': 1674878544944, 'data': {'orderId': '1003067092170850306', 'clientOid': 'Cuongitl_g9dl0artxawgpqa'}}
    """


cancel_orders(1003067092170850306)
