from web3 import Web3
import json
import os

# Configuração da conexão com o blockchain
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Carregar o contrato inteligente
contract_path = os.path.abspath('blockchain/build/contracts/IdentityManagement.json')
with open(contract_path, 'r') as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']
    contract_address = contract_json['networks']['5777']['address']

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def register_identity(user_private_key, data):
    account = w3.eth.account.privateKeyToAccount(user_private_key)
    nonce = w3.eth.getTransactionCount(account.address)
    tx = contract.functions.registerIdentity(data).buildTransaction({
        'chainId': 5777,
        'gas': 70000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': nonce
    })
    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

def get_identity(user_address):
    identity = contract.functions.getIdentity(user_address).call()
    return identity
