# coding: utf-8

"""
    GMO Aozora Net Bank Oepn API SDK

    OpenAPI spec version: 1.0.0

    Create By GMO Aozora Net Bank
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "gmo-aozora-net-bank"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "PyJWT"]

setup(
    name=NAME,
    version=VERSION,
    description="GMO Aozora Net Bank Oepn API",
    author_email="",
    url="",
    keywords=["GMO Aozora Net Bank Oepn API SDK", "oauth", "openid"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)
