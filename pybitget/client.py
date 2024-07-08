import requests
import json
from pybitget.enums import *
from pybitget import utils
from pybitget import exceptions
from pybitget import logger


class Client(object):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, verbose=False):

        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time
        self.verbose = verbose

    def _request(self, method, request_path, params, cursor=False):
        if method == GET:
            request_path = request_path + utils.parse_params_to_str(params)
        # url
        url = API_URL + request_path

        # Get local time
        timestamp = utils.get_timestamp()

        # sign & header
        if self.use_server_time:
            # Get server time interface
            timestamp = self._get_timestamp()

        body = json.dumps(params) if method == POST else ""
        sign = utils.sign(utils.pre_hash(timestamp, method, request_path, str(body)), self.API_SECRET_KEY)
        header = utils.get_header(self.API_KEY, sign, timestamp, self.PASSPHRASE)

        # send request
        response = None
        if method == GET:
            response = requests.get(url, headers=header)
        elif method == POST:
            response = requests.post(url, data=body, headers=header)
        elif method == DELETE:
            response = requests.delete(url, headers=header)
        # exception handle
        if not str(response.status_code).startswith('2'):
            raise exceptions.BitgetAPIException(response)
        try:
            res_header = response.headers
            if cursor:
                r = dict()
                try:
                    r['before'] = res_header['BEFORE']
                    r['after'] = res_header['AFTER']
                except:
                    pass
                return response.json(), r
            else:
                return response.json()

        except ValueError:
            raise exceptions.BitgetRequestException('Invalid Response: %s' % response.text)

    def _request_without_params(self, method, request_path):
        return self._request(method, request_path, {})

    def _request_with_params(self, method, request_path, params, cursor=False):
        return self._request(method, request_path, params, cursor)

    def _get_timestamp(self):
        url = API_URL + SERVER_TIMESTAMP_URL
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['data']
        else:
            return ""

    """ --- MIX-MarkettApi """

    def mix_get_vip_fee_rate(self):
        """
        VIP fee rate: https://bitgetlimited.github.io/apidoc/en/mix/#vip-fee-rate
        Limit rule: 10 times/1s (IP)
        Required: None
        :return:
        """
        return self._request_without_params(GET, MIX_MARKET_V1_URL + '/contract-vip-level')

    def mix_get_symbols_info(self, productType):
        """
        Get All symbols: https://bitgetlimited.github.io/apidoc/en/mix/#get-all-symbols
        Limit rule: 20 times/1s (IP)
        Required: productType
        :return:
        """
        params = {}
        if productType:
            params["productType"] = productType
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/contracts', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_depth(self, symbol, limit=100):
        """
        Get Depth: https://bitgetlimited.github.io/apidoc/en/mix/#get-depth

        Limit rule: 20 times/1s (IP)

        Required: symbol

        :param symbol: Symbol Id (Must be capitalized)
        :type symbol: str
        :param limit: Depth gear 5，15，50，100 default 100
        :type limit: str
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/depth', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_single_symbol_ticker(self, symbol):
        """
        Get Single Symbol Ticker: https://bitgetlimited.github.io/apidoc/en/mix/#get-single-symbol-ticker

        Limit rule: 20 times/1s (IP)

        Required: symbol

        :param symbol: Symbol Id (Must be capitalized)
        :type symbol: str
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/ticker', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_all_symbol_ticker(self, productType):
        """
        Get All Symbol Ticker: https://bitgetlimited.github.io/apidoc/en/mix/#get-all-symbol-ticker

        Limit rule: 20 times/1s (IP)

        Required: productType
        :return:
        """
        params = {}
        if productType:
            params["productType"] = productType
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/tickers', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_fills(self, symbol, limit=100):
        """
        Get recent trades: https://bitgetlimited.github.io/apidoc/en/mix/#get-fills

        Limit rule: 20 times/1s (IP)

        Required: symbol, limit

        :param symbol: Symbol Id (Must be capitalized)
        :type symbol: str
        :param limit: Default limit is 100
        :type limit: str
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/fills', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_candles(self, symbol, granularity, startTime, endTime, kLineType='market', limit=100):
        """
        Get Candle Data: https://bitgetlimited.github.io/apidoc/en/mix/#get-candle-data
        Limit rule: 20 times/1s (IP)
        Required: symbol, granularity, startTime, endTime
        :return:
        """
        params = {}
        if symbol and granularity and startTime and endTime:
            params["symbol"] = symbol
            params["granularity"] = granularity
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["kLineType"] = kLineType
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/candles', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_history_candles(self, symbol, granularity, startTime, endTime, limit=100):
        """
        Get History Candle Data: https://bitgetlimited.github.io/apidoc/en/mix/#get-history-candle-data
        Limit rule: 20 times/1s (IP)
        Required: symbol, granularity, startTime, endTime
        :return:
        """
        params = {}
        if symbol and granularity and startTime and endTime:
            params["symbol"] = symbol
            params["granularity"] = granularity
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["limit"] = limit
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/history-candles', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_symbol_index_price(self, symbol):
        """
        Get Symbol Index Price: https://bitgetlimited.github.io/apidoc/en/mix/#get-symbol-index-price
        Limit rule: 20 times/1s (IP)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/index', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_symbol_next_funding(self, symbol):
        """
        Get Symbol Next Funding Time: https://bitgetlimited.github.io/apidoc/en/mix/#get-symbol-next-funding-time
        Limit rule: 20 times/1s (IP)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/funding-time', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_history_fund_rate(self, symbol, pageSize=20, pageNo=1, nextPage=False):
        """
        Get History Funding Rate: https://bitgetlimited.github.io/apidoc/en/mix/#get-history-funding-rate
        Limit rule: 20 times/1s (IP)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            params["nextPage"] = nextPage
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/history-fundRate', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_current_fund_rate(self, symbol):
        """
        Get Current Funding Rate: https://bitgetlimited.github.io/apidoc/en/mix/#get-current-funding-rate
        Limit rule: 20 times/1s (IP)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/current-fundRate', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_open_interest(self, symbol):
        """
        Get Open Interest: https://bitgetlimited.github.io/apidoc/en/mix/#get-open-interest
        Limit rule: 20 times/1s (IP)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/open-interest', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_market_price(self, symbol):
        """
        Get Symbol Mark Price: https://bitgetlimited.github.io/apidoc/en/mix/#get-symbol-mark-price
        Limit rule: 20 times/1s (IP)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/mark-price', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_leverage(self, symbol):
        """
        Get Symbol Leverage: https://bitgetlimited.github.io/apidoc/en/mix/#get-symbol-leverage
        Limit rule: 20/sec (IP)
        Required: symbol.

        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/symbol-leverage', params)
        else:
            logger.error("pls check args")
            return False

    """ --- MIX-AccountApi """

    def mix_get_account(self, symbol, marginCoin):
        """
        Get Single Account: https://bitgetlimited.github.io/apidoc/en/mix/#get-single-account
        Required: symbol, marginCoin
        :return:
        """
        params = {}
        if symbol and marginCoin:
            params['symbol'] = symbol
            params['marginCoin'] = marginCoin
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/account', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_accounts(self, productType):
        """
        Get Account List: https://bitgetlimited.github.io/apidoc/en/mix/#get-account-list
        productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
        :return:
        """
        params = {}
        if productType:
            params['productType'] = productType
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accounts', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_sub_account_contract_assets(self, productType):
        """
        Get sub Account Contract Assets: https://bitgetlimited.github.io/apidoc/en/mix/#get-sub-account-contract-assets
        Limit rule: 1 times/10s (uid)
        Required: productType
        :return:
        """
        params = {}
        if productType:
            params['productType'] = productType
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/sub-account-contract-assets', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_open_count(self, symbol, marginCoin, openPrice, openAmount, leverage=20):
        """
        Get Open Count: https://bitgetlimited.github.io/apidoc/en/mix/#get-open-count
        Limit rule: 20 times/1s (IP)
        Required: symbol, marginCoin, openPrice, openAmount

        """
        params = {}
        if symbol and marginCoin and openPrice and openAmount:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["openPrice"] = openPrice
            params["openAmount"] = openAmount
            params["leverage"] = leverage
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/open-count', params)
        else:
            logger.error("pls check args")
            return False

    def mix_adjust_leverage(self, symbol, marginCoin, leverage, holdSide=None):
        """
        Change Leverage: https://bitgetlimited.github.io/apidoc/en/mix/#change-leverage
        Limit rule: 5 times/1s (uid)
        The leverage could set to different number in fixed margin mode(holdSide is required)
        Required: symbol, marginCoin, leverage

        """
        params = {}
        if symbol and marginCoin and leverage:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["leverage"] = leverage
            if holdSide is not None:
                params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setLeverage', params)
        else:
            logger.error("pls check args")
            return False

    def mix_adjust_margin(self, symbol, marginCoin, amount, holdSide=None):
        """
        Change Margin: https://bitgetlimited.github.io/apidoc/en/mix/#change-margin
        Limit rule: 5 times/1s (uid)
        Required: symbol, marginCoin, marginMode
        """
        params = {}
        if symbol and marginCoin and amount:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["marginMode"] = amount
            if holdSide is not None:
                params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMargin', params)
        else:
            logger.error("pls check args")
            return False

    def mix_adjust_margintype(self, symbol, marginCoin, marginMode):
        """
        Change Margin Mode: https://bitgetlimited.github.io/apidoc/en/mix/#change-margin-mode
        Limit rule: 5 times/1s (uid)
        Required: symbol, marginCoin, marginMode
        """
        params = {}
        if symbol and marginCoin and marginMode:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["marginMode"] = marginMode

            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMarginMode', params)
        else:
            logger.error("pls check args")
            return False

    def mix_adjust_hold_mode(self, productType, holdMode):
        """
        Change Hold Mode: https://bitgetlimited.github.io/apidoc/en/mix/#change-hold-mode
        Limit rule: 5 times/1s (uid)
        Required: productType, holdMode
        """
        params = {}
        if productType and holdMode:
            params["productType"] = productType
            params["holdMode"] = holdMode
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setPositionMode', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_single_position(self, symbol, marginCoin=None):
        """
            Obtain the user's single position information.
            Get Symbol Position: https://bitgetlimited.github.io/apidoc/en/mix/#get-symbol-position

            :param symbol: Name of symbol
            :type symbol: str
            :param marginCoin: Margin currency (Must be capitalized)
            :type marginCoin: str
            :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            if marginCoin is not None:
                params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_POSITION_V1_URL + '/singlePosition', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_all_positions(self, productType, marginCoin=None):
        """
        Obtain all position information of the user.
        Get All Position: https://bitgetlimited.github.io/apidoc/en/mix/#get-all-position

        :param productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
        :type productType: str
        :param marginCoin: Margin currency (Must be capitalized)
        :type marginCoin: str
        :return:
        """
        params = {}
        if productType:
            params["productType"] = productType
            if marginCoin is not None:
                params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_POSITION_V1_URL + '/allPosition', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_accountBill(self, symbol, marginCoin, startTime, endTime, lastEndId='', pageSize=20, next=False):
        """
        Get Account Bill: https://bitgetlimited.github.io/apidoc/en/mix/#get-account-bill
        Limit rule: 10/sec (uid)
        Required: symbol, marginCoin, startTime, endTime
        :return:
        """
        params = {}
        if symbol and marginCoin and startTime and endTime:
            params['symbol'] = symbol
            params['marginCoin'] = marginCoin
            params['startTime'] = startTime
            params['endTime'] = endTime
            params['lastEndId'] = lastEndId
            params['pageSize'] = pageSize
            params['next'] = next
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accountBill', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_accountBusinessBill(self, productType, startTime, endTime, lastEndId='', pageSize=20, next=False):
        """
        Get Business Account Bill: https://bitgetlimited.github.io/apidoc/en/mix/#get-business-account-bill
        Limit rule: 5/sec (uid)
        Required: productType, startTime, endTime
        :return:
        """
        params = {}
        if productType and startTime and endTime:
            params['productType'] = productType
            params['startTime'] = startTime
            params['endTime'] = endTime
            params['lastEndId'] = lastEndId
            params['pageSize'] = pageSize
            params['next'] = next
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accountBusinessBill', params)
        else:
            logger.error("pls check args")
            return False

    """ --- MIX-tradeApi """

    def mix_place_order(self, symbol, marginCoin, size, side, orderType,
                        price='', clientOrderId=None, reduceOnly=False,
                        timeInForceValue='normal', presetTakeProfitPrice='', presetStopLossPrice=''):
        """
        place an order: https://bitgetlimited.github.io/apidoc/en/mix/#place-order
        Limit rule: 10 times/1s (uid)
        Trader Limit rule: 1 times/1s (uid)

        Required: symbol, marginCoin, size, price, side, orderType.

        price: Mandatory in case of price limit
        marginCoin: Deposit currency
        size: It is quantity when the price is limited. The market price is the limit. The sales is the quantity
        side：open_long open_short close_long close_short
        orderType: limit(fixed price)  market(market price)
        timeInForceValue: normal(Ordinary price limit order)   postOnly(It is only a maker. The market price is not allowed to use this)  ioc(Close immediately and cancel the remaining)  fok(Complete transaction or immediate cancellation)
        presetTakeProfitPrice: Default stop profit price
        presetStopLossPrice：Preset stop loss price
        :return:
        """
        params = {}
        if symbol and marginCoin and side and orderType and size:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["price"] = price
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["reduceOnly"] = reduceOnly
            params["timeInForceValue"] = timeInForceValue
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/placeOrder', params)
        else:
            logger.error("pls check args")
            return False

    def mix_reversal(self, symbol, marginCoin, side, orderType,
                     size=None, clientOrderId=None, timeInForceValue='normal', reverse=False):
        """
        Reversal: https://bitgetlimited.github.io/apidoc/en/mix/#reversal
        Limit rule: 10 times/1s (uid), counted together with placeOrder
        Reversal share the same interface with Place order.

        Required: symbol, marginCoin, side, orderType

        :return:
        """
        params = {}
        if symbol and marginCoin and side and orderType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["side"] = side
            params["orderType"] = orderType
            if size is not None:
                params["size"] = size
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            params["timeInForceValue"] = timeInForceValue
            params["reverse"] = reverse
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/placeOrder', params)
        else:
            logger.error("pls check args")
            return False

    def mix_batch_orders(self, symbol, marginCoin, orderDataList):
        """
        Batch Order: https://bitgetlimited.github.io/apidoc/en/mix/#batch-order
        Limit rule: 10 times/1s (uid)
        Trader Limit rule: 1 times/1s (uid)
        Required: symbol, marginCoin, orderDataList
        """
        params = {}
        if symbol and marginCoin and orderDataList:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderDataList"] = orderDataList
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/batch-orders', params)
        else:
            logger.error("pls check args")
            return False

    def mix_cancel_order(self, symbol, marginCoin, orderId='', clientOid=''):
        """
        Cancel Order: https://bitgetlimited.github.io/apidoc/en/mix/#cancel-order
        Limit rule: 10 times/1s (uid)
        Required: symbol, marginCoin, orderId or clientOid
        - Order Id, int64 in string format, 'orderId' or 'clientOid' must have one
        - Client Order Id, 'orderId' or 'clientOid' must have one
        """
        params = {}
        if symbol and marginCoin and (orderId != '' or clientOid != ''):
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            if orderId != '':
                params["orderId"] = orderId
            elif clientOid != '':
                params["clientOid"] = clientOid

            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-order', params)
        else:
            logger.error("pls check args")
            return False

    def mix_batch_cancel_orders(self, symbol, marginCoin, orderId: list = None, clientOid: list = None):
        """ Batch Cancel Order
        https://bitgetlimited.github.io/apidoc/en/mix/#batch-cancel-order
        Limit rule: 10 times/1s (uid)
        Required: symbol, marginCoin, orderIds or clientOids
        - Order Id list, int64 in string format, 'orderIds' or 'clientOids' must have one
        - Client Order Id list, 'orderIds' or 'clientOids' must have one
        """
        params = {}
        if symbol and marginCoin and orderIds:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            if orderId is not None:
                params["orderId"] = orderId
            elif clientOid is not None:
                params["clientOid"] = clientOid
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-batch-orders', params)
        else:
            logger.error("pls check args")
            return False

    def mix_cancel_all_orders(self, productType, marginCoin):
        """ Cancel All Order
        https://bitgetlimited.github.io/apidoc/en/mix/#cancel-all-order
        Limit rule: 10 times/1s (uid)

        Required: productType, marginCoin
        """
        params = {}
        if productType and marginCoin:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-all-orders', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_open_order(self, symbol):
        """
        Get the current order: https://bitgetlimited.github.io/apidoc/en/mix/#get-open-order
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/current', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_all_open_orders(self, productType, marginCoin=None):
        """
        Get All Open Order:::https://bitgetlimited.github.io/apidoc/en/mix/#get-all-open-order
        Required: productType
        :return:
        """
        params = {}
        if productType:
            params["productType"] = productType
            if marginCoin is not None:
                params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/marginCoinCurrent', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_history_orders(self, symbol, startTime, endTime, pageSize, lastEndId='', isPre=False):
        """
        Get History Orders: https://bitgetlimited.github.io/apidoc/en/mix/#get-history-orders

        Limit rule: 20 times/2s (uid)

        Required: symbol, startTime, endTime, pageSize

        :param symbol: Symbol Id (Must be capitalized)
        :type symbol: str
        :param startTime: Start time, milliseconds
        :type startTime: str
        :param endTime: End time, milliseconds
        :type endTime: str
        :param pageSize: page Size
        :type pageSize: str
        :param lastEndId: last end Id of last query
        :type lastEndId: str
        :param isPre: true: order by order Id asc; default false
        :type isPre: Boolean
        :return:
        """
        params = {}
        if symbol and startTime and endTime and pageSize:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/history', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_productType_history_orders(self, productType, startTime, endTime, pageSize, lastEndId='', isPre=False):
        """
        Get ProductType History Orders: https://bitgetlimited.github.io/apidoc/en/mix/#get-producttype-history-orders

        Limit rule: 5/1s (uid)

        Required: productType, startTime, endTime, pageSize

        :param productType
        :type productType: str
        :param startTime: Start time, milliseconds
        :type startTime: str
        :param endTime: End time, milliseconds
        :type endTime: str
        :param pageSize: page Size
        :type pageSize: str
        :param lastEndId: last end Id of last query
        :type lastEndId: str
        :param isPre: true: order by order Id asc; default false
        :type isPre: Boolean
        :return:
        """
        params = {}
        if productType and startTime and endTime and pageSize:
            params["productType"] = productType
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/historyProductType', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_order_details(self, symbol, orderId=None, clientOrderId=None):
        """
        Get Order Details: https://bitgetlimited.github.io/apidoc/en/mix/#get-order-details
        Limit rule: 20 times/2s (uid)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            if orderId is not None:
                params["orderId"] = orderId
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/detail', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_order_fill_detail(self, symbol, orderId=None, startTime=None, endTime=None, lastEndId=None):
        """
        Get Order fill detail: https://bitgetlimited.github.io/apidoc/en/mix/#get-order-fill-detail
        Limit rule: 20 times/2s (uid)
        Required: symbol
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            if orderId is not None:
                params["orderId"] = orderId
            if startTime is not None:
                params["startTime"] = startTime
            if endTime is not None:
                params["endTime"] = endTime
            if lastEndId is not None:
                params["lastEndId"] = lastEndId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/fills', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_productType_order_fill_detail(self, productType, startTime=None, endTime=None, lastEndId=None):
        """
        Get ProductType Order fill detail: https://bitgetlimited.github.io/apidoc/en/mix/#get-producttype-order-fill-detail
        Limit rule: 10 times/1s (uid)
        Required: productType
        :return:
        """
        params = {}
        if productType:
            params["productType"] = productType
            if startTime is not None:
                params["startTime"] = startTime
            if endTime is not None:
                params["endTime"] = endTime
            if lastEndId is not None:
                params["lastEndId"] = lastEndId
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/allFills', params)
        else:
            logger.error("pls check args")
            return False

    def mix_place_plan_order(self, symbol, marginCoin, size, side, orderType, triggerPrice, triggerType
                             , executePrice=None, clientOrderId=None, presetTakeProfitPrice=None, presetStopLossPrice=None, reduceOnly=False):
        """
        Place Plan order: https://bitgetlimited.github.io/apidoc/en/mix/#place-plan-order
        Limit rule: 10 times/1s (uid)

        Required: symbol, marginCoin, size, side, orderType, triggerPrice, triggerType
        :return:
        """
        params = {}
        if symbol and marginCoin and side and size and orderType and triggerPrice and triggerType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["triggerPrice"] = triggerPrice
            params["triggerType"] = triggerType
            params["reduceOnly"] = reduceOnly
            if executePrice is not None:
                params["executePrice"] = executePrice
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            if presetTakeProfitPrice is not None:
                params["presetTakeProfitPrice"] = presetTakeProfitPrice
            if presetStopLossPrice is not None:
                params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placePlan', params)
        else:
            logger.error("pls check args")
            return False

    def mix_modify_plan_order(self, symbol, marginCoin, orderId, orderType, triggerPrice, triggerType
                              , executePrice=None):
        """
        Modify Plan Order: https://bitgetlimited.github.io/apidoc/en/mix/#modify-plan-order
        Limit rule: 10 times/1s (uid)

        Required: symbol, marginCoin, orderId, orderType, triggerPrice, triggerType
        :return:
        """
        params = {}
        if symbol and marginCoin and orderId and orderType and triggerPrice and triggerType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            params["orderType"] = orderType
            params["triggerPrice"] = triggerPrice
            params["triggerType"] = triggerType
            if executePrice is not None:
                params["executePrice"] = executePrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyPlan', params)
        else:
            logger.error("pls check args")
            return False

    def mix_modify_plan_order_tpsl(self, symbol, marginCoin, orderId
                                   , presetTakeProfitPrice=None, presetStopLossPrice=None):
        """
        Modify Plan Order TPSL: https://bitgetlimited.github.io/apidoc/en/mix/#modify-plan-order-tpsl
        Limit rule: 10 times/1s (uid)

        Required: symbol, marginCoin, orderId
        :return:
        """
        params = {}
        if symbol and marginCoin and orderId:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            if presetTakeProfitPrice is not None:
                params["presetTakeProfitPrice"] = presetTakeProfitPrice
            if presetStopLossPrice is not None:
                params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyPlanPreset', params)
        else:
            logger.error("pls check args")
            return False

    def mix_place_stop_order(self, symbol, marginCoin, triggerPrice, planType, holdSide,
                             triggerType='fill_price', size=None, rangeRate=None):
        """
        Place Stop Order: https://bitgetlimited.github.io/apidoc/en/mix/#place-stop-order
        Limit rule: 10 times/1s (uid)

        Required: symbol, marginCoin, triggerPrice, planType, holdSide
        :return:
        """
        params = {}
        if symbol and marginCoin and planType and holdSide and triggerPrice:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["holdSide"] = holdSide
            params["triggerPrice"] = triggerPrice
            params["triggerType"] = triggerType
            if size is not None:
                params["size"] = size
            if rangeRate is not None:
                params["rangeRate"] = rangeRate
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placeTPSL', params)
        else:
            logger.error("pls check args")
            return False

    def mix_place_trailing_stop_order(self, symbol, marginCoin, triggerPrice, side,
                                      triggerType=None, size=None, rangeRate=None):
        """
        Place Trailing Stop Order: https://bitgetlimited.github.io/apidoc/en/mix/#place-trailing-stop-order
        Limit rule: 10 times/1s (uid)

        Required: symbol, marginCoin, triggerPrice, side
        :return:
        """
        params = {}
        if symbol and marginCoin and side and triggerPrice:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["side"] = side
            params["triggerPrice"] = triggerPrice
            if triggerType is not None:
                params["triggerType"] = triggerType
            if size is not None:
                params["size"] = size
            if rangeRate is not None:
                params["rangeRate"] = rangeRate
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placeTrailStop', params)
        else:
            logger.error("pls check args")
            return False

    def mix_place_PositionsTPSL(self, symbol, marginCoin, planType, triggerPrice, triggerType, holdSide=None):
        """
        Place Position TPSL: https://bitgetlimited.github.io/apidoc/en/mix/#place-position-tpsl
        Limit rule: 10 times/1s (uid)
        When the position take profit and stop loss are triggered, the full amount of the position will be entrusted at the market price by default.
        Required: marginCoin, symbol, planType, triggerPrice, triggerType
        triggertype: fill_price, market_price
        """
        params = {}
        if marginCoin and symbol and planType and triggerPrice and triggerType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["planType"] = planType
            params["triggerPrice"] = triggerPrice
            params["triggerType"] = triggerType
            if holdSide is not None:
                params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placePositionsTPSL', params)
        else:
            logger.error("pls check args")
            return False

    def mix_modify_stop_order(self, symbol, marginCoin, orderId, triggerPrice, planType):
        """
        Modify Stop Order: https://bitgetlimited.github.io/apidoc/en/mix/#modify-stop-order
        Limit rule: 10 times/1s (uid)
        Required: symbol, marginCoin, orderId, triggerPrice, planType
        """
        params = {}
        if symbol and marginCoin and orderId and triggerPrice and planType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            params["triggerPrice"] = triggerPrice
            params["planType"] = planType
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/modifyTPSLPlan', params)
        else:
            logger.error("pls check args")
            return False

    def mix_cancel_plan_order(self, symbol, marginCoin, orderId, planType):
        """
        Cancel Plan Order (TPSL): https://bitgetlimited.github.io/apidoc/en/mix/#cancel-plan-order-tpsl
        Required: symbol, marginCoin, orderId, planType
        Limit rule: 10 times/1s (uid)
        """
        params = {}
        if symbol and marginCoin and orderId and planType:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            params["planType"] = planType
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/cancelPlan', params)
        else:
            logger.error("pls check args")
            return False

    def mix_cancel_all_trigger_orders(self, productType, planType):
        """
        Cancel All trigger Order (TPSL): https://bitgetlimited.github.io/apidoc/en/mix/#cancel-all-trigger-order-tpsl
        Required: productType, planType
        Limit rule: 10 times/1s (uid)
        """
        params = {}
        if productType and planType:
            params["productType"] = productType
            params["planType"] = planType
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/cancelAllPlan', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_plan_order_tpsl(self, symbol=None, productType=None, isPlan=None):
        """
        Get Plan Order (TPSL) List:https://bitgetlimited.github.io/apidoc/en/mix/#get-plan-order-tpsl-list
        can get orders without symbol parameter.
        But either or both of symbol and productType have to be set as request parameters.
        Required: symbol or productType
        isPlan: plan/profit_loss
        Limit rule: 10 times/1s (uid)
        :return:
        """
        params = {}
        if symbol is not None or productType is not None:
            if symbol is not None:
                params["symbol"] = symbol
            if productType is not None:
                params["productType"] = productType
            if isPlan is not None:
                params["isPlan"] = isPlan
            return self._request_with_params(GET, MIX_PLAN_V1_URL + '/currentPlan', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_history_plan_orders(self, symbol, startTime, endTime, pageSize=100, lastEndId=None, isPre=False, isPlan=None):
        """
        Get History Plan Orders (TPSL): https://bitgetlimited.github.io/apidoc/en/mix/#get-history-plan-orders-tpsl
        Limit rule: 10 times/1s (uid)
        Required: symbol, startTime, endTime
        :return:
        """
        params = {}
        if symbol and startTime and endTime:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["isPre"] = isPre
            if lastEndId is not None:
                params["lastEndId"] = lastEndId
            if isPlan is not None:
                params["isPlan"] = isPlan
            return self._request_with_params(GET, MIX_PLAN_V1_URL + '/historyPlan', params)
        else:
            logger.error("pls check args")
            return False

    """ --- MIX-CopyTradeApi """

    # https://bitgetlimited.github.io/apidoc/en/mix/#copytrade
    # CopyTrade (cp)
    def mix_get_cp_open_order(self, symbol, productType, pageSize=20, pageNo=1):
        """
        Get Trader Open order: https://bitgetlimited.github.io/apidoc/en/mix/#get-trader-open-order
        Limit rule: 10 times/1s (uid)
        Required: symbol, productType
        :return:
        """
        params = {}
        if symbol and productType:
            params["symbol"] = symbol
            params["productType"] = productType
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/currentTrack', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_cp_follower_open_orders(self, symbol, productType, pageSize=20, pageNo=1):
        """
        Get Follower Open Orders: https://bitgetlimited.github.io/apidoc/en/mix/#get-follower-open-orders
        Limit rule: 10 times/1s (uid)
        Required: symbol, productType
        :return:
        """
        params = {}
        if symbol and productType:
            params["symbol"] = symbol
            params["productType"] = productType
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/followerOrder', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_cp_follower_history_orders(self, startTime, endTime, pageSize=20, pageNo=1):
        """
        Get Follower History Orders: https://bitgetlimited.github.io/apidoc/en/mix/#get-follower-history-orders
        Limit rule: 10 times/1s (uid)
        Required: startTime, endTime
        :return:
        """
        params = {}
        if startTime and endTime:
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/followerHistoryOrders', params)
        else:
            logger.error("pls check args")
            return False

    def mix_cp_close_position(self, symbol, trackingNo):
        """
        Trader Close Position: https://bitgetlimited.github.io/apidoc/en/mix/#trader-close-position
        Limit rule: 10 times/1s (uid)
        Required: symbol, trackingNo
        :return:
        """
        params = {}
        if symbol and trackingNo:
            params["symbol"] = symbol
            params["trackingNo"] = trackingNo
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/closeTrackOrder', params)
        else:
            logger.error("pls check args")
            return False

    def mix_cp_modify_tpsl(self, symbol, trackingNo, stopProfitPrice=None, stopLossPrice=None):
        """
        Trader Modify TPSL: https://bitgetlimited.github.io/apidoc/en/mix/#trader-modify-tpsl
        Limit rule: 10 times/1s (uid)
        Required: symbol, trackingNo

        :stopProfitPrice set to null means to disable/cancel TP

        :stopLossPrice set to null means to disable/cancel SL

        :return:
        """
        params = {}
        if symbol and trackingNo:
            params["symbol"] = symbol
            params["trackingNo"] = trackingNo
            if stopProfitPrice is not None:
                params["stopProfitPrice"] = stopProfitPrice
            if stopLossPrice is not None:
                params["stopLossPrice"] = stopLossPrice
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/modifyTPSL', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_cp_history_orders(self, startTime, endTime, pageSize=20, pageNo=1):
        """
        Get Traders History Orders: https://bitgetlimited.github.io/apidoc/en/mix/#get-traders-history-orders
        Limit rule: 10 times/1s (uid)
        Required: startTime, endTime
        :return:
        """
        params = {}
        if startTime and endTime:
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/historyTrack', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_cp_profit_summary(self):
        """
        Get Trader Profit Summary: https://bitgetlimited.github.io/apidoc/en/mix/#get-trader-profit-summary
        Limit rule 20 times/1s (uid)
        Required: None
        :return:
        """
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/summary')

    def mix_get_cp_profit_settle_margin_coin(self):
        """
        Get Trader History Profit Summary (according to settlement currency):
        https://bitgetlimited.github.io/apidoc/en/mix/#get-trader-history-profit-summary-according-to-settlement-currency
        Limit rule 20 times/1s (uid)
        Summary of traders' profit sharing (by settlement currency)
        :return:
        """
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/profitSettleTokenIdGroup')

    def mix_get_cp_profit_date_group(self, pageSize=20, pageNo=1):
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#get-trader-history-profit-summary-according-to-settlement-currency-and-date
        Limit rule 20 times/1s (uid)
        Summary of traders' profit sharing (by date)
        :return:
        """
        params = {'pageSize': pageSize, 'pageNo': pageNo}
        return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateGroupList', params)

    def mix_get_cp_profit_date_detail(self, marginCoin, date, pageSize=20, pageNo=1):
        """
        Get Trader History Profit Detail
        https://bitgetlimited.github.io/apidoc/en/mix/#get-trader-history-profit-detail
        Limit rule 20 times/1s (uid)
        Historical profit distribution details of traders
        :return:
        """
        params = {}
        if marginCoin and date and pageSize and pageNo:
            params["marginCoin"] = marginCoin
            params["date"] = date
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/profitDateList', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_cp_wait_profit_detail(self, pageSize=20, pageNo=1):
        """
        Get Trader Profits Details
        https://bitgetlimited.github.io/apidoc/en/mix/#get-trader-profits-details
        Limit rule 20 times/1s (uid)
        Details of traders to be distributed
        :return:
        """
        params = {}
        if pageSize and pageNo:
            params["pageSize"] = pageSize
            params["pageNo"] = pageNo
            return self._request_with_params(GET, MIX_TRACE_V1_URL + '/waitProfitDateList', params)
        else:
            logger.error("pls check args")
            return False

    def mix_get_cp_symbols(self):
        """
        Get CopyTrade Symbols
        https://bitgetlimited.github.io/apidoc/en/mix/#get-copytrade-symbols
        Limit rule 20 times/1s (uid)
        :return:
        """
        return self._request_without_params(GET, MIX_TRACE_V1_URL + '/traderSymbols')

    def mix_cp_change_symbol(self, symbol, operation):
        """
        Trader Change CopyTrade symbol: https://bitgetlimited.github.io/apidoc/en/mix/#trader-change-copytrade-symbol
        Limit rule: 10 times/1s (uid)
        Required: symbol, operation
        :return:
        """
        params = {}
        if symbol and operation:
            params["symbol"] = symbol
            params["operation"] = operation
            return self._request_with_params(POST, MIX_TRACE_V1_URL + '/setUpCopySymbols', params)
        else:
            logger.error("pls check args")
            return False

    """ Bitget-Spot-Endpoints"""
    """ Spot-PublicApi"""

    def spot_get_server_time(self):
        """
        Get Server Time: https://bitgetlimited.github.io/apidoc/en/spot/#get-server-time
        Rate Limit: 20 times/1s (IP)
        :return:
        """
        return self._request_without_params(GET, SPOT_PUBLIC_V1_URL + '/time')

    def spot_get_coin_list(self):
        """
        Get Coin List: https://bitgetlimited.github.io/apidoc/en/spot/#get-coin-list
        Rate Limit: 3 times/1s (IP)
        :return:
        """
        return self._request_without_params(GET, SPOT_PUBLIC_V1_URL + '/currencies')

    def spot_get_symbols(self):
        """
        Get Symbols: https://bitgetlimited.github.io/apidoc/en/spot/#get-symbols
        Rate Limit: 20 times/1s (IP)
        :return:
        """
        return self._request_without_params(GET, SPOT_PUBLIC_V1_URL + '/products')

    def spot_get_symbol(self, symbol):
        """
        Get Single Symbol: https://bitgetlimited.github.io/apidoc/en/spot/#get-single-symbol
        Rate Limit: 20 times/1s (IP)
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, SPOT_PUBLIC_V1_URL + '/product', params)
        else:
            logger.error("pls check args")
            return False

    """ Spot-MarketApi"""

    def spot_get_tickers(self):
        """
        Get All Tickers: https://bitgetlimited.github.io/apidoc/en/spot/#get-all-tickers

        Rate Limit: 20 times/1s (IP)

        Get all transaction pair ticker information
        :return:
        """
        return self._request_without_params(GET, SPOT_MARKET_V1_URL + '/tickers')

    def spot_get_ticker(self, symbol):
        """
        Get Single Ticker: https://bitgetlimited.github.io/apidoc/en/spot/#get-single-ticker

        Rate Limit: 20 times/1s (IP)

        Get ticker information according to the currency pair
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/ticker', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_market_trades(self, symbol, limit=100):
        """
        Get Market Trades: https://bitgetlimited.github.io/apidoc/en/spot/#get-market-trades

        Rate Limit: 20 times/1s (IP)

        Get real-time transaction
        :return:
        """
        params = {}
        if symbol and limit:
            params["symbol"] = symbol
            params["limit"] = limit
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/fills', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_candle_data(self, symbol, period, after='', before='', limit=100):
        """
        Get Candle Data: https://bitgetlimited.github.io/apidoc/en/spot/#get-candle-data

        Rate Limit: 20 times/1s (IP)

        Obtain K line information

        period: 1min, 5min, 15min, 30min, 1h,4h,12h, 1day, 1week

        after: Time after, milliseconds

        before: Time before, milliseconds
        :return:
        """
        params = {}
        if symbol and period:
            params["symbol"] = symbol
            params["period"] = period
            params["after"] = after
            params["before"] = before
            params["limit"] = limit
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/candles', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_depth(self, symbol, limit='150', type='step0'):
        """
        Get Depth: https://bitgetlimited.github.io/apidoc/en/spot/#get-depth

        Rate Limit: 20 times/1s (IP)

        Get depth data

        Depth Merge Type

        type: step0(default) step1 step2 step3 step4 step5
        :return:
        """
        params = {}
        if symbol and limit and type:
            params["symbol"] = symbol
            params["limit"] = limit
            params["type"] = type
            return self._request_with_params(GET, SPOT_MARKET_V1_URL + '/depth', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_vip_fee_rate(self):
        """
        VIP fee rate: https://bitgetlimited.github.io/apidoc/en/spot/#vip-fee-rate
        Limit rule: 10 times/1s (IP)
        Required: None
        :return:
        """
        return self._request_without_params(GET, SPOT_MARKET_V1_URL + '/spot-vip-level')

    """ Spot-WalletApi"""

    def spot_transfer(self, fromType, toType, amount, coin, clientOrderId=None):
        """
        Transfer: https://bitgetlimited.github.io/apidoc/en/spot/#transfer

        fromType： spot, mix_usdt, mix_usd

        toType: spot, mix_usdt, mix_usd

        amount: transfer amount

        coin: crypto currency
        :return:
        """
        params = {}
        if fromType and toType and amount and coin:
            params["fromType"] = fromType
            params["toType"] = toType
            params["amount"] = amount
            params["coin"] = coin
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            return self._request_with_params(POST, SPOT_WALLET_V1_URL + '/transfer', params)
        else:
            logger.error("pls check args")
            return False

    def spot_sub_transfer(self, fromType, toType, amount, coin, clientOrderId, fromUserId, toUserId):
        """
        Sub Transfer: https://bitgetlimited.github.io/apidoc/en/spot/#sub-transfer
        Rate Limit：2/sec (uid)

        :return:
        """
        params = {}
        if fromType and toType and amount and coin and fromUserId and toUserId:
            params["fromType"] = fromType
            params["toType"] = toType
            params["amount"] = amount
            params["coin"] = coin
            params["clientOid"] = clientOrderId
            params["fromUserId"] = fromUserId
            params["toUserId"] = toUserId
            return self._request_with_params(POST, SPOT_WALLET_V1_URL + '/subTransfer', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_depositAddress(self, coin, chain):
        """
        Get Coin Address: https://bitgetlimited.github.io/apidoc/en/spot/#get-coin-address

        Rate Limit：5/sec (uid)

        GET deposit address

        coin： btc usdt

        chain: trc20  erc20

        :return:
        """
        params = {}
        if coin and chain:
            params["coin"] = coin
            params["chain"] = chain
            return self._request_with_params(GET, SPOT_WALLET_V1_URL + '/deposit-address', params)
        else:
            logger.error("pls check args")
            return False

    def spot_withdrawal(self, coin, address, chain, amount, remark='', clientOrderId=None, tag=None):
        """
        Withdraw: https://bitgetlimited.github.io/apidoc/en/spot/#withdraw

        Just withdraw coins on the chain

        Rate Limit:5/sec (Uid)

        :return:
        """
        params = {}
        if coin:
            params["coin"] = coin
            params["address"] = address
            params["chain"] = chain
            params["amount"] = amount
            params["remark"] = remark
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            if tag is not None:
                params["tag"] = tag
            return self._request_with_params(POST, SPOT_WALLET_V1_URL + '/withdrawal', params)
        else:
            logger.error("pls check args")
            return False

    def spot_withdrawal_inner(self, coin, toUid, amount, clientOrderId=None):
        """
        Inner Withdraw: https://bitgetlimited.github.io/apidoc/en/spot/#inner-withdraw

        Internal withdrawal means that both users are on the Bitget platform

        Withdraw money directly in the form of uid, without going on the chain, no need to pass the address

        Rate Limit: 5/sec (Uid)

        :return:
        """
        params = {}
        if coin and toUid and amount:
            params["coin"] = coin
            params["amount"] = amount
            params["toUid"] = toUid
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            return self._request_with_params(POST, SPOT_WALLET_V1_URL + '/withdrawal-inner', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_withdrawalList(self, coin, startTime, endTime, pageSize=20, pageNo=1):
        """
        Get Withdraw list: https://bitgetlimited.github.io/apidoc/en/spot/#get-withdraw-list

        Rate Limit：20/1s (Uid)

        :return:
        """
        params = {}
        if coin and startTime and endTime:
            params["coin"] = coin
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageNo"] = pageNo
            params["pageSize"] = pageSize
            return self._request_with_params(GET, SPOT_WALLET_V1_URL + '/withdrawal-list', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_depositList(self, coin, startTime, endTime, pageSize=20, pageNo=1):
        """
        Get Deposit List: https://bitgetlimited.github.io/apidoc/en/spot/#get-deposit-list

        Rate Limit：20/1s (Uid)

        :return:
        """
        params = {}
        if coin and startTime and endTime:
            params["coin"] = coin
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageNo"] = pageNo
            params["pageSize"] = pageSize
            return self._request_with_params(GET, SPOT_WALLET_V1_URL + '/deposit-list', params)
        else:
            logger.error("pls check args")
            return False

    """ Spot-AccountApi"""

    def spot_get_ApiKeyInfo(self):
        """
        Get ApiKey Info: https://bitgetlimited.github.io/apidoc/en/spot/#get-apikey-info

        Rate Limit: 1/sec (Uid)

        :return:
        """
        return self._request_without_params(GET, SPOT_ACCOUNT_V1_URL + '/getInfo')

    def spot_get_account_assets(self, coin=None):
        """
        Get Account Assets: https://bitgetlimited.github.io/apidoc/en/spot/#get-account-assets

        Rate Limit: 10 times/1s (uid)

        Obtain all asset currency information of the user

        :return:
        """
        params = {}
        if coin is not None:
            params["coin"] = coin
        return self._request_with_params(GET, SPOT_ACCOUNT_V1_URL + '/assets', params)

    def spot_get_sub_account_assets(self):
        """
        Get sub Account Spot Assets: https://bitgetlimited.github.io/apidoc/en/spot/#get-sub-account-spot-assets

        Rate Limit: 1 times/10s (uid)

        ***Warning*** This endpoint's worked on POST, but the Request Example is GET.

        Why this endpoint name is "Get sub Account Spot Assets", but it's used POST ?!!

        :return:
        """
        if self.verbose:
            logger.warning("***Warning*** This endpoint's worked on POST")
        return self._request_without_params(POST, SPOT_ACCOUNT_V1_URL + '/sub-account-spot-assets')

    def spot_get_bills(self, coinId='', groupType='', bizType='', after='', before='', limit=100):
        """
        Get Bills: https://bitgetlimited.github.io/apidoc/en/spot/#get-bills

        Rate Limit: 10 times/1s (uid)

        Obtain all asset currency information of the user

        groupType: Deposit, withdraw, transaction, transfer, other

        bizType：Dispose, withdraw, buy, sell, transfer in, transfer out

        after: Pass in billId, the data before this billId

        before: Incoming billId data after this billId

        :return:
        """
        params = {}

        if coinId:
            params["coinId"] = coinId
        if groupType:
            params["groupType"] = groupType
        if bizType:
            params["bizType"] = bizType
        if after:
            params["after"] = after
        if before:
            params["before"] = before

        params["limit"] = limit
        return self._request_with_params(POST, SPOT_ACCOUNT_V1_URL + '/bills', params)

    def spot_get_transfer_list(self, coinId='', fromType='', after='', before='', limit=100):
        """
        Get Transfer List: https://bitgetlimited.github.io/apidoc/en/spot/#get-transfer-list

        Rate Limit: 20 times/1s (uid)

        query transfer records

        fromType: exchange(spot)   USD_MIX(coin future) USDT_MIX(usdt future)

        :return:
        """
        params = {}

        if coinId:
            params["coinId"] = coinId
        if fromType:
            params["fromType"] = fromType
        if after:
            params["after"] = after
        if before:
            params["before"] = before

        params["limit"] = limit
        return self._request_with_params(GET, SPOT_ACCOUNT_V1_URL + '/transferRecords', params)

    """ Spot-TradeApi"""

    def spot_place_order(self, symbol, quantity, side, orderType, force, price='', clientOrderId=None):
        """
        Place order: https://bitgetlimited.github.io/apidoc/en/spot/#place-order

        Rate Limit: 10/sec (uid)

        price: Mandatory in case of price limit

        quantity: It is quantity when the price is limited. The market price is the limit. The sales is the quantity

        side：buy sell

        orderType: limit(fixed price)  market(market price)

        force:normal(Ordinary price limit order)   postOnly(It is only a maker.

        The market price is not allowed to use this)  ioc(Close immediately and cancel the remaining)  fok(Complete transaction or immediate cancellation)

        :return:
        """
        params = {}

        if symbol and quantity and side and orderType and force:
            params["symbol"] = symbol
            params["price"] = price
            params["quantity"] = quantity
            params["side"] = side
            params["orderType"] = orderType
            params["force"] = force
            if clientOrderId is not None:
                params["clientOrderId"] = clientOrderId
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/orders', params)
        else:
            logger.error("pls check args")
            return False

    def spot_place_batch_orders(self, symbol, orderList):
        """
        Batch order: https://bitgetlimited.github.io/apidoc/en/spot/#batch-order

        Rate Limit: 5/sec (uid)

        Place orders in batches

        :return:
        """

        if symbol and orderList:
            params = {'symbol': symbol, 'orderList': orderList}
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + "/batch-orders", params)
        else:
            logger.error("pls check args")
            return False

    def spot_cance_order(self, symbol, orderId):
        """
        Cancel order: https://bitgetlimited.github.io/apidoc/en/spot/#cancel-order

        Rate Limit: 10 times/sec (uid)

        :return:
        """
        params = {}

        if symbol and orderId:
            params["symbol"] = symbol
            params["orderId"] = orderId
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/cancel-order', params)
        else:
            logger.error("pls check args")
            return False

    def spot_cancel_batch_orders(self, symbol, orderIds):
        """
        Cancel order in batch (single instruments): https://bitgetlimited.github.io/apidoc/en/spot/#cancel-order-in-batch-single-instruments

        Rate Limit: 5 times/1s (uid)

        Batch cancellation

        :return:
        """

        if symbol and orderIds:
            params = {'symbol': symbol, 'orderIds': orderIds}
            return self._request_with_params(POST, SPOT_ORDER_V1_URL + "/cancel-batch-orders", params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_order_details(self, symbol, orderId, clientOrderId=None):
        """
        Get order details:https://bitgetlimited.github.io/apidoc/en/spot/#get-order-details

        Rate Limit: 20 times/sec(uid)

        User could query cancelled/filled order details within 24 hours; Noted that after 24 hours should query via history interface.
        :return:
        """
        params = {}
        if symbol and orderId:
            params["symbol"] = symbol
            params["orderId"] = orderId
            if clientOrderId is not None:
                params["clientOrderId"] = clientOrderId

            if self.verbose:
                logger.warning("***Warning*** This endpoint's worked on POST")

            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/orderInfo', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_open_orders(self, symbol=''):
        """
        Get order List: https://bitgetlimited.github.io/apidoc/en/spot/#get-order-list

        Rate Limit: 20 times/sec(uid)

        :return:
        """
        params = {"symbol": symbol}
        if self.verbose:
            logger.warning("***Warning*** This endpoint's worked on POST")

        return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/open-orders', params)

    def spot_get_order_history(self, symbol, after='', before='', limit=100):
        """
        Get order history: https://bitgetlimited.github.io/apidoc/en/spot/#get-order-history

        Rate Limit: 20 times/sec(uid)

        Get Historical Delegation
        after: The orderId is passed in. The data before the orderId desc

        before: Pass in the data after the orderId asc

        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["after"] = after
            params["before"] = before
            params["limit"] = limit
            if self.verbose:
                logger.warning("***Warning*** This endpoint's worked on POST")

            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/history', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_transaction_details(self, symbol='', orderId='', after='', before='', limit=100):
        """
        Get transaction details: https://bitgetlimited.github.io/apidoc/en/spot/#get-transaction-details

        Rate Limit: 20 times/sec(uid)

        Obtain transaction details

        after: Only the data before the fillId can be passed in

        before: Only data passing in the fillId after this fillId is supported
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["orderId"] = orderId
            params["after"] = after
            params["before"] = before
            params["limit"] = limit
            if self.verbose:
                logger.warning("***Warning*** This endpoint's worked on POST")

            return self._request_with_params(POST, SPOT_ORDER_V1_URL + '/fills', params)
        else:
            logger.error("pls check args")
            return False

    def spot_place_plan_order(self, symbol, side, triggerPrice, size, triggerType, orderType,
                              executePrice=None, timeInForceValue=None, clientOrderId=None):
        """
        Place plan order: https://bitgetlimited.github.io/apidoc/en/spot/#place-plan-order

        Rate Limit: 20 times/sec (uid)

        Required: symbol, side, triggerPrice, size, triggerType, orderType

        :return:
        """
        params = {}

        if symbol and side and triggerPrice and size and triggerType:
            params["symbol"] = symbol
            params["side"] = side
            params["triggerPrice"] = triggerPrice
            params["size"] = size
            params["triggerType"] = triggerType
            params["orderType"] = orderType
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            if executePrice is not None:
                params["executePrice"] = executePrice
            if timeInForceValue is not None:
                params["timeInForceValue"] = timeInForceValue
            return self._request_with_params(POST, SPOT_PLAN_V1_URL + '/placePlan', params)
        else:
            logger.error("pls check args")
            return False

    def spot_modify_plan_order(self, orderId, orderType, triggerPrice,
                               size=None, executePrice=None):
        """
        Modify Plan Order: https://bitgetlimited.github.io/apidoc/en/spot/#modify-plan-order
        Limit rule: 20 times/sec (uid)

        Required: orderId, orderType, triggerPrice
        :return:
        """
        params = {}
        if orderId and orderType and triggerPrice:
            params["orderId"] = orderId
            params["orderType"] = orderType
            params["triggerPrice"] = triggerPrice
            if executePrice is not None:
                params["executePrice"] = executePrice
            if size is not None:
                params["size"] = size
            return self._request_with_params(POST, SPOT_PLAN_V1_URL + '/modifyPlan', params)
        else:
            logger.error("pls check args")
            return False

    def spot_cancel_plan_order(self, orderId):
        """
        Cancel plan order: https://bitgetlimited.github.io/apidoc/en/spot/#cancel-plan-order
        Required: orderId
        Limit rule: 20 times/sec (uid)
        """
        params = {}
        if orderId:
            params["orderId"] = orderId
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/cancelPlan', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_plan_orders(self, symbol, pageSize=20, lastEndId=''):
        """
        Get current plan orders: https://bitgetlimited.github.io/apidoc/en/spot/#get-current-plan-orders

        Rate Limit: 20 times/sec(uid)

        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            if self.verbose:
                logger.warning("***Warning*** This endpoint's worked on POST")

            return self._request_with_params(POST, SPOT_PLAN_V1_URL + '/currentPlan', params)
        else:
            logger.error("pls check args")
            return False

    def spot_get_history_plan_orders(self, symbol, startTime, endTime, pageSize=20, lastEndId=''):
        """
        Get history plan orders: https://bitgetlimited.github.io/apidoc/en/spot/#get-history-plan-orders

        Rate Limit: 20 times/sec(uid)

        :return:
        """
        params = {}
        if symbol and startTime and endTime:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            if self.verbose:
                logger.warning("***Warning*** This endpoint's worked on POST")

            return self._request_with_params(POST, SPOT_PLAN_V1_URL + '/historyPlan', params)
        else:
            logger.error("pls check args")
            return False

    """ Broker-Sub-API-Interface"""

    def broker_sub_create_api(self, subUid, passphrase, remark, ip, perm):
        """ Create Sub ApiKey (Only Broker) : https://bitgetlimited.github.io/apidoc/en/broker/#create-sub-apikey-only-broker

        Limit rule：10/sec (uid)

        broker create sub apikey

        :return:
        """
        params = {}
        if subUid and passphrase and perm:
            params["subUid"] = subUid
            params["passphrase"] = passphrase
            params["remark"] = remark
            params["ip"] = ip
            params["perm"] = perm
            return self._request_with_params(POST, BROKER_MANAGE_V1_URL + '/sub-api-create', params)
        else:
            logger.error("pls check args")
            return False

    def broker_get_sub_api_list(self, subUid):
        """ Get Sub ApiKey List : https://bitgetlimited.github.io/apidoc/en/broker/#get-sub-apikey-list

        Limit rule：10/sec (uid)


        :return:
        """
        params = {}
        if subUid:
            params["subUid"] = subUid
            return self._request_with_params(GET, BROKER_MANAGE_V1_URL + '/sub-api-list', params)
        else:
            logger.error("pls check args")
            return False

    def broker_sub_modify_api(self, subUid, apikey, remark=None, ip=None, perm=None):
        """ Modify Sub ApiKey (Only Broker) : https://bitgetlimited.github.io/apidoc/en/broker/#modify-sub-apikey-only-broker

        Limit rule：10/sec (uid)

        :return:
        """
        params = {}
        if subUid and apikey:
            params["subUid"] = subUid
            params["apikey"] = apikey
            if remark is not None:
                params["remark"] = remark
            if ip is not None:
                params["ip"] = ip
            if perm is not None:
                params["perm"] = perm
            return self._request_with_params(POST, BROKER_MANAGE_V1_URL + '/sub-api-modify', params)
        else:
            logger.error("pls check args")
            return False

    """ Broker-Sub-Account-Interface"""

    def broker_get_info(self):
        """ Get Broker Info
        https://bitgetlimited.github.io/apidoc/en/broker/#get-broker-info """
        return self._request_without_params(GET, BROKER_ACCOUNT_V1_URL + '/info')

    def broker_sub_create(self, subName, remark=None):
        """ Create Sub Account
        https://bitgetlimited.github.io/apidoc/en/broker/#create-sub-account """
        params = {}
        if subName:
            params["subName"] = subName
            if remark is not None:
                params["remark"] = remark
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-create', params)
        else:
            logger.error("pls check args")
            return False

    def broker_get_sub_list(self, pageSize=10, lastEndId=None, status=None):
        """ Get Sub List
        https://bitgetlimited.github.io/apidoc/en/broker/#get-sub-list """
        params = {}
        if pageSize:
            params["pageSize"] = pageSize
            if lastEndId is not None:
                params["lastEndId"] = lastEndId
            if status is not None:
                params["status"] = status
            return self._request_with_params(GET, BROKER_ACCOUNT_V1_URL + '/sub-list', params)
        else:
            logger.error("pls check args")
            return False

    def broker_sub_modify_account(self, subUid, perm, status):
        """ Modify Sub Account
        https://bitgetlimited.github.io/apidoc/en/broker/#modify-sub-account """
        params = {}
        if subUid and perm and status:
            params["subUid"] = subUid
            params["perm"] = perm
            params["status"] = status
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-modify', params)
        else:
            logger.error("pls check args")
            return False

    def broker_sub_modify_email(self, subUid, subEmail):
        """ Modify Sub Email
        https://bitgetlimited.github.io/apidoc/en/broker/#modify-sub-email """
        params = {}
        if subUid and subEmail:
            params["subUid"] = subUid
            params["subEmail"] = subEmail
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-modify-email', params)
        else:
            logger.error("pls check args")
            return False

    def broker_get_sub_email(self, subUid):
        """ GET Sub Email
        https://bitgetlimited.github.io/apidoc/en/broker/#get-sub-email """
        params = {}
        if subUid:
            params["subUid"] = subUid
            return self._request_with_params(GET, BROKER_ACCOUNT_V1_URL + '/sub-email', params)
        else:
            logger.error("pls check args")
            return False

    def broker_get_sub_spot_assets(self, subUid):
        """ Get Sub Spot Assets
        https://bitgetlimited.github.io/apidoc/en/broker/#get-sub-spot-assets """
        params = {}
        if subUid:
            params["subUid"] = subUid
            return self._request_with_params(GET, BROKER_ACCOUNT_V1_URL + '/sub-spot-assets', params)
        else:
            logger.error("pls check args")
            return False

    def broker_get_sub_future_assets(self, subUid, productType):
        """ Get Sub Future Assets
        https://bitgetlimited.github.io/apidoc/en/broker/#get-sub-future-assets """
        params = {}
        if subUid and productType:
            params["subUid"] = subUid
            params["productType"] = productType
            return self._request_with_params(GET, BROKER_ACCOUNT_V1_URL + '/sub-future-assets', params)
        else:
            logger.error("pls check args")
            return False

    def broker_get_sub_deposit_address(self, subUid, coin, chain=None):
        """ Get Sub Deposit Address (Only Broker)
        https://bitgetlimited.github.io/apidoc/en/broker/#get-sub-deposit-address-only-broker """
        params = {}
        if subUid and coin:
            params["subUid"] = subUid
            params["coin"] = coin
            if chain is not None:
                params["chain"] = chain
            if self.verbose:
                logger.warning("***Warning*** This endpoint's worked on POST")
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-address', params)
        else:
            logger.error("pls check args")
            return False

    def broker_sub_withdrawal(self, subUid, coin, address, chain, amount,
                              tag=None, clientOrderId=None, remark=None):
        """ Sub Withdrawal (Only Broker)
        https://bitgetlimited.github.io/apidoc/en/broker/#sub-withdrawal-only-broker """
        params = {}
        if subUid and coin and chain and address and amount:
            params["subUid"] = subUid
            params["coin"] = coin
            params["chain"] = chain
            params["address"] = address
            params["amount"] = amount
            if tag is not None:
                params["tag"] = tag
            if remark is not None:
                params["remark"] = remark
            if clientOrderId is not None:
                params["clientOid"] = clientOrderId
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-withdrawal', params)
        else:
            logger.error("pls check args")
            return False

    def broker_sub_auto_transfer(self, subUid, coin, toAccountType):
        """ Sub Deposit Auto Transfer (Only Broker)
        https://bitgetlimited.github.io/apidoc/en/broker/#sub-deposit-auto-transfer-only-broker """
        params = {}
        if subUid and coin and toAccountType:
            params["subUid"] = subUid
            params["coin"] = coin
            params["toAccountType"] = toAccountType
            return self._request_with_params(POST, BROKER_ACCOUNT_V1_URL + '/sub-auto-transfer', params)
        else:
            logger.error("pls check args")
            return False
