from setuptools import setup, find_packages

setup(
    name="python_ycash_sdk",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "ecdsa>=0.18.0",  # For ECDSA cryptography
        "base58>=2.1.0",  # For Base58 encoding
        "requests>=2.25.1",  # For HTTP requests,
        "pycryptodome>=3.20.0"
    ],
    python_requires=">=3.7",  # Specify the minimum Python version
)

