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

```apiSDK.connect([network], [userkey], [infuraSecret ? Optional], [infuraProjectId ? Optional])```

##### Getting Commodities

```apiSDK.getCommodities()```
This function returns an array with symbols of all the commodities in the connected network. Use this function typically while getting the list of all commoodities availabe on a network.
A typical response for for this function is
```['AL', 'BTC', 'FTSE', ... ]```

##### Creating a commodity instance to trade

```commodity = apiSDK.Commodity([commodity symbol])```
A Commodity instance can be created using the commodity symbol. This initializes a class instance of the particular commodity. An instance of a commodity needs to be created to be able to execute trades and getting expected prices.
We can get commodity symbols available by calling ```getCommodities()```
 
##### Expected trading prices
 
Two functions ```getExpectedInAmount``` and ```getExpectedOutAmount``` can be used to retrive trading prices. These functions can be called on commodity instances created, taking two arguments of token and amount to be traded.
```commodity.getExpectedInAmount([token], [amount])```
Token is provided as a string and can be either ```"long"``` or ```"short"```. Amount is provided as an ```int```.
This function returns the expected value in ```int```

##### Trading
Trading in a commodity is quite simple. We have to call trade function on a commodity instance providing in token, out token and the amount we want to trade.
```In token``` and ```Out Token``` can take ```"long"```,```"short"```, or ```"coin"``` as values. Amount is to be provided as an ```int```.
```commodity.trade([In Token], [Out Token], [amount])```
