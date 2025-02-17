# python_ycash_sdk

A lightweight Python SDK for Ycash using the block explorer API at [https://explorer.ycash.xyz/](https://explorer.ycash.xyz/).

## Basic Usage

### get_status()

```python
from python_ycash_sdk.block_explorer_sdk import YcashBlockExplorerSDK

sdk = YcashBlockExplorerSDK()

status = sdk.get_status()
```

### get_blockchain_info

```python
from python_ycash_sdk.block_explorer_sdk import YcashBlockExplorerSDK

sdk = YcashBlockExplorerSDK()

blockchain_info = sdk.get_blockchain_info()
```

### get_block()

```python
from python_ycash_sdk.block_explorer_sdk import YcashBlockExplorerSDK

sdk = YcashBlockExplorerSDK()
block1 = sdk.get_block(1)
```

### get_balance_history()

```python
from python_ycash_sdk.block_explorer_sdk import YcashBlockExplorerSDK

sdk = YcashBlockExplorerSDK()
sdk.get_balance_history("s1P6ZAeyvokGh3MSxN3bLRk9r5EWdSd34Az")
```

### get_transaction()

```python
from python_ycash_sdk.block_explorer_sdk import YcashBlockExplorerSDK

sdk = YcashBlockExplorerSDK()
txid = "851bf6fbf7a976327817c738c489d7fa657752445430922d94c983c0b9ed4609"
tx_info = sdk.get_transaction(txid)
```

### get_utxos()

```python
from python_ycash_sdk.block_explorer_sdk import YcashBlockExplorerSDK

sdk = YcashBlockExplorerSDK()
utxos = sdk.get_utxos("s1P6ZAeyvokGh3MSxN3bLRk9r5EWdSd34Az")
```

