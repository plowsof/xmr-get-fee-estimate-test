```
get_fee_estimate
```
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

Yet to find a high fee, but found some useless nodes:
```
[http://141.98.28.67:18089/get_info](http://141.98.28.67:18089/get_info)
[http://185.157.160.119:18089/get_info](http://185.157.160.119:18089/get_info)
[http://217.91.47.142:18089/get_info](http://217.91.47.142:18089/get_info)
[http://204.8.15.5:18089/get_info](http://204.8.15.5:18089/get_info)
```
