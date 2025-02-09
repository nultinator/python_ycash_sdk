from python_ycash_sdk.block_explorer_sdk import YcashBlockExplorerSDK
import json

sdk = YcashBlockExplorerSDK()

def test_example():
    assert True  # This is a dummy test.

def test_get_status():
    status = sdk.get_status()

    test_dict = {'blockbook': {'coin': 'Ycash', 'host': 'ip-10-0-193-64', 'version': 'unknown', 'gitCommit': 'unknown', 'buildTime': 'unknown', 'syncMode': True, 'initialSync': False, 'inSync': True, 'bestHeight': 2360580, 'lastBlockTime': '2025-02-04T19:42:53.507984103-08:00', 'inSyncMempool': True, 'lastMempoolTime': '2025-02-04T19:43:53.706987655-08:00', 'mempoolSize': 0, 'decimals': 8, 'dbSize': 14492764567, 'about': 'Blockbook - blockchain indexer for Trezor wallet https://trezor.io/. Do not use for any other purpose.'}, 'backend': {'chain': 'main', 'blocks': 2360580, 'headers': 2360580, 'bestBlockHash': '000000b8822c9742789b9bdb7cea682803f505a5a171afe0ba49bfc11b257c54', 'difficulty': '194.6893455547126', 'sizeOnDisk': 24941327539, 'version': '4040450', 'subversion': '/YcashCpp:4.4.4/', 'protocolVersion': '270013', 'consensus': {'chaintip': '19bd2d2f', 'nextblock': '19bd2d2f'}}}
    assert status.keys() == test_dict.keys()

def test_get_blockchain_info():
    blockchain_info = sdk.get_blockchain_info()

    test_dict = {
        'blockbook': {
                'coin': 'Ycash', 
                'host': 'ip-10-0-193-64', 
                'version': 'unknown', 
                'gitCommit': 'unknown', 
                'buildTime': 'unknown', 
                'syncMode': True, 
                'initialSync': False, 
                'inSync': True, 
                'bestHeight': 2360568, 
                'lastBlockTime': '2025-02-04T19:18:29.357167761-08:00', 
                'inSyncMempool': True, 
                'lastMempoolTime': '2025-02-04T19:20:29.726731608-08:00', 
                'mempoolSize': 0, 
                'decimals': 8, 
                'dbSize': 14484358622, 
                'about': 'Blockbook - blockchain indexer for Trezor wallet https://trezor.io/. Do not use for any other purpose.'
            }, 
        'backend': {
                'chain': 'main', 
                'blocks': 2360568, 
                'headers': 2360568, 
                'bestBlockHash': '00000920e3c52a3e665ecdc36d1f1f6e08fd1b22fbeb69991a143c9a8d59addd', 
                'difficulty': '223.1631705662486', 
                'sizeOnDisk': 24941316249, 
                'version': '4040450', 
                'subversion': '/YcashCpp:4.4.4/', 
                'protocolVersion': '270013', 
                'consensus': {
                    'chaintip': '19bd2d2f', 
                    'nextblock': '19bd2d2f'
                    }
            }
        }
    assert blockchain_info.keys() == test_dict.keys()

def test_get_block():
    block1 = sdk.get_block(1)

    test_dict = {
        'page': 1, 
        'totalPages': 1, 
        'itemsOnPage': 1000, 
        'hash': '0007bc227e1c57a4a70e237cad00e7b7ce565155ab49166bc57397a26d339283', 
        'previousBlockHash': '00040fe8ec8471911baa1db1266ea15dd06b4a8a5c453883c000b031973dce08', 
        'nextBlockHash': '0002a26c902619fc964443264feb16f1e3e2d71322fc53dcb81cc5d797e273ed', 
        'height': 1, 
        'confirmations': 2360572, 
        'size': 1617, 
        'time': 1477671596, 
        'version': 4, 
        'merkleRoot': '851bf6fbf7a976327817c738c489d7fa657752445430922d94c983c0b9ed4609', 
        'nonce': '9057977ea6d4ae867decc96359fcf2db8cdebcbfb3bd549de4f21f16cfe83475', 
        'bits': '1f07ffff', 
        'difficulty': '1', 
        'txCount': 1, 
        'txs': [
            {
                'txid': '851bf6fbf7a976327817c738c489d7fa657752445430922d94c983c0b9ed4609', 
                'version': 1,
                'vin': [{'sequence': 4294967295, 'n': 0, 'isAddress': False, 'coinbase': '5100'}], 
                'vout': [{'value': '50000', 'n': 0, 'spent': True, 'hex': '21027a46eb513588b01b37ea24303f4b628afd12cc20df789fede0921e43cad3e875ac', 'addresses': ['s1PD2bs588FatoEWRsgeurkefmYFP4To9Hb'], 'isAddress': True}, {'value': '12500', 'n': 1, 'spent': True, 'hex': 'a9147d46a730d31f97b1930d3368a967c309bd4d136a87', 'addresses': ['s39yZGB6K2s9ZjPR7TGFhk4niP5yEsdN47P'], 'isAddress': True}],
                'blockHash': '0007bc227e1c57a4a70e237cad00e7b7ce565155ab49166bc57397a26d339283', 
                'blockHeight': 1, 
                'confirmations': 2360572, 
                'blockTime': 1477671596, 
                'value': '62500', 
                'valueIn': '0', 
                'valueBalanceZat': '0', 
                'fees': '0', 
                'hex': '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff025100ffffffff0250c30000000000002321027a46eb513588b01b37ea24303f4b628afd12cc20df789fede0921e43cad3e875acd43000000000000017a9147d46a730d31f97b1930d3368a967c309bd4d136a8700000000'
            }
            ]
        }
    assert block1["hash"] == '0007bc227e1c57a4a70e237cad00e7b7ce565155ab49166bc57397a26d339283'
    assert block1.keys() == test_dict.keys()

def test_get_balance_history():
    tx_model = {'time': 1572217200, 'txs': 1, 'received': '1038435', 'sent': '0', 'sentToSelf': '0'}
    address_history = sdk.get_balance_history("s1P6ZAeyvokGh3MSxN3bLRk9r5EWdSd34Az")
    if len(address_history) > 0:
        for tx in address_history:
            assert tx.keys() == tx_model.keys()

def test_get_transaction():
    txid = "851bf6fbf7a976327817c738c489d7fa657752445430922d94c983c0b9ed4609"

    test_dict = {'txid': '851bf6fbf7a976327817c738c489d7fa657752445430922d94c983c0b9ed4609', 'version': 1, 'vin': [{'sequence': 4294967295, 'n': 0, 'isAddress': False, 'coinbase': '5100'}], 'vout': [{'value': '50000', 'n': 0, 'spent': True, 'hex': '21027a46eb513588b01b37ea24303f4b628afd12cc20df789fede0921e43cad3e875ac', 'addresses': ['s1PD2bs588FatoEWRsgeurkefmYFP4To9Hb'], 'isAddress': True}, {'value': '12500', 'n': 1, 'spent': True, 'hex': 'a9147d46a730d31f97b1930d3368a967c309bd4d136a87', 'addresses': ['s39yZGB6K2s9ZjPR7TGFhk4niP5yEsdN47P'], 'isAddress': True}], 'blockHash': '0007bc227e1c57a4a70e237cad00e7b7ce565155ab49166bc57397a26d339283', 'blockHeight': 1, 'confirmations': 2360575, 'blockTime': 1477671596, 'value': '62500', 'valueIn': '0', 'valueBalanceZat': '0', 'fees': '0', 'hex': '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff025100ffffffff0250c30000000000002321027a46eb513588b01b37ea24303f4b628afd12cc20df789fede0921e43cad3e875acd43000000000000017a9147d46a730d31f97b1930d3368a967c309bd4d136a8700000000'}
    tx_info = sdk.get_transaction(txid)
    assert tx_info.keys() == test_dict.keys()

def test_get_utxos():
    utxos = sdk.get_utxos("s1P6ZAeyvokGh3MSxN3bLRk9r5EWdSd34Az")

    test_dict = {'txid': 'b4bb8ca779ee53b81fe3cde85db71b7cc6456ba1fbcd37951982dcd3ee2fb6b1', 'vout': 0, 'value': '300000000000', 'height': 1694558, 'confirmations': 666026}

    if utxos:
        for utxo in utxos:
            assert utxo.keys() == test_dict.keys()
