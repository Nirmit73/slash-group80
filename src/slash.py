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


def main(search_item, num_item, sort_item, order_item, email):
    order_des = False
    sort = 're'
    if order_item == "Descending":
        order_des = True

    if sort_item == "price":
        sort = 'pr'
    elif sort_item == "rating":
        sort = 'ra'
    
    #Default
    # default linkflag(args.link) == True
    products0 = scraper.searchAmazon(search_item, True)
    products1 = scraper.searchWalmart(search_item, True)
    products2 = scraper.searchTarget(search_item, True)
    products3 = scraper.searchBestBuy(search_item, True)
    # products4 = scraper.searcheBay(search_item, True)
    # products5 = scraper.searchCostCo(search_item, True)
    finalistList = []
    finalistList.append(
        formatter.sortList(products0, sort, order_des)[:num_item])
    finalistList.append(
        formatter.sortList(products1, sort, order_des)[:num_item])
    finalistList.append(
        formatter.sortList(products2, sort, order_des)[:num_item])
    finalistList.append(
        formatter.sortList(products3, sort, order_des)[:num_item])
    # finalistList.append(
    #     formatter.sortList(products4, sort, order_des)[:num_item])
    # finalistList.append(
    #     formatter.sortList(products5, sort, order_des)[:num_item])
    
    
    """
    #Threading:
    t0 = time.time()
    print(t0)
    finalistList = []
    
    thread = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searchAmazon(search_item, True), sort, order_des)[:num_item]), daemon=True)

    thread1 = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searchWalmart(search_item, True), sort, order_des)[:num_item]), daemon=True)

    thread2 = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searchTarget(search_item, True), sort, order_des)[:num_item]), daemon=True)

    #thread3 = threading.Thread(target=finalistList.append(
    #    formatter.sortList(scraper.searchBestBuy(search_item, True), sort, order_des)[:num_item]), daemon=True)

    thread4 = threading.Thread(target=finalistList.append(
        formatter.sortList(scraper.searcheBay(search_item, True), sort, order_des)[:num_item]), daemon=True)
    
    t1 = time.time()
    print(t1)
    print(t1-t0)   
    """
    
    """
    Concurrent Futures:

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit( finalistList.append(
        formatter.sortList(scraper.searchAmazon(search_item, True), sort, order_des)[:num_item]))     # default linkflag(args.link) == True
        executor.submit( finalistList.append(
        formatter.sortList(scraper.searchWalmart(search_item, True), sort, order_des)[:num_item]))
        executor.submit( finalistList.append(
        formatter.sortList(scraper.searchTarget(search_item, True), sort, order_des)[:num_item]))
        #executor.submit( finalistList.append(
        #formatter.sortList(scraper.searchCostCo(search_item, True), sort, order_des)[:num_item]))
    """
    
    
    mergedResults = email_utils.alternateMerge(finalistList)
    results = formatter.sortList(mergedResults, sort, order_des)

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
