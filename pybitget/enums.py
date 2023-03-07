# http header
CONTENT_TYPE = 'Content-Type'
ACCESS_KEY = 'ACCESS-KEY'
ACCESS_SIGN = 'ACCESS-SIGN'
ACCESS_TIMESTAMP = 'ACCESS-TIMESTAMP'
ACCESS_PASSPHRASE = 'ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'

# header key
ACEEPT = 'Accept'
COOKIE = 'Cookie'
LOCALE = 'locale='

# method
GET = "GET"
POST = "POST"
DELETE = "DELETE"

# Base Url
API_URL = 'https://api.bitget.com'

# ws Url
CONTRACT_WS_URL = 'wss://ws.bitget.com/mix/v1/stream'

# ########################################
# ##############【spot url】###############
# ########################################

SPOT_PUBLIC_V1_URL = '/api/spot/v1/public'
SPOT_MARKET_V1_URL = '/api/spot/v1/market'
SPOT_ACCOUNT_V1_URL = '/api/spot/v1/account'
SPOT_ORDER_V1_URL = '/api/spot/v1/trade'
SPOT_WALLET_V1_URL = '/api/spot/v1/wallet'
SPOT_PLAN_V1_URL = '/api/spot/v1/plan'

# ########################################
# ##############【mix url】################
# ########################################

MIX_MARKET_V1_URL = '/api/mix/v1/market'
MIX_ACCOUNT_V1_URL = '/api/mix/v1/account'
MIX_POSITION_V1_URL = '/api/mix/v1/position'
MIX_ORDER_V1_URL = '/api/mix/v1/order'
MIX_PLAN_V1_URL = '/api/mix/v1/plan'
MIX_TRACE_V1_URL = '/api/mix/v1/trace'

BROKER_ACCOUNT_V1_URL = '/api/broker/v1/account'
BROKER_MANAGE_V1_URL = '/api/broker/v1/manage'

SUBSCRIBE = 'subscribe'
UNSUBSCRIBE = 'unsubscribe'
LOGIN = 'login'

REQUEST_PATH = '/user/verify'

SERVER_TIMESTAMP_URL = '/api/spot/v1/public/time'

# SIDE - Order direction
NEW_BUY = "open_long"
NEW_SELL = "open_short"
BUY_CLOSE = 'close_long'
SELL_CLOSE = 'close_short'
PS_BUY = "long"
PS_SELL = "short"

# orderType
ORDER_TYPES = ['limit', 'market']
ORDER_TYPE_LIMIT = 'limit'
ORDER_TYPE_MARKET = 'market'
ORDER_SIDES = ['long', 'short']


# orderStatus - state
ORDER_STATUS_OP = ['new']
ORDER_STATUS_NEW = 'new'
ORDER_STATUS_CANCELED = 'canceled'
ORDER_STATUS_FILLED = 'filled'
ORDER_STATUS_FILLEDs = ['partially_filled', 'filled']
ORDER_STATUS_TYPES = ['init', 'new', 'partially_filled', 'filled', 'canceled']

# stopType
STOP_TYPES = ['profit', 'loss']
STOP_TYPE_PROFIT = "profit"
STOP_TYPE_LOSS = "loss"

# timeInForceValue
TIME_IN_FORCE_TYPES = ['normal', 'post_only', 'fok', 'ioc']
# triggerType
TRIGGER_TYPES = ['fill_price', 'market_price']

# planType
PLAN_TYPES = ['profit_plan', 'loss_plan', 'normal_plan', 'pos_profit', 'pos_loss', 'moving_plan', 'track_plan']

# planStatus
PLAN_STATUS_NOT_TRIGGER = "not_trigger"
PLAN_STATUS_TRIGGERED = "triggered"
PLAN_STATUS_FAIL_TRIGGER = "fail_trigger"
PLAN_STATUS_CANCEL = "cancel"
PLAN_TYPE_POS_PROFIT = "pos_profit"
PLAN_TYPE_POS_LOSS = "pos_loss"

# isPlan
IS_PLAN_TYPES = ['plan', 'profit_loss']
# Plan
isPlan_plan = "plan"
isPlan_profit_loss = "profit_loss"


# symbolStatus
SYMBOL_STATUS_TYPES = ['normal', 'maintain', 'off']


PRODUCT_TYPE_UMCBL = 'umcbl'
PRODUCT_TYPE_SUMCBL = 'sumcbl'  # demo ?
MARGIN_COIN_USDT = 'USDT'
MARGIN_COIN_USDC = 'USDC'
MARGIN_COIN_SUSDT = 'SUSDT'  # demo?
# Websocket planType
WS_PLAN_TYPES = ['pl', 'tp', 'sl', 'ptp', 'psl']

# Websocket channels type
WS_PRIVATE_ACCOUNT_CHANNEL = "account"
WS_PRIVATE_ORDERS_CHANNEL = "orders"
WS_PRIVATE_POSITIONS_CHANNEL = "positions"
WS_PRIVATE_PLAN_ORDERS_CHANNEL = "ordersAlgo"
WS_CHANNEL_INSTTYPE = "UMCBL"
WS_CHANNEL_INSTID = "default"


# === API define fields name
ORDER_STATUS = "state"
ORDER_TYPE_NAME = "orderType"
STOP_PRICE_FIELD = "triggerPrice"
