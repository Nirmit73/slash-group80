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
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/run")
def main():
    """
    Argument parser to capture command line and trigger the workflow
    """
    parser = argparse.ArgumentParser(description="Slash")
    parser.add_argument('--search', type=str, help='Product search query')
    parser.add_argument('--num',
                        type=int,
                        help="Maximum number of records",
                        default=3)
    parser.add_argument(
        '--sort',
        type=str,
        nargs='+',
        help=
        "Sort according to re (relevance: default), pr (price) or ra (rating) or all",
        default="re")
    parser.add_argument('--link',
                        action='store_true',
                        help="Show links in the table")
    parser.add_argument('--des',
                        action='store_true',
                        help="Sort in descending (non-increasing) order")
    parser.add_argument('--email',
                        type=str,
                        default="",
                        help="list of email to get notified")
    args = parser.parse_args()

    products1 = scraper.searchAmazon(args.search, args.link)
    products2 = scraper.searchWalmart(args.search, args.link)
    products3 = scraper.searchTarget(args.search, args.link)
    finalistList = []
    finalistList.append(
        formatter.sortList(products1, args.sort, args.des)[:args.num])
    finalistList.append(
        formatter.sortList(products2, args.sort, args.des)[:args.num])
    finalistList.append(
        formatter.sortList(products3, args.sort, args.des)[:args.num])
    mergedResults = email_utils.alternateMerge(finalistList)
    results = formatter.sortList(mergedResults, args.sort, args.des)

    print()
    print()
    print(tabulate(results, headers="keys", tablefmt="github"))
    print(
        "\nTrying to send email notification to the customers if there are any...\n"
    )
    email_utils.write_data(results, args.link, args.email)
    print("Done :)")
    print()
    print()


@app.route("/")
def hello():
    return render_template("UI.html")


if __name__ == '__main__':
    """
    Execution starts here.
    """
    app.run()
    #main()
