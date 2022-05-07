```
get_fee_estimate
```

Yet to find a high fee (using get_peer_list from my home node), but found some useless nodes:    
- [http://141.98.28.67:18089/get_info](http://141.98.28.67:18089/get_info)    
- [http://185.157.160.119:18089/get_info](http://185.157.160.119:18089/get_info)   
- [http://217.91.47.142:18089/get_info](http://217.91.47.142:18089/get_info)
- [http://204.8.15.5:18089/get_info](http://204.8.15.5:18089/get_info)

### quick test on [FeatherWallets' node list](https://github.com/feather-wallet/feather/blob/d379262a78af4f846949684e310ed5acf2354025/src/assets/nodes.json#L18) 

node | fee
---|---
http://sfprpc5klzs5vyitq2mrooicgk2wcs5ho2nm3niqduvzn5o6ylaslaqd.onion:18089/json_rpc | 4185
http://majesticrepik35vnngouksfl7jiwf6sj7s2doj3bvdffq27tgqoeayd.onion:18089/json_rpc | 4185
http://mxcd4577fldb3ppzy7obmmhnu3tf57gbcbd4qhwr2kxyjj2qi3dnbfqd.onion:18081/json_rpc | 4185
http://moneroxmrxw44lku6qniyarpwgznpcwml4drq7vb24ppatlcg4kmxpqd.onion:18089/json_rpc | 4185
http://6dsdenp6vjkvqzy4wzsnzn6wixkdzihx3khiumyzieauxuxslmcaeiad.onion:18081/json_rpc | 4185
http://56wl7y2ebhamkkiza4b7il4mrzwtyvpdym7bm2bkg3jrei2je646k3qd.onion:18089/json_rpc | 4185
http://ip4zpbps7unk6xhlanqtw24f75akfbl3upeckfjqjks7ftfnk4i73oid.onion:18081/json_rpc | 4185
http://xmrnodesarnt4w35aqmu66aart3o324yw6qbnv6pglpof6uqaydzk5id.onion:18081/json_rpc | 4185
http://mhfsxznn5pi4xuxohj5k7unqp73sa6d44mbeewbpxnm25z3wzfogcfyd.onion:18081/json_rpc | 4185
http://node.community.rino.io:18081/json_rpc | 4185
http://node.sethforprivacy.com:18089/json_rpc | 4185
http://node2.sethforprivacy.com:18089/json_rpc | 4185
http://selsta1.featherwallet.net:18081/json_rpc | 4185
http://selsta2.featherwallet.net:18081/json_rpc | 4185
http://node.monerooutreach.org:18081/json_rpc | 4185
http://node.majesticbank.is:18089/json_rpc | 4185
http://node.majesticbank.su:18089/json_rpc | 4185
http://xmr-node-eu.cakewallet.com:18081/json_rpc | 4185
http://xmr-node-usa-east.cakewallet.com:18081/json_rpc | 4185
http://node.supportxmr.com:18081/json_rpc | 4185
http://node.xmr.ru:18081/json_rpc | 4185
http://testnet.community.rino.io:28081/json_rpc | 9823
http://ct36dsbe3oubpbebpxmiqz4uqk6zb6nhmkhoekileo4fts23rvuse2qd.onion:38081/json_rpc | 30439
http://stagenet.community.rino.io:38081/json_rpc | 30439

Python:
```
r = requests.post('node.sethforprivacy.com:18089/json_rpc', json={"jsonrpc":"2.0","id":"0","method":"get_fee_estimate","params":{"client":""}})
pprint.pprint(r.json())
```

cURL:
```
curl node.sethforprivacy.com:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_fee_estimate","params":{"client":""}}' -H 'Content-Type: application/json'
```

Output:
```
{'id': '0',
 'jsonrpc': '2.0',
 'result': {'credits': 0,
            'fee': 4187,
            'quantization_mask': 10000,
            'status': 'OK',
            'top_hash': '',
            'untrusted': False}}
```

Significance of client other than nodes to identity a request?


requests using tor [using python](https://stackoverflow.com/questions/30286293/make-requests-using-python-over-tor)



```python
def get_fee_curl(node):
  try:
    r = requests.post(node, json={"jsonrpc":"2.0","id":"0","method":"get_fee_estimate","params":{"client":""}}, timeout=5)
    print(r.json()["result"]["fee"])
  except:
    pass
   
#my local nodes peer list
data = requests.get("http://192.168.1.68:18081/get_peer_list")
data = data.json()

for x in data["white_list"]:
    try:
        if x["rpc_port"]:
            if "::ffff:" in x["host"]:
                x["host"] = x["host"].split("::ffff:")[1]
            node = f'http://{x["host"]}:{x["rpc_port"]}/json_rpc'
            try:
              th = threading.Thread(target=get_fee_curl, args=(node,))
              th.start()
            except:
              pass
    except:
        pass
```

