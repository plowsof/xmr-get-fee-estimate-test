import requests
import pprint
from check_feather import get_tor_session, clear_get_fee, tor_get_fee

mainnet = requests.get("https://www.ditatompel.com/api/monero/remote-node?nettype=mainnet").json()["data"]
stagenet = requests.get("https://www.ditatompel.com/api/monero/remote-node?nettype=stagenet").json()["data"]
testnet = requests.get("https://www.ditatompel.com/api/monero/remote-node?nettype=testnet").json()["data"]

data = {
"mainnet": mainnet,
"testnet": testnet,
"stagenet": stagenet
}

ses = get_tor_session()

for network in data:
	print(f"ditatompel {network} nodes | fee")
	print(f'--- | ---')
	for node in data[network]:
		hostname = (f'{node["hostname"]}:{node["port"]}')
		if ".onion" in hostname:
			tor_get_fee(ses,hostname)
		else:
			clear_get_fee(hostname)
	print("\n")
