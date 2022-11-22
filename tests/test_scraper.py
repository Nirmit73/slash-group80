"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import scraper


def test_searchAmazon():
    """
    Checks the searchAmazon function
    """
    products = scraper.searchAmazon("Apple computer", True)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None
    products = scraper.searchAmazon("Apple Computer", True)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None


def test_searchWalmart():
    """
    Checks the searchWalmart function
    """
    products = scraper.searchWalmart("Apple computer", True)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None
    products = scraper.searchWalmart("Apple Computer", False)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None


def test_searchTarget():
    """
    Checks the searchTarget function
    """
    products = scraper.searchTarget("Apple computer", True)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None
    products = scraper.searchTarget("Apple Computer", False)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None


def test_searchBestBuy():
    """
    Checks the searchBestBuy function
    """
    products = scraper.searchBestBuy("Apple computer", True)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None
    products = scraper.searchBestBuy("Apple Computer", False)
    assert len(products) > 0
    for p in products:
        assert p["title"] is not None
        assert p["price"] is not None
