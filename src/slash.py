"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import argparse
import scraper
import formatter
import email_utils
from tabulate import tabulate
import browser
import time
import threading
import concurrent.futures
from multiprocessing.dummy import Pool as ThreadPool
import itertools


def main(search_item, num_item, sort_item, order_item, email):
    order_des = False
    sort = 're'
    if order_item == "Descending":
        order_des = True

    if sort_item == "price":
        sort = 'pr'
    elif sort_item == "rating":
        sort = 'ra'
    # """
    # Default
    # default linkflag(args.link) == True
    timeInitDefault = time.time()

    products_amazon = scraper.searchAmazon(search_item, True)
    products_walmart = scraper.searchWalmart(search_item, True)
    products_target = scraper.searchTarget(search_item, True)
    products_ebay = scraper.searcheBay(search_item, True)
    products_costco = scraper.searchCostCo(search_item, True)
    finalistList = []
    finalistList.append(
        formatter.sortList(products_amazon, sort, order_des)[:num_item])
    finalistList.append(
        formatter.sortList(products_walmart, sort, order_des)[:num_item])
    finalistList.append(
        formatter.sortList(products_target, sort, order_des)[:num_item])
    finalistList.append(
        formatter.sortList(products_ebay, sort, order_des)[:num_item])
    finalistList.append(
        formatter.sortList(products_costco, sort, order_des)[:num_item])

    timeDiffDefault = time.time() - timeInitDefault
    # """
    """
    # Threading:
    timeInitThreading = time.time()
    finalistList = []

    thread_amazon = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searchAmazon(search_item, True), sort, order_des)[:num_item]), daemon=True)

    thread_walmart = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searchWalmart(search_item, True), sort, order_des)[:num_item]), daemon=True)

    thread_target = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searchTarget(search_item, True), sort, order_des)[:num_item]), daemon=True)

    thread_ebay = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searcheBay(search_item, True), sort, order_des)[:num_item]), daemon=True)

    thread_costco = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searchCostCo(search_item, True), sort, order_des)[:num_item]), daemon=True)

    timeDiffThreading = time.time() - timeInitThreading

    """
    """
    # Concurrent Futures:

    timeInitFutures = time.time()
    finalistList = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(finalistList.append(
            formatter.sortList(scraper.searchAmazon(search_item, True), sort, order_des)[:num_item]))     # default linkflag(args.link) == True
        executor.submit(finalistList.append(
            formatter.sortList(scraper.searchWalmart(search_item, True), sort, order_des)[:num_item]))
        executor.submit(finalistList.append(
            formatter.sortList(scraper.searchTarget(search_item, True), sort, order_des)[:num_item]))
        executor.submit(finalistList.append(
            formatter.sortList(scraper.searchCostCo(search_item, True), sort, order_des)[:num_item]))
        executor.submit(finalistList.append(
            formatter.sortList(scraper.searcheBay(search_item, True), sort, order_des)[:num_item]))

    timeDiffFutures = time.time() - timeInitFutures

    """
    """
    # Pool:

    timeInitPool = time.time()
    finalistList = []

    stores = ['amazon', 'walmart', 'target', 'costco', 'ebay']
    pool = ThreadPool(len(stores))
    results = pool.starmap(scraper.searchStore,
                           zip(stores, itertools.repeat(search_item), itertools.repeat(True)))
    for x in range(0, len(results)):
        finalistList.append(results[x][:num_item])

    timeDiffPool = time.time() - timeInitPool
    """
    mergedResults = email_utils.alternateMerge(finalistList)
    results = formatter.sortList(mergedResults, sort, order_des)

    print(f"Default: {timeDiffDefault}")
    #print(f"Threading: {timeDiffThreading}")
    #print(f"Concurrent Futures: {timeDiffFutures}")
    #print(f"Pool: {timeDiffPool}")
    print()
    print()
    print(tabulate(results, headers="keys", tablefmt="github"))
    print(
        "\nTrying to send email notification to the customers if there are any...\n"
    )
    email_utils.write_data(results, True, email)
    print("Done :)")
    print()
    print()

    return results


if __name__ == "__main__":
    main("Apple Computer", 10, "relevance", "Ascending", "")
