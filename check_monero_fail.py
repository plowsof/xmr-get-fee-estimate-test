import requests
import pprint 
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

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
def tor_get_fee(ses,node,f):
  try:
    node = f"{node}/json_rpc"
    r = ses.post(node, json={"jsonrpc":"2.0","id":"0","method":"get_fee_estimate","params":{"client":""}}, timeout=5)
    f.write(f'{node} | {r.json()["result"]["fee"]}    \n')
  except Exception as e:
    pass

def clear_get_fee(node,f):
  try:
    node = f"{node}/json_rpc"
    r = requests.post(node, json={"jsonrpc":"2.0","id":"0","method":"get_fee_estimate","params":{"client":""}}, timeout=5)
    f.write(f'{node} | {r.json()["result"]["fee"]}    \n')
  except Exception as e:
    pass


networks = ["https://monero.fail/?nettype=mainnet","https://monero.fail/?nettype=testnet","https://monero.fail/?nettype=stagenet"]
node_list = {}
node_list["https://monero.fail/?nettype=mainnet"] = []
node_list["https://monero.fail/?nettype=testnet"] = []
node_list["https://monero.fail/?nettype=stagenet"] = []
for network in networks:
  response = requests.get(network)
  webpage = response.content
  soup = BeautifulSoup(webpage, "html.parser")
  for tr in soup.find_all('tr'):
      values = [data for data in tr.find_all('td')]
      for value in values:
          if "http" in value.text:
            node_list[network].append(value.text)



ses = get_tor_session()

with open("output_check_monero_fail.md", "w+") as f:
  for network in node_list:
    f.write(f"{network} | fee\n")
    f.write("--- | ---\n")
    for node in node_list[network]:
      print(node)
      if ".onion" in node:
        tor_get_fee(ses,node,f)
      else:
        clear_get_fee(node,f)
    f.write("\n")
