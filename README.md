# Mettalex -  World’s first DEX focused on token based commodities trading

[**Website** ](https://mettalex.com/)

Access the world’s first DEX focused on token based commodities trading using this SDK. Accessible 24/7 with tight trading spreads, low margin requirements and unique hedge instruments that ensure you don’t get liquidated prior to settlement dates.

## Prerequisites

This package is designed for python 3. While using pip, pip should be configured for python3.

## Installation

Mettalex for python can be installed directly from github using the following command:

```pip install -e git+https://github.com/fetchai/mettalex-sdk.git@master#egg=mettalex-sdk```

## Usage

##### Importing
```from mettalex import apiSDK```

##### Connecting to a network

Mettalex provides 3 networks for connecting to Metallex exchange, namely, ```'bsc-testnet'```, ```'kovan'``` and ```'bsc-mainnet'```. You will need to connect to one of these to be able to access Mettalex.
You will require your your ```key``` while connecting to any network. 
```Infura project ID``` and ```Infura API Secret``` are required only while connecting to ```kovan```.


    apiSDK.connect([network], [userkey], [infuraSecret ? Optional], [infuraProjectId ? Optional])

or pass credentials as a json file e.g. trade_sdk_creds.json

    {
      "kovan": {
        "infura": {
          "project_id": "...",
          "secret": "..."
        },
        "user": {
          "address": "0x...",
          "key": "14a..."
        }
      },
      "bsc-mainnet": {
        "user": {
          "address": "", 
          "key": ""
        }
      },
      "bsc-testnet": {
        "user": {
          "address": "", 
          "key": ""
        }
      }
    }

then connect with 

    apiSDK.connect('kovan', filename=os.path.expanduser('~/trader_sdk_creds.json'))

##### Getting Commodities

```apiSDK.getCommodities()```
This function returns a pandas DataFrame with details of all the commodities in the connected network. Use this function typically while getting the list of all commoodities availabe on a network.

##### Creating a commodity instance to trade

```commodity = apiSDK.Commodity([commodity symbol or commodity ID])```
A Commodity instance can be created using the commodity symbol. This initializes a class instance of the particular commodity. An instance of a commodity needs to be created to be able to execute trades and getting expected prices.
We can get commodity symbols available by calling ```getCommodities()```
 
##### Expected trading prices
 
Two functions ```ask``` and ```bid``` can be used to retrieve trading prices. These functions can be called on commodity instances created, taking two arguments of token and amount to be traded.

    commodity.ask(token, amount) - amount of coin required to buy token amount

    commodity.bid(token, amount) - amount of coin received from sell token amount

Token is provided as a string and can be either `"long"` or `"short"`.  
Amount is provided by default as a `float` using token amounts taking token decimals
into account.  
If the `unitless` parameter is set to True the amount values are in ```int```

##### Trading
Trading in a commodity is quite simple. We have to call trade function on a commodity instance providing in token, out token and the amount we want to trade.
```In token``` and ```Out Token``` can take ```"long"```,```"short"```, or ```"coin"``` as values.  
Amount is provided as a `float or` `int` as for `bid` and `ask` methods.
```commodity.trade([In Token], [Out Token], [amount In], [minimum amount Out])```


## Example
Setup and imports in ipython console

    %load_ext autoreload
    %autoreload 2
    import pandas as pd
    import os
    from mettalex import apiSDK
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', None)

Connect to blockchain and list commodities

    apiSDK.connect('kovan', filename=os.path.expanduser('~/trader_sdk_creds.json'))
    commodities = apiSDK.getCommodities('kovan', output='dataframe')
    Connected to network ID 42
    commodities.groupby('category')['id'].count()
    Out[6]: 
    category
    Agricultural    1
    Crypto          3
    Ferrous         5
    Forex           1
    Indices         1
    Industrial      5
    Other           1
    Spread          5
    Test QA         2
    Name: id, dtype: int64
    commodities.loc[commodities.category == 'Spread', ['id', 'commodity_symbol', 'commodity_name']]
    Out[7]: 
         id commodity_symbol            commodity_name
    5   303         LINKBAND          Link Band Spread
    12  286           BTCETH   Bitcoin Ethereum Spread
    17  299          BTCTSLA      Bitcoin Tesla Spread
    18  307        SDEFISCEX         sDEFI sCEX spread
    19  211          SRSCSPR  Steel Rebar Scrap Spread

Connect to specific market and trade

    commodity = apiSDK.Commodity('BTCTSLA')
    connection established sucessfully
    commodity
    Out[11]: 
    BTCTSLA: Bitcoin Tesla Spread
    Mettalex Vault: 0x37eeDc79D22980Bd60652751072ac252C300959a
      Prices - Floor: 50.0 Spot: 79.2 Cap: 100.0
      Coin : 0xe551960F80e5f855bB75d36016Ca92c981314b3E  568937.305831
      Short: 0x6aE1854843e5AD57e103E68C6E1A455530336750  11374.34611
      Long : 0x924D2bf052538F4DF696450214A827D0575127b6  11374.34611
    Mettalex Liquidity Pool: 0x071826Eb1FD5bCC1a2219CC8F9ae99a1A6eC9AFE
      Coin : 0xe551960F80e5f855bB75d36016Ca92c981314b3E  {'y_vault': 330.505877, 'vault_controller': 0.0, 'strategy': 0.0, 'balancer': 594117.125268}
      Short: 0x6aE1854843e5AD57e103E68C6E1A455530336750  {'y_vault': 0.0, 'vault_controller': 0.0, 'strategy': 0.0, 'balancer': 7776.0527}
      Long : 0x924D2bf052538F4DF696450214A827D0575127b6  {'y_vault': 0.0, 'vault_controller': 0.0, 'strategy': 0.0, 'balancer': 9659.39263}
    Short spot price: 23.953781  Long spot price : 27.070647
    commodity.getUserBalance()
    Out[12]: (35752.557059, 0.0, 0.0)
    commodity.ask('long', 100)
    Out[13]: 2727.088497
    commodity.ask('long', 10)
    Out[14]: 270.887126
    commodity.bid('long', 10)
    Out[15]: 259.778631
    commodity.bid('long', 100)
    Out[16]: 2580.950892
    commodity.trade('coin', 'long', 3000)
    swap started
    txn approved
    Swapped 3000.000 coin to 109.926 long
    Out[17]: (3000.0, 109.92576)
    commodity.getUserBalance()
    Out[18]: (32752.557059, 0.0, 109.92576)