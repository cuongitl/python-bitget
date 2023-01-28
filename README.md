# Python bitget API Library


[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/cuongitl/python-bitget/-/blob/main/LICENSE)
[![python-bitget Version](https://img.shields.io/pypi/v/python-bitget?logo=pypi)](https://pypi.org/project/python-bitget/)
[![python-bitget Python Versions](https://img.shields.io/pypi/pyversions/python-bitget?logo=pypi)](https://pypi.org/project/python-bitget/)
[![python-bitget Downloads Per Day](https://img.shields.io/pypi/dd/python-bitget?logo=pypi)](https://pypi.org/project/python-bitget/)
[![python-bitget Downloads Per Week](https://img.shields.io/pypi/dw/python-bitget?logo=pypi)](https://pypi.org/project/python-bitget/)
[![python-bitget Downloads Per Month](https://img.shields.io/pypi/dm/python-bitget?logo=pypi)](https://pypi.org/project/python-bitget/)

[bitget](https://www.bitget.com/en/referral/register?from=referral&clacCode=6EKP94LE) is a cryptocurrency derivatives exchange.

This is a wrapper around the Bitget API as described on Bitget, including all features the API provides using clear and readable objects, both for the REST  as the websocket API.

 
I am in no way affiliated with Bitget, use at your own risk.

**If you think something is broken, something is missing or have any questions, please open an [Issue](https://github.com/cuongitl/python-bitget/issues)**

# Get Started and Documentation
If you're new to Bitget, use the following link to [save 10% on all of your trade fees, and can get rewards up to $5005.](https://www.bitget.com/en/referral/register?from=referral&clacCode=6EKP94LE)
* [Register an account with Bitget.](https://partner.bitget.com/bg/e55g05831674816745836)
* [Generate an API Key and assign relevant permissions.](https://www.bitget.com/en/support/articles/360038968251-API%20Creation%20Guide)
* [Bitget API docs](https://bitgetlimited.github.io/apidoc/en/mix/#welcome)
  * [Example Bitget rest API](https://github.com/cuongitl/python-bitget/blob/main/example_rest_api.py)
  * [Example Bitget websocket API](https://github.com/cuongitl/python-bitget/blob/main/example_websocket_api.py)

# Install
    pip install python-bitget
# Usage

> Change your API KEY and your SECRET KEY.
### Restful Api Sample Code 

```python
from pybitget import Client

api_key = "your-api-key"
api_secret = "your-secret-key"
api_passphrase = "your-api-passphrase"

client = Client(api_key, api_secret, passphrase=api_passphrase)
result = client.mix_get_accounts(productType='UMCBL')
print(result)

```
### Websocket Sample Code 

```python
from pybitget.stream import BitgetWsClient, SubscribeReq, handel_error

from pybitget.enums import *
from pybitget import logger

api_key = "your-api-key"
api_secret = "your-secret-key"
api_passphrase = "your-api-passphrase"

def on_message(message):
    logger.info(message)


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
channels = [SubscribeReq("mc", "ticker", "BTCUSD")]
client.subscribe(channels, on_message)

# single subscribe - Order Channel - Private Channels
channels = [SubscribeReq(WS_CHANNEL_INSTTYPE, WS_PRIVATE_ORDERS_CHANNEL, WS_CHANNEL_INSTID)]
client.subscribe(channels, on_message)
```

## Donate / Sponsor
I develop and maintain this package on my own for free in my spare time. 
Donations are greatly appreciated. If you prefer to donate any other currency please contact me.

* **BTC**:  `3LrqgdMbToh1mAD3sjhbv3oaEppXY7hkae`

* **BTC**:  `0x329a9F2b01aDA25F15eAE4C633d3bed8442c7BC6`  (BSC)

* **USDT**:  `0x329a9F2b01aDA25F15eAE4C633d3bed8442c7BC6`  (BSC)

* **BGB**:  `0x3ee4ca7cc911ad4e423dec2ae8f2846e9a6a0a77`  (ERC-20)

## Communities
* Telegram: [Python-bitget API](https://t.me/python_bitget)

## Release Notes
The release notes can be found
[here.](https://github.com/cuongitl/python-bitget/blob/master/release_notes.md)

## Contribution
* Fork this repository.
* Make pull requests with proper commit message.