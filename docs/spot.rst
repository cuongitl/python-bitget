Spot
===============

Public
------------

`Get Server Time <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_server_time()

`Get Coin List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_coin_list()

`Get Symbols <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_symbols()

`Get Single Symbol <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_symbol()

Public
------------

`Get Single Ticker <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_ticker(self, symbol)

`Get All Tickers <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_tickers()

`Get Market Trades <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.pot_get_market_trades(self, symbol, limit=100)

`Get Candle Data <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_candle_data(self, symbol, period, after='', before='', limit=100)

`Get Depth <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_depth(self, symbol, limit='150', type='step0')

Wallet
------------

`Transfer <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_transfer(self, fromType, toType, amount, coin, clientOrderId=None)

`Sub Transfer <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_sub_transfer(self, fromType, toType, amount, coin, clientOrderId, fromUserId, toUserId)

`Get Coin Address <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_depositAddress(self, coin, chain)

`Withdraw <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_withdrawal(self, coin, address, chain, amount, remark='', clientOrderId=None, tag=None)

`Inner Withdraw <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_withdrawal_inner(self, coin, toUid, amount, clientOrderId=None)

`Get Withdraw list <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_withdrawalList(self, coin, startTime, endTime, pageSize=20, pageNo=1)

`Get Deposit List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_depositList(self, coin, startTime, endTime, pageSize=20, pageNo=1)

Account
------------

`Get ApiKey Info <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_ApiKeyInfo()

`Get Account Assets <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_account_assets(self, coin=None)

`Get sub Account Spot Assets <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_sub_account_assets()

`Get Bills <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_bills(self, coinId='', groupType='', bizType='', after='', before='', limit=100)

`Get Transfer List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_transfer_list(self, coinId='', fromType='', after='', before='', limit=100)


Trade
------------

`Place order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_place_order(self, symbol, quantity, side, orderType, force, price='', clientOrderId=None)

`Batch order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_place_batch_orders(self, symbol, orderList)

`Cancel order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_cance_order(self, symbol, orderId)

`Cancel order in batch (single instruments) <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_cancel_batch_orders(self, symbol, orderIds)

`Get order details <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_order_details(self, symbol, orderId, clientOrderId=None)

`Get order List <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_open_orders(self, symbol='')

`Get order history <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_order_history(self, symbol, after='', before='', limit=100)

`Get transaction details <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_transaction_details(self, symbol='', orderId='', after='', before='', limit=100)

`Place plan order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_place_plan_order(self, symbol, side, triggerPrice, size, triggerType, orderType,
                              executePrice=None, timeInForceValue=None, clientOrderId=None)

`Modify plan order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_modify_plan_order(self, orderId, orderType, triggerPrice,
                               size=None, executePrice=None)

`Cancel plan order <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_cancel_plan_order(self, orderId)

`Get current plan orders <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_plan_orders(self, symbol, pageSize=20, lastEndId='')

`Get history plan orders <#>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    data = client.spot_get_history_plan_orders(self, symbol, startTime, endTime, pageSize=20, lastEndId=''):
