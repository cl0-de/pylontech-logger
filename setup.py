from setuptools import setup, find_packages

requiredPackages = [#should only contain third party pakages
    "coloredlogs",
    "pyserial",
    "construct",
    "python-pylontech"
],

setup(
    name="Python logger for pylontech batteries",
    version="0.1",
    author="cl0-de",
    author_email="",
    install_requires = requiredPackages,
    packages = [],
)