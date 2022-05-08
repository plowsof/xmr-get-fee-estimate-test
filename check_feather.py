import requests
import pprint 
from stem import Signal
from stem.control import Controller

def get_feather_nodes():
  r = requests.get("https://raw.githubusercontent.com/feather-wallet/feather/master/src/assets/nodes.json")
  return r.json()
# signal TOR for a new connection 
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="hunter2")
        controller.signal(Signal.NEWNYM)
        
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}
    return session

#https://stackoverflow.com/questions/42971622/fetching-a-onion-domain-with-requests
def tor_get_fee(ses,node):
  try:
    node = f"http://{node}/json_rpc"
    r = ses.post(node, json={"jsonrpc":"2.0","id":"0","method":"get_fee_estimate","params":{"client":""}}, timeout=5)
    print(f'{node} | {r.json()["result"]["fee"]}')
  except Exception as e:
    pass

def clear_get_fee(node):
  try:
    node = f"http://{node}/json_rpc"
    r = requests.post(node, json={"jsonrpc":"2.0","id":"0","method":"get_fee_estimate","params":{"client":""}}, timeout=5)
    print(f'{node} | {r.json()["result"]["fee"]}')
  except Exception as e:
    pass

def main():
  feather_nodes = get_feather_nodes()
  ses = get_tor_session()

  pprint.pprint(feather_nodes)

  for network in feather_nodes:
    print(f"{network} | fee")
    print(f"--- | ---")
    for node in feather_nodes[network]["tor"]:
      tor_get_fee(ses,node) 
    for node in feather_nodes[network]["clearnet"]:
      clear_get_fee(node)

if __name__ == "__main__":
  main()