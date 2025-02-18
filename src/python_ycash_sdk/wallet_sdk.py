import hashlib
import base58
from ecdsa import SigningKey, SECP256k1
from Crypto.Hash import RIPEMD160
import secrets
from .block_explorer_sdk import YcashBlockExplorerSDK

sdk = YcashBlockExplorerSDK()


class Wallet:
    def __init__(self, wif=None):
        if wif:
            # Restore wallet from WIF
            self.private_key = self._wif_to_private_key(wif)
            self.entropy = None  # Entropy isn't available when restored from WIF
        else:
            # Generate a new wallet
            self.entropy = secrets.token_bytes(32)
            self.private_key = self.entropy.hex()

        # Derive public key from private key
        self.public_key = self._generate_public_key()

        # Generate transparent address
        self.address = self._generate_address()

        # Generate WIF (if not restored)
        self.wif = wif if wif else self._generate_wif()

    def _generate_public_key(self):
        """Derive the compressed public key from the private key."""
        private_key_bytes = bytes.fromhex(self.private_key)
        sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        vk = sk.verifying_key

        # Extract the full public key (X || Y)
        public_key_full = vk.to_string()  # 64 bytes: 32 bytes X + 32 bytes Y
        x_coord = public_key_full[:32]  # X coordinate (first 32 bytes)
        y_coord = public_key_full[32:]  # Y coordinate (last 32 bytes)

        # Correctly determine the prefix (0x02 if Y is even, 0x03 if Y is odd)
        prefix = b"\x02" if y_coord[-1] % 2 == 0 else b"\x03"

        # Return the compressed public key (33 bytes: 1-byte prefix + 32-byte X coordinate)
        return prefix + x_coord

    def _generate_address(self):
        """Generate the Ycash transparent address (starts with 's1')."""
        # Step 1: SHA-256 hash of the public key
        sha256_hash = hashlib.sha256(self.public_key).digest()

        # Step 2: RIPEMD-160 hash of the SHA-256 hash
        ripemd160 = RIPEMD160.new()
        ripemd160.update(sha256_hash)
        public_key_hash = ripemd160.digest()

        # Step 3: Add Ycash transparent address prefix (0x1C28)
        address_prefix = b"\x1C\x28"  # Ycash prefix for transparent addresses
        prefixed_key_hash = address_prefix + public_key_hash

        # Step 4: Compute checksum
        checksum = hashlib.sha256(hashlib.sha256(prefixed_key_hash).digest()).digest()[:4]

        # Step 5: Encode in Base58Check
        return base58.b58encode(prefixed_key_hash + checksum).decode()

    def _generate_wif(self):
        """Generate the Wallet Import Format (WIF) private key."""
        private_key_bytes = bytes.fromhex(self.private_key)
        wif_prefix = b"\x80"  # Ycash mainnet prefix
        prefixed_private_key = wif_prefix + private_key_bytes + b"\x01"  # Add compression flag
        checksum = hashlib.sha256(hashlib.sha256(prefixed_private_key).digest()).digest()[:4]
        return base58.b58encode(prefixed_private_key + checksum).decode()

    def _wif_to_private_key(self, wif):
        """Convert WIF to private key."""
        # Decode WIF from Base58Check
        decoded = base58.b58decode(wif)

        # Verify the prefix and checksum
        wif_prefix = decoded[:1]
        if wif_prefix != b"\x80":
            raise ValueError("Invalid WIF prefix for Ycash (expected 0x80)")

        checksum = decoded[-4:]
        data = decoded[:-4]
        expected_checksum = hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]
        if checksum != expected_checksum:
            raise ValueError("Invalid WIF checksum")

        # Extract private key (excluding prefix and compression flag)
        private_key = data[1:-1]
        return private_key.hex()

    def get_entropy(self):
        """Return entropy in hexadecimal format."""
        if self.entropy:
            return self.entropy.hex()
        return None

    def get_private_key(self):
        """Return private key in hexadecimal format."""
        return self.private_key

    def get_public_key(self):
        """Return the public key in compressed format."""
        return self.public_key.hex()

    def get_address(self):
        """Return the Ycash transparent address."""
        return self.address

    def get_wif(self):
        """Return the Wallet Import Format (WIF) private key."""
        return self.wif
    def get_utxos(self):
        utxos = sdk.get_utxos(self.address)
        return utxos


# Example Usage
if __name__ == "__main__":
    # Generate a new wallet
    new_wallet = Wallet()
    print("New Wallet:")
    print("Entropy (hex):", new_wallet.get_entropy())
    print("Private Key (hex):", new_wallet.get_private_key())
    print("Public Key (hex):", new_wallet.get_public_key())
    print("Ycash Transparent Address:", new_wallet.get_address())
    print("WIF Private Key:", new_wallet.get_wif())

    # Restore a wallet from WIF
    restored_wallet = Wallet(wif="L5289LNGcpPri4AVp9xHCCnkJDwDmhWiE4kzqGGCHjWhnYZof5sn")
    print("\nRestored Wallet:")
    print("Private Key (hex):", restored_wallet.get_private_key())
    print("Public Key (hex):", restored_wallet.get_public_key())
    print("Ycash Transparent Address:", restored_wallet.get_address())
    print("WIF Private Key:", restored_wallet.get_wif())
    UTXOS = restored_wallet.get_utxos()
    print("UTXOS:", UTXOS)
    UTXO_INFO = []
    for utxo in UTXOS:
        UTXO_INFO.append(sdk.get_transaction(utxo["txid"]))
    print("UTXO DETAILED:", UTXO_INFO)
