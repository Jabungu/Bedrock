import json
from web3 import Web3
 

infura_url="https://mainnet.infura.io/v3/1a8d55910dd4470898ba27e44fb97c5f"
web3 = Web3(Web3.HTTPProvider(infura_url))


abi=json.loads('[{"inputs":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"string","name":"_FirstName","type":"string"},{"internalType":"string","name":"_LastName","type":"string"},{"internalType":"string","name":"_Address1","type":"string"},{"internalType":"string","name":"_Address2","type":"string"},{"internalType":"string","name":"_City","type":"string"},{"internalType":"string","name":"_State","type":"string"},{"internalType":"uint256","name":"_Zip","type":"uint256"},{"internalType":"string","name":"_Country","type":"string"}],"name":"addUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"userCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
address=web3.toChecksumAddress("0x82fb058b5195464076c23B558a5a854BD5d8FDB6")

contract = web3.eth.contract(address=address, abi=abi)

print(contract)

print(contract.functions.addUser("0x63d8B779d8Ed2f6F8bd1B6F33A161bfBd863004E", 1, "ass", "ass", "ass", "ass", "ass", "ass", 1,  "ass").call())
