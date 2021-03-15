vault_v1 = [
    {'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'},
                {'internalType': 'uint256', 'name': '_version', 'type': 'uint256'},
                {'internalType': 'address', 'name': '_collateralToken', 'type': 'address'},
                {'internalType': 'address', 'name': '_longPosition', 'type': 'address'},
                {'internalType': 'address', 'name': '_shortPosition', 'type': 'address'},
                {'internalType': 'address', 'name': '_oracleAddress', 'type': 'address'},
                {'internalType': 'address',
                 'name': '_automatedMarketMaker',
                 'type': 'address'},
                {'internalType': 'uint256', 'name': '_cap', 'type': 'uint256'},
                {'internalType': 'uint256', 'name': '_floor', 'type': 'uint256'},
                {'internalType': 'uint256', 'name': '_multiplier', 'type': 'uint256'},
                {'internalType': 'uint256', 'name': '_feeRate', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'constructor'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': '_previousAMM',
                 'type': 'address'},
                {'indexed': True,
                 'internalType': 'address',
                 'name': '_newAMM',
                 'type': 'address'}],
     'name': 'AutomatedMarketMakerUpdated',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'uint256',
                 'name': '_settlePrice',
                 'type': 'uint256'}],
     'name': 'ContractSettled',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': '_payee',
                 'type': 'address'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_weiAmount',
                 'type': 'uint256'}],
     'name': 'FeeClaimed',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': '_previousOracle',
                 'type': 'address'},
                {'indexed': True,
                 'internalType': 'address',
                 'name': '_newOracle',
                 'type': 'address'}],
     'name': 'OracleUpdated',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': 'previousOwner',
                 'type': 'address'},
                {'indexed': True,
                 'internalType': 'address',
                 'name': 'newOwner',
                 'type': 'address'}],
     'name': 'OwnershipTransferred',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': '_settler',
                 'type': 'address'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_longTokensBurned',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_shortTokensBurned',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_collateralReturned',
                 'type': 'uint256'}],
     'name': 'PositionSettled',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': False,
                 'internalType': 'address[]',
                 'name': '_settlers',
                 'type': 'address[]'},
                {'indexed': False,
                 'internalType': 'uint8',
                 'name': '_length',
                 'type': 'uint8'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_totalLongBurned',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_totalShortBurned',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_totalCollateralReturned',
                 'type': 'uint256'}],
     'name': 'PositionSettledInBulk',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': '_to',
                 'type': 'address'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_value',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_collateralRequired',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_collateralFee',
                 'type': 'uint256'}],
     'name': 'PositionsMinted',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': '_to',
                 'type': 'address'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_tokensBurned',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': '_collateralReturned',
                 'type': 'uint256'}],
     'name': 'PositionsRedeemed',
     'type': 'event'},
    {'anonymous': False,
     'inputs': [{'indexed': False,
                 'internalType': 'uint256',
                 'name': '_price',
                 'type': 'uint256'}],
     'name': 'UpdatedLastPrice',
     'type': 'event'},
    {'constant': True,
     'inputs': [],
     'name': 'automatedMarketMaker',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address[]',
                 'name': '_settlers',
                 'type': 'address[]'}],
     'name': 'bulkSettlePositions',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}],
     'name': 'claimFee',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'collateralFeePerUnit',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'collateralPerUnit',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'collateralToken',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'contractName',
     'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'feeAccumulated',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'isOwner',
     'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'isSettled',
     'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'longPositionToken',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'uint256',
                 'name': '_collateralAmount',
                 'type': 'uint256'}],
     'name': 'mintFromCollateralAmount',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'uint256',
                 'name': '_quantityToMint',
                 'type': 'uint256'}],
     'name': 'mintPositions',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'oracle',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'owner',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'priceCap',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'priceFloor',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'priceSpot',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'qtyMultiplier',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'uint256',
                 'name': '_quantityToRedeem',
                 'type': 'uint256'}],
     'name': 'redeemPositions',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'},
                {'internalType': 'uint256', 'name': '_redeemQuantity', 'type': 'uint256'}],
     'name': 'redeemPositions',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [],
     'name': 'renounceOwnership',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [],
     'name': 'settlePositions',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'settlementPrice',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'settlementTimeStamp',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'shortPositionToken',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': 'newOwner',
                 'type': 'address'}],
     'name': 'transferOwnership',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': '_newAMM',
                 'type': 'address'}],
     'name': 'updateAutomatedMarketMaker',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': '_newOracle',
                 'type': 'address'}],
     'name': 'updateOracle',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'uint256', 'name': '_price', 'type': 'uint256'}],
     'name': 'updateSpot',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'version',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'}]

balancer_factory = [
    {
        "inputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "caller",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "blabs",
                "type": "address"
            }
        ],
        "name": "LOG_BLABS",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "caller",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "LOG_NEW_POOL",
        "type": "event"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "contract BPool",
                "name": "pool",
                "type": "address"
            }
        ],
        "name": "collect",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getBLabs",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getColor",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "b",
                "type": "address"
            }
        ],
        "name": "isBPool",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "newBPool",
        "outputs": [
            {
                "internalType": "contract BPool",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "b",
                "type": "address"
            }
        ],
        "name": "setBLabs",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
balancer_pool = [
    {
        "inputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "src",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "dst",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": True,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes4",
                "name": "sig",
                "type": "bytes4"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "caller",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "LOG_CALL",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "caller",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            }
        ],
        "name": "LOG_EXIT",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "caller",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            }
        ],
        "name": "LOG_JOIN",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "caller",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            }
        ],
        "name": "LOG_SWAP",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "src",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "dst",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "BONE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "BPOW_PRECISION",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "EXIT_FEE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "INIT_POOL_SUPPLY",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MAX_BOUND_TOKENS",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MAX_BPOW_BASE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MAX_FEE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MAX_IN_RATIO",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MAX_OUT_RATIO",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MAX_TOTAL_WEIGHT",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MAX_WEIGHT",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MIN_BALANCE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MIN_BOUND_TOKENS",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MIN_BPOW_BASE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MIN_FEE",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "MIN_WEIGHT",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "src",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "dst",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "dst",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "whom",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "denorm",
                "type": "uint256"
            }
        ],
        "name": "bind",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenBalanceIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenBalanceOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "calcInGivenOut",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenBalanceIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenBalanceOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "calcOutGivenIn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenBalanceOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "poolSupply",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalWeight",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "calcPoolInGivenSingleOut",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "poolAmountIn",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenBalanceIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "poolSupply",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalWeight",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "calcPoolOutGivenSingleIn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "poolAmountOut",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenBalanceIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "poolSupply",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalWeight",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "poolAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "calcSingleInGivenPoolOut",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenBalanceOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "poolSupply",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalWeight",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "poolAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "calcSingleOutGivenPoolIn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenBalanceIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenBalanceOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenWeightOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "calcSpotPrice",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "spotPrice",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "dst",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256"
            }
        ],
        "name": "decreaseApproval",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "poolAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256[]",
                "name": "minAmountsOut",
                "type": "uint256[]"
            }
        ],
        "name": "exitPool",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxPoolAmountIn",
                "type": "uint256"
            }
        ],
        "name": "exitswapExternAmountOut",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "poolAmountIn",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "poolAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minAmountOut",
                "type": "uint256"
            }
        ],
        "name": "exitswapPoolAmountIn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "finalize",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "getBalance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getColor",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getController",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getCurrentTokens",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "tokens",
                "type": "address[]"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "getDenormalizedWeight",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getFinalTokens",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "tokens",
                "type": "address[]"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "getNormalizedWeight",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getNumTokens",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            }
        ],
        "name": "getSpotPrice",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "spotPrice",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            }
        ],
        "name": "getSpotPriceSansFee",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "spotPrice",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getSwapFee",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getTotalDenormalizedWeight",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "gulp",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "dst",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256"
            }
        ],
        "name": "increaseApproval",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "t",
                "type": "address"
            }
        ],
        "name": "isBound",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isFinalized",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isPublicSwap",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "poolAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256[]",
                "name": "maxAmountsIn",
                "type": "uint256[]"
            }
        ],
        "name": "joinPool",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minPoolAmountOut",
                "type": "uint256"
            }
        ],
        "name": "joinswapExternAmountIn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "poolAmountOut",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "poolAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxAmountIn",
                "type": "uint256"
            }
        ],
        "name": "joinswapPoolAmountOut",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "denorm",
                "type": "uint256"
            }
        ],
        "name": "rebind",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "manager",
                "type": "address"
            }
        ],
        "name": "setController",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "bool",
                "name": "public_",
                "type": "bool"
            }
        ],
        "name": "setPublicSwap",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "swapFee",
                "type": "uint256"
            }
        ],
        "name": "setSwapFee",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "minAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxPrice",
                "type": "uint256"
            }
        ],
        "name": "swapExactAmountIn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "spotPriceAfter",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "maxAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxPrice",
                "type": "uint256"
            }
        ],
        "name": "swapExactAmountOut",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "spotPriceAfter",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "dst",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "src",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "dst",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amt",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "unbind",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
coin = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_symbol",
                "type": "string"
            },
            {
                "internalType": "uint8",
                "name": "_decimals",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "Burn",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "Mint",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_from",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "burn",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "subtractedValue",
                "type": "uint256"
            }
        ],
        "name": "decreaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "addedValue",
                "type": "uint256"
            }
        ],
        "name": "increaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "mint",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "who",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "enable",
                "type": "bool"
            }
        ],
        "name": "setWhitelist",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "whitelist",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]
position = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_symbol",
                "type": "string"
            },
            {
                "internalType": "uint8",
                "name": "_decimals",
                "type": "uint8"
            },
            {
                "internalType": "uint256",
                "name": "_version",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "Burn",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "Mint",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Paused",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "PauserAdded",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "PauserRemoved",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "Unpaused",
        "type": "event"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "addPauser",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_from",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "burn",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "subtractedValue",
                "type": "uint256"
            }
        ],
        "name": "decreaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "addedValue",
                "type": "uint256"
            }
        ],
        "name": "increaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isOwner",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "isPauser",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "mint",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "pause",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "paused",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "renouncePauser",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "who",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "enable",
                "type": "bool"
            }
        ],
        "name": "setWhitelist",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "settled",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "unpause",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "updateNameToSettled",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "version",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "whitelist",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]
vault_v2 = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_name",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_version",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "_collateralToken",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_longPosition",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_shortPosition",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_oracleAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_ammPoolController",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_cap",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_floor",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_multiplier",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_feeRate",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_previousAMMPoolController",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "_newAMMPoolController",
                "type": "address"
            }
        ],
        "name": "AMMPoolControllerUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "_settlePrice",
                "type": "uint256"
            }
        ],
        "name": "ContractSettled",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_payee",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_weiAmount",
                "type": "uint256"
            }
        ],
        "name": "FeeClaimed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_previousOracle",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "_newOracle",
                "type": "address"
            }
        ],
        "name": "OracleUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_settler",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_longTokensBurned",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_shortTokensBurned",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_collateralReturned",
                "type": "uint256"
            }
        ],
        "name": "PositionSettled",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address[]",
                "name": "_settlers",
                "type": "address[]"
            },
            {
                "indexed": False,
                "internalType": "uint8",
                "name": "_length",
                "type": "uint8"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_totalLongBurned",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_totalShortBurned",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_totalCollateralReturned",
                "type": "uint256"
            }
        ],
        "name": "PositionSettledInBulk",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_value",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_collateralRequired",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_collateralFee",
                "type": "uint256"
            }
        ],
        "name": "PositionsMinted",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_tokensBurned",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_collateralReturned",
                "type": "uint256"
            }
        ],
        "name": "PositionsRedeemed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_price",
                "type": "uint256"
            }
        ],
        "name": "UpdatedLastPrice",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "ammPoolController",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address[]",
                "name": "_settlers",
                "type": "address[]"
            }
        ],
        "name": "bulkSettlePositions",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_to",
                "type": "address"
            }
        ],
        "name": "claimFee",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "collateralFeePerUnit",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "collateralPerUnit",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "collateralToken",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "contractName",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "feeAccumulated",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isOwner",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isSettled",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "longPositionToken",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_collateralAmount",
                "type": "uint256"
            }
        ],
        "name": "mintFromCollateralAmount",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_quantityToMint",
                "type": "uint256"
            }
        ],
        "name": "mintPositions",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "oracle",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "priceCap",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "priceFloor",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "priceSpot",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "qtyMultiplier",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_quantityToRedeem",
                "type": "uint256"
            }
        ],
        "name": "redeemPositions",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_redeemQuantity",
                "type": "uint256"
            }
        ],
        "name": "redeemPositions",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "settleFee",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "settlePositions",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "settlementPrice",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "settlementTimeStamp",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "shortPositionToken",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_newAMMPoolController",
                "type": "address"
            }
        ],
        "name": "updateAMMPoolController",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_newOracle",
                "type": "address"
            }
        ],
        "name": "updateOracle",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "newSettleFee",
                "type": "uint256"
            }
        ],
        "name": "updateSettleFee",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_price",
                "type": "uint256"
            }
        ],
        "name": "updateSpot",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "version",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]
y_controller = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_rewards",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "converters",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            }
        ],
        "name": "earn",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "factory",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "_strategy",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "parts",
                "type": "uint256"
            }
        ],
        "name": "getExpectedReturn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "expected",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "governance",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            }
        ],
        "name": "inCaseTokensGetStuck",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "max",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "onesplit",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "rewards",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_input",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_output",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_converter",
                "type": "address"
            }
        ],
        "name": "setConverter",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_factory",
                "type": "address"
            }
        ],
        "name": "setFactory",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_governance",
                "type": "address"
            }
        ],
        "name": "setGovernance",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_onesplit",
                "type": "address"
            }
        ],
        "name": "setOneSplit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_split",
                "type": "uint256"
            }
        ],
        "name": "setSplit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_strategy",
                "type": "address"
            }
        ],
        "name": "setStrategy",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_vault",
                "type": "address"
            }
        ],
        "name": "setVault",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "split",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "strategies",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "vaults",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            }
        ],
        "name": "withdrawAll",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_strategy",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "parts",
                "type": "uint256"
            }
        ],
        "name": "yearn",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
y_vault = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_controller",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "available",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "balance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "controller",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "subtractedValue",
                "type": "uint256"
            }
        ],
        "name": "decreaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            }
        ],
        "name": "deposit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "earn",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getPricePerFullShare",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "governance",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "addedValue",
                "type": "uint256"
            }
        ],
        "name": "increaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "max",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "min",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_controller",
                "type": "address"
            }
        ],
        "name": "setController",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_governance",
                "type": "address"
            }
        ],
        "name": "setGovernance",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_min",
                "type": "uint256"
            }
        ],
        "name": "setMin",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "token",
        "outputs": [
            {
                "internalType": "contract IERC20",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_shares",
                "type": "uint256"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
pool_controller = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_controller",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_want",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_balancer",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_mettalexVault",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_longToken",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_shortToken",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "caller",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            }
        ],
        "name": "LOG_SWAP",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "total",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "balancer",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "breaker",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "controller",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "getBalance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "fromToken",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "toToken",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "toTokenAmount",
                "type": "uint256"
            }
        ],
        "name": "getExpectedInAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokensReturned",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "priceImpact",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "fromToken",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "toToken",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "fromTokenAmount",
                "type": "uint256"
            }
        ],
        "name": "getExpectedOutAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokensReturned",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "priceImpact",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getSwapFee",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "governance",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "handleBreach",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "token",
                "type": "address"
            }
        ],
        "name": "isBound",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isBreachHandled",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "longToken",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "mettalexVault",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "bool",
                "name": "_breaker",
                "type": "bool"
            }
        ],
        "name": "setBreaker",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_controller",
                "type": "address"
            }
        ],
        "name": "setController",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_governance",
                "type": "address"
            }
        ],
        "name": "setGovernance",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_swapFee",
                "type": "uint256"
            }
        ],
        "name": "setSwapFee",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "shortToken",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenIn",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenAmountIn",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "tokenOut",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "minAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxPrice",
                "type": "uint256"
            }
        ],
        "name": "swapExactAmountIn",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "tokenAmountOut",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "spotPriceAfter",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_vault",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_ltk",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_stk",
                "type": "address"
            }
        ],
        "name": "updateCommodityAfterBreach",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_controller",
                "type": "address"
            }
        ],
        "name": "updatePoolController",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "updateSpotAndNormalizeWeights",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "want",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "_token",
                "type": "address"
            }
        ],
        "name": "withdraw",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "withdrawAll",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
pool_controller_202102 = [
    {'inputs': [{'internalType': 'address',
                 'name': '_controller',
                 'type': 'address'},
                {'internalType': 'address', 'name': '_want', 'type': 'address'},
                {'internalType': 'address', 'name': '_balancer', 'type': 'address'},
                {'internalType': 'address', 'name': '_mettalexVault', 'type': 'address'},
                {'internalType': 'address', 'name': '_longToken', 'type': 'address'},
                {'internalType': 'address', 'name': '_shortToken', 'type': 'address'},
                {'internalType': 'address', 'name': '_mtlxToken', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'constructor'},
    {'anonymous': False,
     'inputs': [{'indexed': True,
                 'internalType': 'address',
                 'name': 'caller',
                 'type': 'address'},
                {'indexed': True,
                 'internalType': 'address',
                 'name': 'tokenIn',
                 'type': 'address'},
                {'indexed': True,
                 'internalType': 'address',
                 'name': 'tokenOut',
                 'type': 'address'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': 'tokenAmountIn',
                 'type': 'uint256'},
                {'indexed': False,
                 'internalType': 'uint256',
                 'name': 'tokenAmountOut',
                 'type': 'uint256'}],
     'name': 'LOG_SWAP',
     'type': 'event'},
    {'constant': True,
     'inputs': [],
     'name': 'balanceOf',
     'outputs': [{'internalType': 'uint256', 'name': 'total', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'balancer',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'breaker',
     'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'controller',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [],
     'name': 'deposit',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}],
     'name': 'getBalance',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [{'internalType': 'address',
                 'name': 'fromToken',
                 'type': 'address'},
                {'internalType': 'address', 'name': 'toToken', 'type': 'address'},
                {'internalType': 'uint256', 'name': 'toTokenAmount', 'type': 'uint256'}],
     'name': 'getExpectedInAmount',
     'outputs': [{'internalType': 'uint256',
                  'name': 'tokensReturned',
                  'type': 'uint256'},
                 {'internalType': 'uint256', 'name': 'priceImpact', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [{'internalType': 'address',
                 'name': 'fromToken',
                 'type': 'address'},
                {'internalType': 'address', 'name': 'toToken', 'type': 'address'},
                {'internalType': 'uint256', 'name': 'fromTokenAmount', 'type': 'uint256'}],
     'name': 'getExpectedOutAmount',
     'outputs': [{'internalType': 'uint256',
                  'name': 'tokensReturned',
                  'type': 'uint256'},
                 {'internalType': 'uint256', 'name': 'priceImpact', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'getSwapFee',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'governance',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [],
     'name': 'handleBreach',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}],
     'name': 'isBound',
     'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'isBreachHandled',
     'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'longToken',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'mettalexVault',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'minMtlxBalance',
     'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'mtlxToken',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'newStrategy',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'bool', 'name': '_breaker', 'type': 'bool'}],
     'name': 'setBreaker',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': '_controller',
                 'type': 'address'}],
     'name': 'setController',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': '_governance',
                 'type': 'address'}],
     'name': 'setGovernance',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'uint256',
                 'name': 'balance',
                 'type': 'uint256'}],
     'name': 'setMinMtlxBalance',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': '_mtlxToken',
                 'type': 'address'}],
     'name': 'setMtlxTokenAddress',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': '_strategy',
                 'type': 'address'}],
     'name': 'setNewStrategy',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'uint256',
                 'name': '_swapFee',
                 'type': 'uint256'}],
     'name': 'setSwapFee',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'shortToken',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address', 'name': 'tokenIn', 'type': 'address'},
                {'internalType': 'uint256', 'name': 'tokenAmountIn', 'type': 'uint256'},
                {'internalType': 'address', 'name': 'tokenOut', 'type': 'address'},
                {'internalType': 'uint256', 'name': 'minAmountOut', 'type': 'uint256'},
                {'internalType': 'uint256', 'name': 'maxPrice', 'type': 'uint256'}],
     'name': 'swapExactAmountIn',
     'outputs': [{'internalType': 'uint256',
                  'name': 'tokenAmountOut',
                  'type': 'uint256'},
                 {'internalType': 'uint256', 'name': 'spotPriceAfter', 'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address', 'name': '_vault', 'type': 'address'},
                {'internalType': 'address', 'name': '_ltk', 'type': 'address'},
                {'internalType': 'address', 'name': '_stk', 'type': 'address'}],
     'name': 'updateCommodityAfterBreach',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address',
                 'name': '_controller',
                 'type': 'address'}],
     'name': 'updatePoolController',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [],
     'name': 'updateSpotAndNormalizeWeights',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': True,
     'inputs': [],
     'name': 'want',
     'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
     'payable': False,
     'stateMutability': 'view',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'uint256',
                 'name': '_amount',
                 'type': 'uint256'}],
     'name': 'withdraw',
     'outputs': [],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [{'internalType': 'address', 'name': '_token', 'type': 'address'}],
     'name': 'withdraw',
     'outputs': [{'internalType': 'uint256',
                  'name': 'balance',
                  'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'},
    {'constant': False,
     'inputs': [],
     'name': 'withdrawAll',
     'outputs': [{'internalType': 'uint256',
                  'name': 'balance',
                  'type': 'uint256'}],
     'payable': False,
     'stateMutability': 'nonpayable',
     'type': 'function'}]
