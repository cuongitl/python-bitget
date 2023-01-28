import requests
import json
from pybitget.enums import *
from pybitget import utils
from pybitget import exceptions
from pybitget import logger


class Client(object):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False):

        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time

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

    """ --- MarkettApi """

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
            logger.debug("pls check args")
            return False

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
            logger.debug("pls check args")
            return False

    """ --- AccountApi """

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
            logger.debug("pls check args")
            return False

    def mix_get_accounts(self, productType):
        """
        Get account information list: https://bitgetlimited.github.io/apidoc/en/mix/#get-account-list
        productType: Umcbl (USDT professional contract) dmcbl (mixed contract) sumcbl (USDT professional contract simulation disk) sdmcbl (mixed contract simulation disk)
        :return:
        """
        params = {}
        if productType:
            params['productType'] = productType
            return self._request_with_params(GET, MIX_ACCOUNT_V1_URL + '/accounts', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_get_leverage(self, symbol):
        """
        Docs: https://bitgetlimited.github.io/apidoc/en/mix/#get-symbol-leverage
        Limit rule: 20/sec (IP)
        Required: symbol.

        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_MARKET_V1_URL + '/symbol-leverage', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_adjust_leverage(self, symbol, marginCoin, leverage, holdSide=''):
        """
        Docs: https://bitgetlimited.github.io/apidoc/en/mix/#change-leverage
        Limit rule: 5 times/1s (uid)
        The leverage could set to different number in fixed margin mode(holdSide is required)
        Required: symbol, marginCoin, leverage

        """
        params = {}
        if symbol and marginCoin and leverage:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["leverage"] = leverage
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setLeverage', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_adjust_margintype(self, symbol, marginCoin, marginMode):
        """
        Docs: https://bitgetlimited.github.io/apidoc/en/mix/#change-margin-mode
        Limit rule: 5 times/1s (uid)
        Required: symbol, marginCoin, marginMode
        - marginMode: fixed, crossed
        """
        params = {}
        if symbol and marginCoin and marginMode:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["marginMode"] = marginMode

            return self._request_with_params(POST, MIX_ACCOUNT_V1_URL + '/setMarginMode', params)
        else:
            logger.debug("pls check args")
            return False

    """ --- PositionApi """
    '''
    Obtain the user's single position information
    :return:
    '''

    def mix_get_single_position(self, symbol, marginCoin=None):
        """
            Obtain the user's single position information.
            Docs: https://bitgetlimited.github.io/apidoc/en/mix/#get-symbol-position

            :param symbol: Name of symbol pair e.g BNBBTC
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
            logger.debug("pls check args")
            return False

    def mix_get_all_positions(self, productType, marginCoin=None):
        """
        Obtain all position information of the user. Docs: https://bitgetlimited.github.io/apidoc/en/mix/#get-all-position

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
            logger.debug("pls check args")
            return False

    def mix_get_current_orders(self, symbol):
        """
        Get the current order.
        Docs: https://bitgetlimited.github.io/apidoc/en/mix/#get-open-order
        :return:
        """
        params = {}
        if symbol:
            params["symbol"] = symbol
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/current', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_get_all_open_orders(self, productType, marginCoin=None):
        """
        Get All Open Order:::https://bitgetlimited.github.io/apidoc/en/mix/#get-all-open-order

        :return:
        """
        params = {}
        if productType:
            params["productType"] = productType
            if marginCoin:
                params["marginCoin"] = marginCoin
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/marginCoinCurrent', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_get_current_plan(self, symbol=None, productType=None, isPlan=None):
        """
        Get Plan Order (TPSL) List:https://bitgetlimited.github.io/apidoc/en/mix/#get-plan-order-tpsl-list
        can get orders without symbol parameter.
        But either or both of symbol and productType have to be set as request parameters.
        Required: symbol or productType
        isPlan: plan/profit_loss
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
            logger.debug("pls check args")
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
            logger.debug("pls check args")
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
        if symbol:
            params["symbol"] = symbol
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/history', params)
        else:
            logger.debug("pls check args")
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
        if productType:
            params["productType"] = productType
            params["startTime"] = startTime
            params["endTime"] = endTime
            params["pageSize"] = pageSize
            params["lastEndId"] = lastEndId
            params["isPre"] = isPre
            return self._request_with_params(GET, MIX_ORDER_V1_URL + '/historyProductType', params)
        else:
            logger.debug("pls check args")
            return False

    # OrderApi - Trade
    def mix_place_order(self, symbol, marginCoin, size, side, orderType,
                        price='', clientOrderId='', reduceOnly=False,
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
        if symbol and marginCoin and side and orderType and marginCoin:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["price"] = price
            params["size"] = size
            params["side"] = side
            params["orderType"] = orderType
            params["reduceOnly"] = reduceOnly
            params["timeInForceValue"] = timeInForceValue
            params["clientOid"] = clientOrderId
            params["presetTakeProfitPrice"] = presetTakeProfitPrice
            params["presetStopLossPrice"] = presetStopLossPrice
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/placeOrder', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_cancel_all_orders(self, productType, marginCoin):
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#cancel-all-order
        Limit rule: 10 times/1s (uid)

        Required: productType, marginCoin
        """
        params = {}
        if productType and orderId:
            params["productType"] = productType
            params["marginCoin"] = marginCoin
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-all-orders', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_cancel_order(self, symbol, marginCoin, orderId):
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#cancel-order
        Limit rule: 10 times/1s (uid)
        Required: symbol, marginCoin, orderId
        """
        params = {}
        if symbol and marginCoin and orderId:
            params["symbol"] = symbol
            params["marginCoin"] = marginCoin
            params["orderId"] = orderId
            return self._request_with_params(POST, MIX_ORDER_V1_URL + '/cancel-order', params)
        else:
            logger.debug("pls check args")
            return False

    def mix_cancel_plan_order(self, symbol, marginCoin, orderId, planType):
        """
        https://bitgetlimited.github.io/apidoc/en/mix/#cancel-plan-order-tpsl
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
            logger.debug("pls check args")
            return False

    # PlanApi - Trade

    def mix_place_PositionsTPSL(self, symbol, marginCoin, planType, triggerPrice, triggerType, holdSide=''):
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
            params["holdSide"] = holdSide
            return self._request_with_params(POST, MIX_PLAN_V1_URL + '/placePositionsTPSL', params)
        else:
            logger.debug("pls check args")
            return False
