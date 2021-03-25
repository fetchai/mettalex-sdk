import os
import json
import requests
import pandas as pd
import time
from web3.middleware import construct_sign_and_send_raw_middleware

from mettalex.api import LiquidityPool, Vault, TX_TIMEOUT

INNFURA_SECRET = ''
INNFURA_PROJECT_ID = ''
USER_KEY = ''
NETWORK_ID = ''
COMMODITY_DATA = None
W3 = None

NETWORK_NAME_ID_MAP = {
    'kovan': '42',
    'bsc-mainnet': '56',
    'bsc-testnet': '97'
}


def setUser(w3, user):
    """

    :param w3:
    :param user:
    :return:
    """
    global W3
    w3.eth.defaultAccount = user.address
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(user))
    W3 = w3


def connectNetwork(network):
    if network == 'local':
        from web3 import Web3

        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        try:
            w3.eth.defaultAccount = w3.eth.accounts[0]
            user = w3.eth.accounts[0]
        except:
            raise Exception("Ensure ganache-cli is connected")
    elif network == 'bsc-testnet':
        os.environ['WEB3_PROVIDER_URI'] = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
        os.environ['WEB3_CHAIN_ID'] = '97'

        from web3.middleware import construct_sign_and_send_raw_middleware
        from web3.middleware import geth_poa_middleware
        from web3.auto import w3

        user = w3.eth.account.from_key(USER_KEY)
        w3.eth.defaultAccount = user.address
        try:
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        except ValueError as ex:
            print(f'Warning: "{ex}" on inject geth_poa_middleware.  Attempting to continue')
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(user))

    elif network == 'bsc-mainnet':
        os.environ['WEB3_PROVIDER_URI'] = 'https://bsc-dataseed.binance.org/'
        os.environ['WEB3_CHAIN_ID'] = '56'

        from web3.middleware import construct_sign_and_send_raw_middleware
        from web3.middleware import geth_poa_middleware
        from web3.auto import w3

        user = w3.eth.account.from_key(USER_KEY)
        w3.eth.defaultAccount = user.address
        try:
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        except ValueError as ex:
            print(f'Warning: "{ex}" on inject geth_poa_middleware.  Attempting to continue')
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(user))

    elif network == 'kovan':
        os.environ['WEB3_INFURA_PROJECT_ID'] = INNFURA_PROJECT_ID
        os.environ['WEB3_INFURA_API_SECRET'] = INNFURA_SECRET

        from web3.auto.infura.kovan import w3
        from web3.middleware import construct_sign_and_send_raw_middleware

        user = w3.eth.account.from_key(USER_KEY)
        w3.eth.defaultAccount = user.address
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(user))
    else:
        raise ValueError(f'Unknown network {network}')

    assert w3.isConnected()
    return w3, user


def get_network_id(w3):
    chain_id = w3.eth.chainId
    return chain_id


def get_coin(network_id, coin_name=None):
    coin_address = {
        '97': {
            'default': '0xa5Ebc90a713908872f137f7e468c2d887a8A2869'
        },
        '42': {
            'default': '0xe551960F80e5f855bB75d36016Ca92c981314b3E',
            'USDT': '0xe551960F80e5f855bB75d36016Ca92c981314b3E',
            'wUSD': '0xAE04c8e47cAc09e27A06b76407DA9C8836A576b6'
        },
        '56': {
            'default': '0x6e71C530bAdEB04b95C64a8ca61fe0b946A94525',
            'MUSD': '0x6e71C530bAdEB04b95C64a8ca61fe0b946A94525',
            'BUSD': '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'
        }
    }[str(network_id)][coin_name]
    return coin_address


def swap(w3, strategy, tokenIn, amountIn, tokenOut, amountOut=1):
    # approve
    tx_hash = tokenIn.functions.approve(strategy.address, amountIn).transact(
        {'from': w3.eth.defaultAccount, 'gas': 1_000_000}
    )
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=240)
    time.sleep(TX_TIMEOUT)

    # swap
    MAX_UINT_VALUE = 2 ** 256 - 1

    tx_hash = strategy.functions.swapExactAmountIn(tokenIn.address, amountIn, tokenOut.address, amountOut,
                                                   MAX_UINT_VALUE).transact(
        {'from': w3.eth.defaultAccount, 'gas': 5_000_000}
    )
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=240)
    time.sleep(TX_TIMEOUT)


def read_credentials(network, filename):
    with open(filename, 'r') as f:
        credentials = json.load(f)[network]
    user_key = credentials['user']['key']
    if network in {'kovan', 'eth-mainnet'}:
        infura_project = credentials['infura']['project_id']
        infura_secret = credentials['infura']['secret']
    else:
        infura_project = ''
        infura_secret = ''
    return user_key, infura_project, infura_secret


def connect(network, userkey='', infuraSecret='', infuraProjectId='', filename=None):
    global INNFURA_SECRET, INNFURA_PROJECT_ID, USER_KEY, NETWORK_ID, W3, CONTRACTS
    if filename is not None:
        userkey, infuraProjectId, infuraSecret = read_credentials(network, filename)
    else:
        assert userkey != '', 'Must supply user private key to trade'
    if network == "kovan":
        if (infuraSecret == '') and (infuraProjectId == ''):
            raise Exception("Provide infura details to connect to kovan")

    INNFURA_SECRET = infuraSecret
    INNFURA_PROJECT_ID = infuraProjectId
    USER_KEY = userkey
    w3, user = connectNetwork(network)
    NETWORK_ID = get_network_id(w3)
    print(f'Connected to network ID {NETWORK_ID}')
    W3 = w3
    return w3, user


def commodity_from_pool_address(liquidity_pool_address=None):
    assert W3 is not None, 'Needs connection to blockchain'
    w3 = W3
    pool = LiquidityPool(w3, liquidity_pool_address)
    strategy = pool.get('strategy')
    mettalex_contract_address = strategy.functions.mettalexVault().call()
    vault = Vault(w3, mettalex_contract_address)
    ltk = vault.get('long')
    tok_name = ltk.functions.symbol().call()
    symbol = tok_name[:len(tok_name) - tok_name[-1::-1].index('L') - 1]
    details = {
        'commodity_name': vault.contract.functions.contractName().call(),
        'liquidity_pool_address': liquidity_pool_address,
        'mettalex_contract_address': mettalex_contract_address
    }
    df_d = pd.DataFrame([details]).squeeze()
    commodity = Commodity(symbol, df_d)
    return commodity


def commodity_from_symbol(symbol, version=None):
    commodity_ind = COMMODITY_DATA['commodity_symbol'] == symbol
    if version is not None:
        commodity_ind &= (COMMODITY_DATA['version'] == version)
    assert commodity_ind.sum() > 0, "No commodities found with specified symbol"
    assert commodity_ind.sum() < 2, f"Multiple commodities:\n {COMMODITY_DATA.loc[commodity_ind, ['category', 'commodity_symbol', 'version', 'is_settled', 'id']]}"
    df_d = COMMODITY_DATA.loc[commodity_ind, :].squeeze()
    commodity = Commodity(symbol, df_d)
    return commodity


def commodity_from_id(commodity_id=None):
    df_d = COMMODITY_DATA.loc[COMMODITY_DATA['id'] == int(commodity_id), :].squeeze()
    symbol = df_d['commodity_symbol']
    commodity = Commodity(symbol, df_d)
    return commodity


def getCommodities(
        network=None, coin=None, output='dataframe', liquidity_pool_address=None
):
    global COMMODITY_DATA
    if network is not None:
        network_id = NETWORK_NAME_ID_MAP[network]
    else:
        network_id = NETWORK_ID

    coin = coin or 'all'
    if coin[:2] != '0x' and coin != 'all':
        coin = get_coin(network_id, coin)

    url = f"https://storage.googleapis.com/mettalex-assets-stats/commodities_{network_id}_{coin}.json"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    commodities = response.json()["data"]
    commodities.sort(key=lambda s: s['version'])
    commodities.reverse()
    COMMODITY_DATA = pd.DataFrame(commodities)
    if output.lower() == 'object':
        CommodityArr = []
        for cmdt in commodities:
            if cmdt['commodity_symbol'] not in CommodityArr:
                CommodityArr.append(cmdt['commodity_symbol'])
        return CommodityArr
    elif output.lower() == 'dataframe':
        return COMMODITY_DATA
    else:
        return commodities


class Commodity:
    def __init__(self, symbol, df_details, connect=True, w3=None):
        self.symbol = symbol
        self.commodity_details = df_details
        self.w3 = w3 or W3
        self.pool = None
        self.vault = None
        self.coin = None
        self.ltk = None
        self.stk = None
        self.strategy = None
        if connect:
            self.connect()

    def connect(self):
        self.pool = LiquidityPool(self.w3, self.commodity_details['liquidity_pool_address'])
        self.vault = Vault(self.w3, self.commodity_details['mettalex_contract_address'])
        self.coin = self.pool.get('coin')
        self.ltk = self.pool.get('long')
        self.stk = self.pool.get('short')
        self.strategy = self.pool.get('strategy')
        print("connection established sucessfully")

    def switch(self, token):
        switcher = {
            "long": self.ltk,
            "short": self.stk,
            "coin": self.coin
        }
        return switcher.get(token, "--")

    def mint(self, amount_in, unitless=False):
        token_order = ['coin', 'short', 'long']
        balance_pre = {k: v for k, v in zip(token_order, self.getUserBalance())}
        if not unitless:
            amount_in = int(amount_in * (10 ** self.coin.functions.decimals().call()))
        self.vault.mint(amount_in)
        balance_post = {k: v for k, v in zip(token_order, self.getUserBalance())}
        token_out = 'long'
        token_in = 'coin'
        received_amount = balance_post[token_out] - balance_pre[token_out]
        paid_amount = balance_pre[token_in] - balance_post[token_in]
        print(f'Paid {paid_amount:0.3f} {token_in} to mint {received_amount:0.3f} long and short')
        return paid_amount, received_amount

    def redeem(self, amount_in=None, unitless=False):
        token_order = ['coin', 'short', 'long']
        balance_pre = {k: v for k, v in zip(token_order, self.getUserBalance())}
        if amount_in is None:
            unitless = True
            _, ltk, stk = self.getUserBalance(unitless)
            amount_in = min(ltk, stk)

        if not unitless:
            amount_in = int(amount_in * (10 ** self.ltk.functions.decimals().call()))
        self.vault.redeem(amount_in)
        balance_post = {k: v for k, v in zip(token_order, self.getUserBalance())}
        token_out = 'coin'
        token_in = 'long'
        received_amount = balance_post[token_out] - balance_pre[token_out]
        paid_amount = balance_pre[token_in] - balance_post[token_in]
        print(f'Redeemed {paid_amount:0.3f} long and short for {received_amount:0.3f} coin')
        return paid_amount, received_amount

    def trade(self, token_in, token_out, amount_in, min_amount_out=1, unitless=False):
        if self.vault.contract.functions.isSettled().call() == True:
            raise Exception("Settled")
        intkn = self.switch(token_in)
        outtkn = self.switch(token_out)
        if intkn == outtkn:
            raise Exception("In and out token can't be same")
        if (intkn == "--") or (outtkn == "--"):
            raise Exception("In token or out token not valid")
        if not unitless:
            amount_in = int(amount_in * (10 ** intkn.functions.decimals().call()))
            min_amount_out = int(min_amount_out * (10 ** outtkn.functions.decimals().call()))
        token_order = ['coin', 'short', 'long']
        balance_pre = {k: v for k,v in zip(token_order, self.getUserBalance())}
        swap(self.w3, self.strategy, intkn, amount_in, outtkn, min_amount_out)
        balance_post = {k: v for k,v in zip(token_order, self.getUserBalance())}
        received_amount = balance_post[token_out] - balance_pre[token_out]
        paid_amount = balance_pre[token_in] - balance_post[token_in]
        print(f'Swapped {paid_amount:0.3f} {token_in} to {received_amount:0.3f} {token_out}')
        return paid_amount, received_amount

    def bid(self, token_in, amount, token_out='coin', unitless=False):
        """Return the bid for amount of position tokens

        :param token_in: type of position token, 'long' or 'short'
        :param amount: amount of position tokens to sell
        :param unitless: take into account coin and token decimals in input and output if False
        :return: amount of coin expected from sale
        """
        token_in = token_in.lower()
        assert token_in in {'long', 'short'}, "In token should be either long or short"

        if not unitless:
            amount = int(amount * (10 ** self.pool.get(token_in).functions.decimals().call()))
        intkn = self.switch(token_in)
        outtkn = self.switch(token_out)
        tokens_returned, price_impact = self.strategy.functions.getExpectedOutAmount(
            intkn.address, outtkn.address, amount
        ).call(
            {'from': W3.eth.defaultAccount, 'gas': 5_000_000}
        )
        if not unitless:
            tokens_returned = tokens_returned / (10 ** self.pool.get(token_out).functions.decimals().call())
        return tokens_returned

    def ask(self, token_out, amount, token_in='coin', unitless=False):
        token_out = token_out.lower()
        assert token_out in {'long', 'short'}, "Out token should be either long or short"

        if not unitless:
            amount = int(amount * (10 ** self.pool.get(token_out).functions.decimals().call()))
        out_tkn = self.switch(token_out)
        in_tkn = self.switch(token_in)
        tokens_returned, price_impact = self.strategy.functions.getExpectedInAmount(
            in_tkn.address, out_tkn.address, amount).call(
            {'from': W3.eth.defaultAccount, 'gas': 5_000_000}
        )
        if not unitless:
            tokens_returned = tokens_returned / (10 ** self.pool.get(token_in).functions.decimals().call())
        return tokens_returned

    def getUserBalance(self, unitless=False):
        user = self.w3.eth.defaultAccount
        coin_amt = self.coin.functions.balanceOf(user).call()
        short_amt = self.stk.functions.balanceOf(user).call()
        long_amt = self.ltk.functions.balanceOf(user).call()
        if not unitless:
            coin_amt /= 10**self.coin.functions.decimals().call()
            short_amt /= 10**self.stk.functions.decimals().call()
            long_amt /= 10**self.ltk.functions.decimals().call()
        return coin_amt, short_amt, long_amt

    def __repr__(self):
        out = f'{self.symbol}: {self.commodity_details["commodity_name"]}'
        if self.pool is not None:
            out += f'\n{self.vault}\n{self.pool}'
            try:
                out += f'\nShort spot price: {self.pool.get_spot("short")}  Long spot price : {self.pool.get_spot("long")}'
            finally:
                pass
        else:
            out = 'Not connected: ' + out
        return out
