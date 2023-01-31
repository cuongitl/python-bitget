WebSocketAPI
===============

Overview
------------

This is a wrapper around the Bitget API as described on Bitget, so please read the `official documents  <https://bitgetlimited.github.io/apidoc/en/mix/#overview>`_ for more details.

Example connect
------------

Pass your API Key and Secret

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
