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
