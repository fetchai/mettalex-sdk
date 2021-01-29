# Mettalex -  World’s first DEX focused on token based commodities trading

[**Website** ](https://mettalex.com/)

Access the world’s first DEX focused on token based commodities trading using this SDK. Accessible 24/7 with tight trading spreads, low margin requirements and unique hedge instruments that ensure you don’t get liquidated prior to settlement dates.

## Installation

Mettalex for python can be installed directly from github using the following command:

```pip install -e git+https://github.com/fetchai/mettalex-sdk.git@master#egg=mettalex-sdk```

## Usage

##### Importing
```from mettalex import apiSDK```

##### Connecting to a network

Mettalex provides 3 networks for connecting to Metallex exchange, namely, ```'bsc-testnet'```, ```'kovan'``` and ```'bsc-mainnet'```. You will need to connect to one of these to be able to access Mettalex.
You will require your your ```key``` to connect and also your ```Infura project ID``` and ```Infura API Secret``` in case you are connecting to ```kovan```.

```apiSDK.connect([network], [userkey], [infuraSecret], [infuraProjectId])```

##### Getting Commodities

```apiSDK.getCommodities()```
This function returns an array with all the commodities on platform. A typical response for for this function is
```['AL', 'BTC', 'FTSE', ... ]```

##### Creating a commodity to trade

```commodity = apiSDK.Commodity([commodity symbol])```
 Commodity can be created using the commodity symbol. This initializes a classs instance of the perticular commodity. We can get commodity symbols available by calling ```getCommodities()```
 
##### Expected trading prices
 
Two functions ```getExpectedInAmount``` and ```getExpectedOutAmount``` can be used to retrive trading prices. These functions can be called on commodities, taking two arguments of token and amount to be traded.
```commodity.getExpectedInAmount("short", 50000)```
This function returns the expected value in ```int```

##### Trading
Trading in a commodity is quite simple. We have to call trade function on a commodity providing in token, out token and the amount we want to trade.

```commodity.trade([In Token], [Out Token], [amount])```