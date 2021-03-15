import os
import json
import requests

from mettalex.abi import abi_coin, abi_position, abi_vault, abi_poolController

INNFURA_SECRET = ''
INNFURA_PROJECT_ID = ''
USER_KEY = ''
NETWORK_ID = ''
COMMODITY_LIST = []


def connectNetwork(network, account='admin'):
    if network == 'bsc-testnet':
        os.environ['WEB3_PROVIDER_URI'] = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
        os.environ['WEB3_CHAIN_ID'] = '97'

        from web3.middleware import construct_sign_and_send_raw_middleware
        from web3.middleware import geth_poa_middleware
        from web3.auto import w3

        admin = w3.eth.account.from_key(USER_KEY)
        w3.eth.defaultAccount = admin.address
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(admin))

    elif network == 'bsc-mainnet':
        os.environ['WEB3_PROVIDER_URI'] = 'https://bsc-dataseed.binance.org/'
        os.environ['WEB3_CHAIN_ID'] = '56'

        from web3.middleware import construct_sign_and_send_raw_middleware
        from web3.middleware import geth_poa_middleware
        from web3.auto import w3

        admin = w3.eth.account.from_key(USER_KEY)
        w3.eth.defaultAccount = admin.address
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(admin))

    elif network == 'kovan':
        os.environ['WEB3_INFURA_PROJECT_ID'] = INNFURA_PROJECT_ID
        os.environ['WEB3_INFURA_API_SECRET'] = INNFURA_SECRET

        from web3.middleware import construct_sign_and_send_raw_middleware
        from web3.auto.infura.kovan import w3

        admin = w3.eth.account.from_key(USER_KEY)
        w3.eth.defaultAccount = admin.address
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(admin))
    else:
        raise ValueError(f'Unknown network {network}')

    assert w3.isConnected()
    return w3, admin


def get_contracts(w3):
    contracts = {
        # 'BFactory': create_contract(w3, abi_BFactory),
        # 'BPool': create_contract(w3, abi_BPool),
        'Coin': create_contract(w3, abi_coin),
        'Long': create_contract(w3, abi_position),
        'Short': create_contract(w3, abi_position),
        'Vault': create_contract(w3, abi_vault),
        # 'YController': create_contract(w3, abi_yController),
        # 'YVault': create_contract(w3, abi_yVault),
        'PoolController': create_contract(w3, abi_poolController),
    }
    return contracts


def create_contract(w3, _abi):
    contract = w3.eth.contract(abi=_abi)
    return contract


def connect_contract(w3, contract_abi, address):
    """Connect to existing deployed contract

    :param w3:
    :param contract:
    :param address:
    :return:
    """
    deployed_contract = w3.eth.contract(
        address=address,
        abi=contract_abi
    )
    return deployed_contract


def connect_deployed(w3, contracts, tkn=""):
    for commodity in COMMODITY_LIST:
        if (commodity["commodity_symbol"] == tkn):
            cmdt = commodity
            break

    deployed_contracts = {}

    deployed_contracts["Short"] = connect_contract(w3, abi_position, cmdt["short_token_contract_address"])
    deployed_contracts["Long"] = connect_contract(w3, abi_position, cmdt["long_token_contract_address"])
    deployed_contracts["Coin"] = connect_contract(w3, abi_coin, get_coin(str(NETWORK_ID)))
    deployed_contracts["PoolController"] = connect_contract(w3, abi_poolController, cmdt["strategy_address"])
    deployed_contracts["Vault"] = connect_contract(w3, abi_vault, cmdt["mettalex_contract_address"])
    # deployed_contracts["BPool"] = connect_contract(w3, abi_BPool, cmdt["liquidity_pool_address"])

    return deployed_contracts


def get_network_id(w3):
    chain_id = w3.eth.chainId
    return chain_id


def get_coin(network_id):
    coin_address = {
        '97': '0xa5Ebc90a713908872f137f7e468c2d887a8A2869',
        '42': '0xe551960F80e5f855bB75d36016Ca92c981314b3E',
        '56': '0x6e71C530bAdEB04b95C64a8ca61fe0b946A94525'
    }[network_id]
    return coin_address


def swap(w3, strategy, tokenIn, amountIn, tokenOut, amountOut=1):
    # approve
    tx_hash = tokenIn.functions.approve(strategy.address, amountIn).transact(
        {'from': w3.eth.defaultAccount, 'gas': 1_000_000}
    )
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("txn approved")

    # swap
    MAX_UINT_VALUE = 2 ** 256 - 1

    tx_hash = strategy.functions.swapExactAmountIn(tokenIn.address, amountIn, tokenOut.address, amountOut,
                                                   MAX_UINT_VALUE).transact(
        {'from': w3.eth.defaultAccount, 'gas': 5_000_000}
    )
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    logs = strategy.events.LOG_SWAP.getLogs()
    if logs == ():
        print("TXN reverted, Check the reason on etherscan")
        print(tx_receipt)
    else:
        amount_out = logs[0]['args']['tokenAmountOut']
        print(
            f'Swap successful from {tokenIn.address} to {tokenOut.address} with received amount = {amount_out}')


def connect(network, userkey, infuraSecret='', infuraProjectId=''):
    global INNFURA_SECRET, INNFURA_PROJECT_ID, USER_KEY, NETWORK_ID, W3, CONTRACTS
    if (network == "kovan"):
        if (infuraSecret == '' and infuraProjectId == ''):
            raise Exception("Provide infura details to connect to kovan")

    INNFURA_SECRET = infuraSecret
    INNFURA_PROJECT_ID = infuraProjectId
    USER_KEY = userkey
    w3, admin = connectNetwork(network)
    NETWORK_ID = get_network_id(w3)
    print(NETWORK_ID)
    CONTRACTS = get_contracts(w3)
    W3 = w3


def getCommodities():
    global COMMODITY_LIST
    url = "https://storage.googleapis.com/mettalex-assets-stats/commodities_" + str(NETWORK_ID) + "_all.json"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    cmdts = []
    cmdts = json.loads(response.text)["data"]
    cmdts.sort(key=lambda s: s['version'])
    cmdts.reverse()
    COMMODITY_LIST = cmdts
    CommodityArr = []
    for cmdt in cmdts:
        if cmdt['commodity_symbol'] not in CommodityArr:
            CommodityArr.append(cmdt['commodity_symbol'])
    return CommodityArr


class Commodity:
    def __init__(self, symbol):
        self.cmdtFlag = 0
        for cmdt in getCommodities():
            if (symbol == cmdt):
                self.cmdtFlag = 1
                break
        if (self.cmdtFlag == 0):
            raise Exception("Not a valid commodity symbol")
        self.symbol = symbol
        self.w3 = W3
        self.contracts = CONTRACTS
        self.connect()

    def connect(self):
        self.deployed_contracts = connect_deployed(self.w3, self.contracts, self.symbol)
        self.coin = self.deployed_contracts['Coin']
        self.ltk = self.deployed_contracts['Long']
        self.stk = self.deployed_contracts['Short']
        self.strategy = self.deployed_contracts['PoolController']
        self.vault = self.deployed_contracts['Vault']
        print("connection established sucessfully")

    def switch(self, token):
        switcher = {
            "long": self.ltk,
            "short": self.stk,
            "coin": self.coin
        }
        return switcher.get(token, "--")

    def trade(self, tokenIn, tokenOut, amountIn, amountOut=1):
        if (self.vault.functions.isSettled().call() == True):
            raise Exception("Settled")
        intkn = self.switch(tokenIn)
        outtkn = self.switch(tokenOut)
        if (intkn == outtkn):
            raise Exception("In and out token can't be same")
        if (intkn == "--" or intkn == "--"):
            raise Exception("In token or out token not valid")
        print("swap started")
        swap(self.w3, self.strategy, intkn, amountIn, outtkn, amountOut)

    def getExpectedOutAmount(self, tokenIn, amount):
        if (tokenIn == "long" or tokenIn == "short"):
            intkn = self.switch(tokenIn)
            tokensReturned, PriceImpact = self.strategy.functions.getExpectedOutAmount(intkn.address, self.coin.address,
                                                                                       amount).call(
                {'from': W3.eth.defaultAccount, 'gas': 5_000_000}
            )
            return tokensReturned
        else:
            raise Exception("In token should be either long or short")

    def getExpectedInAmount(self, tokenOut, amount):
        if (tokenOut == "long" or tokenOut == "short"):
            intkn = self.switch(tokenOut)
            tokensReturned, PriceImpact = self.strategy.functions.getExpectedInAmount(
                intkn.address, self.coin.address, amount).call(
                {'from': W3.eth.defaultAccount, 'gas': 5_000_000}
            )
            return tokensReturned
        else:
            raise Exception("Out token should be either long or short")
