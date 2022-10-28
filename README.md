**This is a cloned project of `https://github.com/vishnuchalla/slash`**

<p align="center"><img width="500" src="./assets/slash.png"></p>

**Shopping Made Easy**

![GitHub](https://img.shields.io/github/license/vishnuchalla/slash)
![github workflow](https://github.com/secheaper/cheaper/actions/workflows/python-app.yml/badge.svg) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7158813.svg)](https://doi.org/10.5281/zenodo.7158813)
![Github](https://img.shields.io/badge/language-python-red.svg)
![GitHub issues](https://img.shields.io/github/issues-raw/vishnuchalla/slash)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/vishnuchalla/slash)
![Github pull requests](https://img.shields.io/github/issues-pr/vishnuchalla/slash)
![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/vishnuchalla/slash)
[![codecov](https://codecov.io/gh/vishnuchalla/slash/branch/main/graph/badge.svg?token=VO0F809CJT)](https://codecov.io/gh/vishnuchalla/slash)

Slash is a command line tool that scrapes the most popular e-commerce websites to get the best deals on the searched items across these websites. 
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash uses very easy commands to filter, sort and search your items
- **Powerful**: Quickly alter the commands to get desired results
- **Informative**: Provides the information about items through an email with attached csv file

<ul align="left">
  <li> <a href="#rocket-installation">Installation</a> </li>
  
  <li> <a href="#golf-flags-and-command-line-arguments">Flags & Args</a> </li>
  
  <li><a href="#card_index_dividers-some-examples">Examples</a></li>
  
  <li><a href="#thought_balloon-use-case">Use Case</a></li>
  
  <li><a href="#page_facing_up-why">Why</a></li>
  
  <li><a href="#sparkles-contributors">Contributors</a></li>
  
  <li><a href="#email-support">Support</a></li>
  
</ul>

---

<p align="center"><img width="700" src="./assets/DemoGif.gif"></p>

---

:rocket: Installation
---
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/vishnuchalla/slash
cd slash
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
3. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the python command to run the ```slash.py``` file.
```
cd src

For Mac
python3 slash.py --search icecream

For Windows
python slash.py --search icecream
```
:golf: Flags and Command Line Arguments
---
Currently the tool supports the following flags and command line arguments. These flags and arguments can be used to quickly filter and guide the search to get you the best results very quickly.

| Arguments | Type | Default | Description                                                          |
|-----------|------|---------|----------------------------------------------------------------------|
| --search  | str  | None    | The product name to be used as the search query                      |
| --num     | int  | 3       | Maximum number of products to search                                 |
| --sort    | str  | re      | Sort results by relevance (re), by price (pr), by rating (ra) or by all the features using "all" this sorts in the order of price and ratings in the respective order|
| --des     | bool | True      | Set boolean flag if results should be sorted in non-increasing order, the default value is true |
| --email   | str  | "" (empty string) | list of comma separated emails to send notifications |

:card_index_dividers: Some Examples
---

#### 1. Searching
```--search```  accepts one argument string which it uses to search and scrape the requested products on 
the e-commerce websites. So, to use this, run the python script followed by the --search argument and the 
search string. The search string should be in double quotes if it have two or more words. Example:
```
For Mac
python3 slash.py --search "philips hue"

For Windows
python slash.py --search "philips hue"
```
```
| timestamp                     | title                                       | price      | website   | rating   |
|-------------------------------|---------------------------------------------|------------|-----------|----------|
| 01/10/2022 13:56:08 EDT -0400 | Amazon Basics 60W Equivalent, Soft White... | $14.99     | amazon    | 4.6      |
| 01/10/2022 13:56:08 EDT -0400 | Philips Hue White & Color Ambiance White... | $119.99    | amazon    | 4.7      |
| 01/10/2022 13:56:08 EDT -0400 | PHILIPS Hue 2pk A19 LED Starter Kit with... | $69.99     | amazon    | 4.7      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue Smart Stand Alone Bridge, Hu... | $49.68     | walmart   | N.A      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue 3-Pack 60W White Bluetooth S... | $69.00     | walmart   | N.A      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue LED 60-Watt White A19 Dimmab... | $52.99     | walmart   | N.A      |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue A19 75W Smart LED Bulb White    | $15.99     | target    | 4.44     |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue 4pk White and Color Ambiance... | $199.99    | target    | 4.63     |
| 01/10/2022 13:56:10 EDT -0400 | Philips Hue A19 75W Smart LED Bulb          | $54.99     | target    | 4.3      |
```
#### 2. Sorting
```--sort``` accepts one or more arguments that determine how the tool sorts and filters the requested products
after scraping. The first value is used to initially sort and filter the results of the scraping. The arguments
following the first one are not required but will be used to further sort the filtered results. Example:
```
For Mac
python3 slash.py --search "philips hue" --sort pr

For Windows
python slash.py --search "philips hue" --sort pr
```
```
| timestamp                     | title                                       | price      | website   | rating   |
|-------------------------------|---------------------------------------------|------------|-----------|----------|
| 01/10/2022 13:57:59 EDT -0400 | Philips Hue Econic Outdoor White & Color... | N.A        | amazon    | 4.8      |
| 01/10/2022 13:57:59 EDT -0400 | Amazon Basics 60W Equivalent, Soft White... | $14.99     | amazon    | 4.6      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue A19 75W Smart LED Bulb White    | $15.99     | target    | 4.44     |
| 01/10/2022 13:57:59 EDT -0400 | Outdoor Low voltage Extension Cable for ... | $19.98     | amazon    | 4.7      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue White Ambiance A19 LED 60-Wa... | $21.88     | walmart   | N.A      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue White Ambiance A19 LED 60-Wa... | $21.97     | walmart   | N.A      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue White and Color Ambiance Blu... | $39.99     | target    | 3.42     |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue Smart Stand Alone Bridge, Hu... | $49.68     | walmart   | N.A      |
| 01/10/2022 13:58:01 EDT -0400 | Philips Hue 2pk BR30 Warm-To-Cool LED Sm... | $49.99     | target    | 4.73     |
```
#### 3. Sort Order
The ```--des``` flag can be set to sort the requested products in a non-increasing order. This flag will be 
actually used when coupled with ```--sort``` and the default value taken is true. Example:
```
For Mac
python3 slash.py --search "philips hue" --sort pr --des

For Windows
python slash.py --search "philips hue" --sort pr --des
```
```
| timestamp                     | title                                       | price   | website   | rating   |
|-------------------------------|---------------------------------------------|---------|-----------|----------|
| 01/10/2022 13:59:09 EDT -0400 | 75" Gradient TV Lightstrip Entertainment... | $541.77 | amazon    | 4.3      |
| 01/10/2022 13:59:09 EDT -0400 | Philips Hue 2-Pack Bluetooth Gradient Am... | $324.99 | amazon    | N.A      |
| 01/10/2022 13:59:09 EDT -0400 | Philips Hue White and Color Ambiance Ext... | $323.95 | amazon    | N.A      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White and Color Ambiance A19... | $199.99 | walmart   | N.A      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue 4pk White and Color Ambiance... | $199.99 | target    | 4.63     |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White &#38; Color Ambiance D... | $179.99 | target    | 3.7      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue 4-Pack White and Color A19 M... | $159.99 | walmart   | N.A      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White & Color Ambiance Calla... | $149.99 | target    | 5.0      |
| 01/10/2022 13:59:11 EDT -0400 | Philips Hue White A19 Smart Light Starte... | $81.86  | walmart   | N.A      |
```

#### 4. Result length
The maximum number of results that are scraped from each website can be set using the ```--num``` argument. It accepts
an integer value ```n``` and then returns ```n``` results from each website. Note that tool returns a maximum of 
the value of ```n``` and the number of results on the webiste. By default this value is set to 3. Example:
```
For Mac
python3 slash.py --search "philips hue" --num 5

For Windows
python slash.py --search "philips hue" --num 5
```
```
| timestamp                     | title                                       | price      | website   | rating   |
|-------------------------------|---------------------------------------------|------------|-----------|----------|
| 01/10/2022 13:59:54 EDT -0400 | Amazon Basics 60W Equivalent, Soft White... | $14.99     | amazon    | 4.6      |
| 01/10/2022 13:59:54 EDT -0400 | Philips Hue White & Color Ambiance White... | $119.99    | amazon    | 4.7      |
| 01/10/2022 13:59:54 EDT -0400 | PHILIPS Hue 2pk A19 LED Starter Kit with... | $69.99     | amazon    | 4.7      |
| 01/10/2022 13:59:54 EDT -0400 | Philips Hue White Filament Globe G25 LED... | $32.94     | amazon    | 4.7      |
| 01/10/2022 13:59:54 EDT -0400 | Philips Hue White and Color Ambiance A19... | $99.99     | amazon    | 4.7      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue Smart Stand Alone Bridge, Hu... | $49.68     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue 3-Pack 60W White Bluetooth S... | $69.00     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue LED 60-Watt White A19 Dimmab... | $52.99     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue White A19 Smart Light Starte... | $81.86     | walmart   | N.A      |
| 01/10/2022 13:59:56 EDT -0400 | Philips Hue White and Color Ambiance Sma... | $69.99     | walmart   | N.A      |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue A19 75W Smart LED Bulb White    | $15.99     | target    | 4.44     |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue 4pk White and Color Ambiance... | $199.99    | target    | 4.63     |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue A19 75W Smart LED Bulb          | $54.99     | target    | 4.3      |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue 2pk A19 LED Starter Kit with... | $69.99     | target    | 4.35     |
| 01/10/2022 13:59:57 EDT -0400 | Philips Hue White &#38; Color Ambiance D... | $179.99    | target    | 3.7      |
```

#### 5. Link
There is an option to display links int the output. Example:
```
For Mac
python3 slash.py --search "philips hue" --link

For Windows
python slash.py --search "philips hue" --link
```
```
| timestamp                     | title                                       | price   | website   |   rating | link                         |
|-------------------------------|---------------------------------------------|---------|-----------|----------|------------------------------|
| 07/10/2022 16:57:17 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2hf4nm8l |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:17 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2hf4nm8l |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:18 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2qjv6k8w |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Solid Crew Soc... | $7.79   | target    |     4.71 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:18 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2qjv6k8w |
| 07/10/2022 16:57:35 EDT -0400 | Pair of Thieves Men&#39;s Solid Crew Soc... | $7.79   | target    |     4.71 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:57:18 EDT -0400 | No Show Socks Women Low Socks Non Slip F... | $15.89  | amazon    |     4.5  | https://tinyurl.com/2khadfy2 |
| 07/10/2022 16:57:35 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |
| 07/10/2022 16:57:18 EDT -0400 | No Show Socks Women Low Socks Non Slip F... | $15.89  | amazon    |     4.5  | https://tinyurl.com/2khadfy2 |
| 07/10/2022 16:57:35 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |

Trying to send email notification to the customers if there are any...

No email to send data. Hence not sending the email
Done :)
```

#### 6. Email Notification
There is an option to send emails to customers using a parameter that accepts a comma separated list of emails. Example:
```
For Mac
python3 slash.py --search "philips hue" --link --email "vchalla2@ncsu.edu,sponnur@ncsu.edu"

For Windows
python slash.py --search "philips hue" --link --email "vchalla2@ncsu.edu,sponnur@ncsu.edu"
```
```
| timestamp                     | title                                       | price   | website   |   rating | link                         |
|-------------------------------|---------------------------------------------|---------|-----------|----------|------------------------------|
| 07/10/2022 16:47:58 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2outdp6f |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:58 EDT -0400 | mens Performance Cotton Cushioned Athlet... | $13.50  | amazon    |     4.5  | https://tinyurl.com/2outdp6f |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $3.59   | target    |     4.79 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:58 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2dsl5uyc |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $8.99   | target    |     4.65 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:58 EDT -0400 | Mens Socks, 6 Pairs Anti-Blister Cushion... | $15.99  | amazon    |     4.6  | https://tinyurl.com/2dsl5uyc |
| 07/10/2022 16:48:15 EDT -0400 | Pair of Thieves Men&#39;s Cushion Crew S... | $8.99   | target    |     4.65 | https://tinyurl.com/2o5fx6az |
| 07/10/2022 16:47:59 EDT -0400 | CelerSport Ankle Athletic Running Socks ... | $15.95  | amazon    |     4.7  | https://tinyurl.com/2en2jbsd |
| 07/10/2022 16:48:15 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |
| 07/10/2022 16:47:59 EDT -0400 | CelerSport Ankle Athletic Running Socks ... | $15.95  | amazon    |     4.7  | https://tinyurl.com/2en2jbsd |
| 07/10/2022 16:48:15 EDT -0400 | Signature Gold by GOLDTOE Men&#39;s Mode... | $9.35   | target    |     4.67 | https://tinyurl.com/2m5ec5nt |

Trying to send email notification to the customers if there are any...

Done :)
```

:thought_balloon: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually inportant.
* ***Customers***: Can be used by customers to simply query for the items and get a email on the details.

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for people who have some understanding of python and are comfortable in using the command line interface to interact with systems.
- Future updates aim to encompass a wide variety of users irrespective of their computer knowledge and background.

:open_file_folder: Document Generated
---
To have a better understanding of the code, please click on the [link](https://sumanthbsundar.github.io/slash_doc/) provided below.

[Github Pages](https://sumanthbsundar.github.io/slash_doc/)


:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/srujanponnur">Srujan Ponnur</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/sumanth-somasundar">Sumanth Somasundar</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/vishnuchalla/">Vishnu Challa</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/svnsairam/">Sairam Sakhamuri</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/kanchan-rawat-793753a2/">Kanchan Rawat</a></td>
  </tr>
</table>

:email: Support
---

For any queries and help, please reach out to us at: vchalla2@ncsu.edu
