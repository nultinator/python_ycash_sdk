from setuptools import setup, find_packages

setup(
    name="python_ycash_sdk",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
