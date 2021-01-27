import os
import subprocess
from pathlib import Path
import json
import argparse
import shutil
import requests
import web3

# class Metallex:
INNFURA_SECRET = ''
INNFURA_PROJECT_ID = ''
USER_KEY = ''
NETWORK_ID = ''
COMMODITY_LIST = []

abi_BFactory = [
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
abi_BPool = [
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
abi_coin = [
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
abi_position = [
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
abi_vault = [
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
abi_yController = [
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
abi_yVault = [
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
abi_poolController = [
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

# def read_config():
#     with open(os.path.expanduser('~/.mettalex/config-dev.json'), 'r') as f:
#         config = json.load(f)
#     return config

def connectNetwork(network, account='admin'):
    if network == 'local':
        from web3 import Web3

        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        try:
            w3.eth.defaultAccount = w3.eth.accounts[0]
            admin = w3.eth.accounts[0]
        except:
            raise Exception("Ensure ganache-cli is connected")
    elif network == 'bsc-testnet':
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
        os.environ['WEB3_PROVIDER_URI'] = ' https://bsc-dataseed.binance.org/'
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


def connect_deployed(w3, contracts, tkn = ""):
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


def swap(w3,strategy, tokenIn, amountIn, tokenOut, amountOut=1):
    # approve
    tx_hash = tokenIn.functions.approve(strategy.address, amountIn).transact(
        {'from': w3.eth.defaultAccount, 'gas': 1_000_000}
    )
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("txn approved")

    # swap
    MAX_UINT_VALUE = 2**256 - 1

    tx_hash = strategy.functions.swapExactAmountIn(tokenIn.address, amountIn, tokenOut.address, amountOut, MAX_UINT_VALUE).transact(
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

def connect(network, userkey, infuraSecret = '', infuraProjectId = ''):
    global INNFURA_SECRET, INNFURA_PROJECT_ID, USER_KEY, NETWORK_ID, W3, CONTRACTS
    if (network == "kovan"):
      if(infuraSecret == '' and infuraProjectId == ''):
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
  url = "https://storage.googleapis.com/mettalex-assets-stats/commodities_"+str(NETWORK_ID)+".json"
  payload={}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)
  cmdts = []
  # for commodity in json.loads(response.text)["data"]:
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
    # self.balancer = self.deployed_contracts['BPool']
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
    if(intkn == outtkn):
      raise Exception("In and out token can't be same")
    if(intkn == "--" or intkn == "--"):
      raise Exception("In token or out token not valid")
    print("swap started")
    swap(self.w3,self.strategy, intkn, amountIn, outtkn, amountOut)

  def getExpectedOutAmount(self, tokenIn, amount):
    if (tokenIn == "long" or tokenIn == "short"):
      intkn = self.switch(tokenIn)
      tokensReturned,PriceImpact = self.strategy.functions.getExpectedOutAmount(intkn.address, self.coin.address, amount).call(
        {'from': W3.eth.defaultAccount, 'gas': 5_000_000}
      )
      return tokensReturned
    else:
      raise Exception("In token should be either long or short")

  def getExpectedInAmount(self, tokenOut, amount):
    if (tokenOut == "long" or tokenOut == "short"):
      intkn = self.switch(tokenOut)
      tokensReturned,PriceImpact = self.strategy.functions.getExpectedInAmount(intkn.address, self.coin.address, amount).call(
        {'from': W3.eth.defaultAccount, 'gas': 5_000_000}
      )
      return tokensReturned
    else:
      raise Exception("Out token should be either long or short")
