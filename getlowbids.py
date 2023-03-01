import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import copy


prices = None
priceList = []
totalLOW = None

# low bids -----------------------------------------------------
with open("lowbids.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    price = [text for text in soup.stripped_strings]

    # print(len(price))
    # print(type(price))
    # print(price)

    print("------------------------------")

    for i in range(len(price)):

        try:
            if price[i] == "," or price[i] == "[" or price[i] == "]": 
                del price[i]
        except IndexError:
            pass
    

    # print(len(price))
    # print(type(price))
    # print(price)

    print("------------------------------")


    for i in range(len(price)):

        price[i] = int(re.sub("[$,]", "", price[i]))
        # print(type(price[i]))

    # print(len(price))
    # print(type(price))
    # print(price)


# print(len(price))
# print(type(price))
# print(price)

totalLOW = sum(price)
print(totalLOW)

