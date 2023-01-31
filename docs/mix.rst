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
