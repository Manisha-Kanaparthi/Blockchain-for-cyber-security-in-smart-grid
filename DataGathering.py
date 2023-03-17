import requests
import iotDevice
import time
from web3 import Web3,HTTPProvider
import json

def connect_with_energy_meter(acc):
    blockchainServer='http://127.0.0.1:7545'
    web3=Web3(HTTPProvider(blockchainServer))
    if acc==0:
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='build/contracts/energymeter.json'
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']
        contract_address=contract_json['networks']['5777']['address']
    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    return(contract,web3)

apiRequest='https://api.thingspeak.com/update?api_key=SFV5HOTQWQHZWUP4&field1='

while True:
    v,c,p=iotDevice.getSensoryFeed()
    apiRequest+=str(v)+'&field2='+str(c)+'&field3='+str(p)
    statusCode=requests.get(apiRequest)
    print(statusCode)
    contract,web3=connect_with_energy_meter(0)
    tx_hash=contract.functions.insertData(str(v),str(c),str(p)).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    time.sleep(10)


