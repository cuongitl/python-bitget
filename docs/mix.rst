FuturesⓂ(USDT/Coin)
===============

Market
------------

`Get All Symbols <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_symbols_info(productType)

`Get Depth <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_depth(symbol, limit=100)

`Get Single Symbol Ticker <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_single_symbol_ticker(symbol)

`Get All Symbol Ticker <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_all_symbol_ticker(productType)

`Get Fills <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    # Get recent trades.
    data = client.mix_get_fills(symbol, limit=100)

`Get Candle Data <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_candles(symbol, granularity, startTime, endTime)

`Get Symbol Index Price <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_symbol_index_price(symbol)

`Get Symbol Next Funding Time <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_symbol_next_funding(symbol)

`Get History Funding Rate <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_history_fund_rate(symbol, pageSize=20, pageNo=1, nextPage=False)

`Get Current Funding Rate <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_current_fund_rate(symbol)

`Get Open Interest <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_open_interest(symbol)

`Get Symbol Mark Price <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_market_price(symbol)

`Get Symbol Leverage <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_leverage(symbol)

Account
------------

`Get Single Account <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_account(symbol, marginCoin)

`Get Account List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_accounts(productType)

`Get sub Account Contract Assets <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_sub_account_contract_assets(productType)

`Get Open Count <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_open_count(symbol, marginCoin, openPrice, openAmount, leverage=20)

`Change Leverage <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_adjust_leverage(symbol, marginCoin, leverage, holdSide=None)

`Change Margin <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_adjust_margin(symbol, marginCoin, amount, holdSide=None)

`Change Margin Mode <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_adjust_margintype(symbol, marginCoin, marginMode)

`Change Hold Mode <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_adjust_hold_mode(productType, holdMode)

`Get Symbol Position <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_single_position(symbol, marginCoin=None)

`Get All Position <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_all_positions(productType, marginCoin=None)

`Get Account Bill <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_accountBill(symbol, marginCoin, startTime, endTime, lastEndId='', pageSize=20, next=False)

`Get Business Account Bill <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_accountBusinessBill(productType, startTime, endTime, lastEndId='', pageSize=20, next=False)

Trade
------------

`Place Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_place_order(symbol, marginCoin, size, side, orderType,
                        price='', clientOrderId=None, reduceOnly=False,
                        timeInForceValue='normal', presetTakeProfitPrice='', presetStopLossPrice='')

`Reversal <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_reversal(symbol, marginCoin, side, orderType,
                     size=None, clientOrderId=None, timeInForceValue='normal', reverse=False)

`Batch Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_batch_orders(symbol, marginCoin, orderDataList)

`Cancel Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_cancel_order(symbol, marginCoin, orderId)

`Batch Cancel Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_batch_cancel_orders(symbol, marginCoin, orderIds)

`Cancel All Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_cancel_all_orders(productType, marginCoin)

`Get Open Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_open_order(symbol)

`Get All Open Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_all_open_orders(productType, marginCoin=None)

`Get History Orders <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_history_orders(symbol, startTime, endTime, pageSize, lastEndId='', isPre=False)

`Get ProductType History Orders <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_productType_history_orders(productType, startTime, endTime, pageSize, lastEndId='', isPre=False)

`Get Order Details <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_order_details(symbol, orderId=None, clientOrderId=None)

`Get Order fill detail <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_order_fill_detail(symbol, orderId=None, startTime=None, endTime=None, lastEndId=None)

`Get ProductType Order fill detail <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_productType_order_fill_detail(productType, startTime=None, endTime=None, lastEndId=None)

`Place Plan order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_place_plan_order(symbol, marginCoin, size, side, orderType, triggerPrice, triggerType
                             , executePrice=None, clientOrderId=None, presetTakeProfitPrice=None, presetStopLossPrice=None, reduceOnly=False)

`Modify Plan Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_modify_plan_order(symbol, marginCoin, orderId, orderType, triggerPrice, triggerType
                              , executePrice=None)

`Modify Plan Order TPSL <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_modify_plan_order_tpsl(symbol, marginCoin, orderId
                                   , presetTakeProfitPrice=None, presetStopLossPrice=None)

`Place Stop Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_place_stop_order(symbol, marginCoin, triggerPrice, planType, holdSide,
                             triggerType='fill_price', size=None, rangeRate=None)

`Place Trailing Stop Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_place_trailing_stop_order(symbol, marginCoin, triggerPrice, side,
                                      triggerType=None, size=None, rangeRate=None)

`Place Position TPSL <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_place_PositionsTPSL(symbol, marginCoin, planType, triggerPrice, triggerType, holdSide=None)

`Modify Stop Order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_modify_stop_order(symbol, marginCoin, orderId, triggerPrice, planType)

`Cancel Plan Order (TPSL) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_cancel_plan_order(symbol, marginCoin, orderId, planType)

`Cancel All trigger Order (TPSL) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_cancel_all_trigger_orders(productType, planType)

`Get Plan Order (TPSL) List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_plan_order_tpsl(symbol=None, productType=None, isPlan=None)

`Get History Plan Orders (TPSL) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_history_plan_orders(symbol, startTime, endTime, pageSize=100, lastEndId=None, isPre=False, isPlan=None)

CopyTrade
------------

`Get Trader Open order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_open_order(symbol, productType, pageSize=20, pageNo=1)

`Get Follower Open Orders <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_follower_open_orders(symbol, productType, pageSize=20, pageNo=1)

`Trader Close Position <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_cp_close_position(symbol, trackingNo)

`Trader Modify TPSL <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_cp_modify_tpsl(symbol, trackingNo, stopProfitPrice=None, stopLossPrice=None)

`Get Traders History Orders <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_history_orders(startTime, endTime, pageSize=20, pageNo=1)

`Get Trader Profit Summary <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_profit_summary()

`Get Trader History Profit Summary (according to settlement currency) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_profit_settle_margin_coin()

`Get Trader History Profit Summary (according to settlement currency and date) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_profit_date_group(pageSize=20, pageNo=1)

`Get Trader History Profit Detail <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_profit_date_detail(marginCoin, date, pageSize=20, pageNo=1)

`Get Trader Profits Details <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_wait_profit_detail(pageSize=20, pageNo=1)

`Get CopyTrade Symbols <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_get_cp_symbols()

`Trader Change CopyTrade symbol <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.mix_cp_change_symbol(symbol, operation)
