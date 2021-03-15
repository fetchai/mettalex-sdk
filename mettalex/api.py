from .abi import (
    vault_v2, balancer_pool, pool_controller_202102 as pool_controller, y_vault, y_controller,
    coin as coin_abi, position as position_abi
)


def get_strategy_state(w3, address):
    strategy = w3.eth.contract(address=address, abi=pool_controller)
    return strategy


class Vault(object):
    def __init__(self, w3, address):
        self.w3 = w3
        self.contract = w3.eth.contract(address=address, abi=vault_v2)
        self.state = {
            'floor': None,
            'cap': None,
            'spot': None,
            'is_settled': None,
            'coin': None,
            'short': None,
            'long': None,
            'coin_balance': None,
            'short_balance': None,
            'long_balance': None
        }
        self.property_map = {
            'floor': 'priceFloor',
            'cap': 'priceCap',
            'spot': 'priceSpot',
            'is_settled': 'isSettled',
            'coin': {
                'address': 'collateralToken',
                'abi': coin_abi
            },
            'short': {
                'address': 'shortPositionToken',
                'abi': position_abi
            },
            'long': {
                'address': 'longPositionToken',
                'abi': position_abi
            }
        }

    def view_property(self, name):
        return self.contract.functions[name]().call()

    def get(self, name: str) -> object:
        assert name in self.state.keys()
        if self.state[name] is None:
            if name in {'floor', 'cap', 'spot', 'is_settled'}:
                self.state[name] = self.view_property(self.property_map[name])
            elif name in {'coin', 'long', 'short'}:
                self.state[name] = self.w3.eth.contract(
                    address=self.contract.functions[self.property_map[name]['address']]().call(),
                    abi=self.property_map[name]['abi']
                )
            elif name in {'coin_balance', 'short_balance', 'long_balance'}:
                token = name.split('_')[0]
                self.state[name] = self.balance(token)
            else:
                raise ValueError(f'Unknown property {name}')
        return self.state[name]

    def update(self):
        for name in self.state.keys():
            self.get(name)

    def balance(self, token):
        tok = self.get(token)
        if token == 'coin':
            amt = tok.functions.balanceOf(self.contract.address).call()
        elif token in {'short', 'long'}:
            amt = tok.functions.totalSupply().call()
        else:
            raise ValueError(f'Unknown token {token}')
        return amt / (10**tok.functions.decimals().call())

    def __repr__(self):
        out_str = '\n'.join(
            [
                f'Mettalex Vault: {self.contract.address}',
                f'  Prices - Floor: {self.get("floor")}  Spot: {self.get("spot")} Cap: {self.get("cap")}',
                f'  Coin : {self.get("coin").address}  {self.get("coin_balance")}',
                f'  Short: {self.get("short").address}  {self.get("short_balance")}',
                f'  Long : {self.get("long").address}  {self.get("long_balance")}',
            ]
        )
        return out_str


class LiquidityPool(object):
    def __init__(self, w3, address):
        self.w3 = w3
        self.contract = w3.eth.contract(address=address, abi=y_vault)
        self.state = {
            'y_vault': self.contract,
            'coin': None,
            'long': None,
            'short': None,
            'vault_controller': None,
            'strategy': None,
            'balancer': None,
            'coin_balance': None,
            'short_balance': None,
            'long_balance': None,
        }
        self.property_map = {
            'coin': {
                'address': 'token',
                'abi': coin_abi
            },
            'long': {
                'contract': 'strategy',
                'address': 'longToken',
                'abi': position_abi
            },
            'short': {
                'contract': 'strategy',
                'address': 'shortToken',
                'abi': position_abi
            },
            'vault_controller': {
                'address': 'controller',
                'abi': y_controller
            },
            'strategy': {
                'contract': 'vault_controller',
                'address': 'strategies',  # Property of y-vault controller
                'abi': pool_controller
            },
            'balancer': {
                'contract': 'strategy',
                'address': 'balancer',  # Property of strategy
                'abi': balancer_pool
            },
        }

    def view_property(self, name):
        return self.contract.functions[name]().call()

    def get(self, name: str) -> object:
        assert name in self.state.keys(), name
        if self.state[name] is None:
            if name == 'coin':
                self.state[name] = self.w3.eth.contract(
                    address=self.contract.functions[self.property_map[name]['address']]().call(),
                    abi=self.property_map[name]['abi']
                )
            elif name == 'vault_controller':
                self.state[name] = self.w3.eth.contract(
                    address=self.contract.functions[self.property_map[name]['address']]().call(),
                    abi=self.property_map[name]['abi']
                )
            elif name == 'strategy':
                v_controller = self.get('vault_controller')
                strategy_address = v_controller.functions.strategies(self.get('coin').address).call()
                self.state[name] = self.w3.eth.contract(
                    address=strategy_address,
                    abi=self.property_map[name]['abi']
                )
            elif name in {'balancer', 'long', 'short'}:
                strategy = self.get('strategy')
                self.state[name] = self.w3.eth.contract(
                    address=strategy.functions[self.property_map[name]['address']]().call(),
                    abi=self.property_map[name]['abi']
                )
            elif name in {'coin_balance', 'short_balance', 'long_balance'}:
                token = name.split('_')[0]
                self.state[name] = self.balance(token)
            elif name == 'y_vault':
                self.state[name] = self.contract
        return self.state[name]

    def get_spot(self, token):
        strategy = self.get('strategy')
        spot = strategy.functions.getExpectedInAmount(
            self.get('coin').address, self.get(token).address,
            10**(self.get(token).functions.decimals().call())
        ).call()[0] / 10 ** (self.get('coin').functions.decimals().call())
        return spot

    def update(self):
        for name in self.state.keys():
            self.state[name] = None
            self.get(name)

    def balance(self, token):
        tok = self.get(token)
        components = ['y_vault', 'vault_controller', 'strategy', 'balancer']
        decimals_scale = (10 ** tok.functions.decimals().call())
        return {
            c: tok.functions.balanceOf(self.get(c).address).call() / decimals_scale
            for c in components
        }

    def earn(self, w3, acct=None):
        if acct is None:
            acct = w3.eth.defaultAccount
        tx_hash = self.get('y_vault').functions.earn().transact(
            {'from': acct, 'gas': 5_000_000})
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def __repr__(self):
        out_str = '\n'.join(
            [
                f'Mettalex Liquidity Pool: {self.contract.address}',
                f'  Coin : {self.get("coin").address}  {self.get("coin_balance")}',
                f'  Short: {self.get("short").address}  {self.get("short_balance")}',
                f'  Long : {self.get("long").address}  {self.get("long_balance")}',
            ]
        )
        return out_str
