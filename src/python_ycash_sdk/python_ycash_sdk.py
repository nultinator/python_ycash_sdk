import requests
import json

class YcashBlockExplorerSDK:
    ###RAW JSON RESPONSES###
    def __init__(self, api_base_url="https://explorer.ycash.xyz"):
        """
        Initialize the SDK with the Blockbook API base URL.
        """
        self.api_base_url = api_base_url.rstrip('/')

    def _make_request(self, endpoint, params=None):
        """
        Internal method to make GET requests to the Blockbook API.
        """
        try:
            url = f"{self.api_base_url}/{endpoint}"
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

    def get_block(self, block_hash_or_height):#
        """
        Get details of a block by hash or height.
        """
        return self._make_request(f"api/v2/block/{block_hash_or_height}")

    def get_balance_history(self, address):#
        """
        Get balance history of an address
        """
        return self._make_request(f"api/v2/balancehistory/{address}")

    def get_transaction(self, tx_id):#
        """
        Get details of a transaction by its ID.
        """
        return self._make_request(f"api/v2/tx/{tx_id}")

    def get_address(self, address):#
        """
        Get details of an address, including balance and transaction history.
        """
        return self._make_request(f"api/v2/address/{address}")

    def get_status(self):#
        """
        Get the current status of the Blockbook server.
        """
        return self._make_request("api/v2")

    def get_blockchain_info(self):#
        """
        Get general information about the blockchain.
        """
        return self._make_request("api/v2/info")

    def get_utxos(self, address):
        """
        Get unspent transaction outputs (UTXOs) for an address.
        """
        return self._make_request(f"api/v2/utxo/{address}")

    def estimate_fee(self, blocks):
        """
        Estimate the transaction fee for the given number of blocks.
        """
        return self._make_request(f"api/v2/estimatefee/{blocks}")

    


# Example usage
if __name__ == "__main__":
    # Replace with your Blockbook API base URL
    api_base_url = "https://explorer.ycash.xyz"
    sdk = YcashBlockExplorerSDK(api_base_url)

    try:
        utxos = sdk.get_utxos("s1P6ZAeyvokGh3MSxN3bLRk9r5EWdSd34Az")
        print(utxos)

    except RuntimeError as e:
        print(e)
