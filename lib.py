from decimal import Decimal
import json
import requests


EXCHANGE_RATE = 1.241 # 1 aUST == 1.241 UST
BLOCKS_PER_YEAR = 4_656_810

def get_balance(address):
    """Return balance for a given address in UST"""

    query_str = '{tokenBalance: WasmContractsContractAddressStore(ContractAddress: "terra1hzh9vpxhsk8253se0vv5jj6etdvxu3nv8z07zu" QueryMsg: "{\\"balance\\":{\\"address\\":\\"'+ address +'\\"}}"){Result Height}}'
    res = requests.post(f'https://mantle.terra.dev/?cw20--balance=terra1hzh9vpxhsk8253se0vv5jj6etdvxu3nv8z07zu', {'query': query_str, 'variables': {}})

    balance = json.loads(json.loads(res.content)['data']['tokenBalance']['Result'])['balance']

    balance = (int(balance) * EXCHANGE_RATE) / 1000000
    return round(balance, 3)

def get_interest():
    """Returns interest rate in APY"""

    query_str = "{\n  moneyMarketEpochState: WasmContractsContractAddressStore(\n    ContractAddress: \"terra1sepfj7s0aeg5967uxnfk4thzlerrsktkpelm5s\"\n    QueryMsg: \"{\\\"epoch_state\\\":{\\\"block_height\\\":7423358}}\"\n  ) {\n    Result\n    Height\n  }\n  overseerEpochState: WasmContractsContractAddressStore(\n    ContractAddress: \"terra1tmnqgvg567ypvsvk6rwsga3srp7e3lg6u0elp8\"\n    QueryMsg: \"{\\\"epoch_state\\\":{}}\"\n  ) {\n    Result\n    Height\n  }\n}\n"
    response = requests.post('https://mantle.terra.dev/?earn--epoch-states', 
    {"query":query_str, "variables":{}})
    
    result = response.json()['data']
    data = json.loads(result['overseerEpochState']['Result'])
   
    deposit_rate = BLOCKS_PER_YEAR * Decimal(data['deposit_rate']) * 100

    return round(deposit_rate, 2)
