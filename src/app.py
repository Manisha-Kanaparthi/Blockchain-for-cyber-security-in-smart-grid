from web3 import Web3,HTTPProvider
import json
from flask import Flask,render_template

def connect_with_energy_meter(acc):
    blockchainServer='http://127.0.0.1:7545'
    web3=Web3(HTTPProvider(blockchainServer))
    if acc==0:
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='../build/contracts/energymeter.json'
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']
        contract_address=contract_json['networks']['5777']['address']
    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    return(contract,web3)

app=Flask(__name__)

@app.route('/')
def homePage():
    contract,web3=connect_with_energy_meter(0)
    v,c,p=contract.functions.viewData().call()
    data=[]
    for i in range(len(v)):
        dummy=[]
        dummy.append(v[i])
        dummy.append(c[i])
        dummy.append(p[i])
        data.append(dummy)
    return render_template('index.html',dashboard_data=data,len=len(data))

if __name__=="__main__":
    app.run(debug=True)

