Getting Started
===============

Installation
------------

``python-bitget`` is available on `PYPI <https://pypi.python.org/pypi/python-bitget/>`_.
Install with ``pip``:

.. code:: bash

    pip install python-bitget

Register on bitget
-------------------

Firstly register an account with bitget `save 10% on all of your trade fee, and can get rewards up to $5005 <https://partner.bitget.com/bg/e55g05831674816745836>`_.

Generate an API Key
-------------------

To use signed account methods you are required to `create an API Key  <https://www.bitget.com/en/support/articles/360038968251-API%20Creation%20Guide>`_.

Initialise the client
---------------------

Pass your API Key and Secret

.. code:: python

    api_key = "your-api-key"
    api_secret = "your-secret-key"
    api_passphrase = "your-api-passphrase"
    client = Client(api_key, api_secret, api_passphrase, use_server_time=False)


Making API Calls
----------------

Every method supports the passing of arbitrary parameters via keyword matching those in the
`bitget API documentation <https://bitgetlimited.github.io/apidoc/en/mix/#welcome>`_.
These keyword arguments will be sent directly to the relevant endpoint.

Each API method returns a dictionary of the JSON response as per the
`bitget API documentation <https://bitgetlimited.github.io/apidoc/en/mix/#welcome>`_.
The docstring of each method in the code references the endpoint it implements.

The bitget API documentation references a `timestamp` parameter, this is generated for you where required.

API Endpoints are rate limited by bitget, it's diff on per endpoint, ask them if you require more.



API Rate Limit
--------------

The Sub Account and Main Account have their own UIDs.
Because the Limit Rules are based on each UID, every sub account has the same limit rate as main account.
It's not necessary to worry about the limit rate for main account when you are trading with sub accounts Or their API Keys.
And the limit rate is same for every user including VIP account. You may contact your Bitget business manager for more information.

Some calls have a higher weight than others especially if a call returns information about all symbols.
Read the `official bitget documentation <https://bitgetlimited.github.io/apidoc/en/mix/#welcome>`_ for specific information.


Here are examples to access these

restAPI example

.. code:: python

    from bitget import Client

    api_key = "your-api-key"
    api_secret = "your-secret-key"
    api_passphrase = "your-api-passphrase"

    client = Client(api_key, api_secret, passphrase=api_passphrase)
    result = client.mix_get_accounts(productType='UMCBL')
    print(result)

websocketAPI example

.. code:: python

    from pybitget.stream import BitgetWsClient, SubscribeReq, handel_error

    from pybitget.enums import *
    from pybitget import logger


    def on_message(message):
        logger.info(message)


    api_key = "your-api-key"
    api_secret = "your-secret-key"
    api_passphrase = "your-api-passphrase"

    if __name__ == '__main__':
        # Un-auth subscribe
        # client = BitgetWsClient() \
        #     .error_listener(handel_error) \
        #     .build()

        # Auth subscribe
        client = BitgetWsClient(api_key=api_key,
                                api_secret=api_secret,
                                passphrase=api_passphrase,
                                verbose=True) \
            .error_listener(handel_error) \
            .build()

        # multi subscribe  - Public Channels
        channels = [SubscribeReq("mc", "ticker", "BTCUSD"), SubscribeReq("SP", "candle1W", "BTCUSDT")]
        client.subscribe(channels, on_message)

        # single subscribe -     # multi subscribe  Public Channels
        # channels = [SubscribeReq("mc", "ticker", "BTCUSD")]
        # client.subscribe(channels, on_message)

        # single subscribe - Order Channel - Private Channels
        channels = [SubscribeReq(WS_CHANNEL_INSTTYPE, WS_PRIVATE_ORDERS_CHANNEL, WS_CHANNEL_INSTID)]
        client.subscribe(channels, on_message)
