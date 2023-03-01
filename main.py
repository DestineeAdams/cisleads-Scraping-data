import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import copy

compname = "JRCRUZ Corp"

load_dotenv()  # take environment variables from .env.


url = "https://cisleads.com/?login=1"

# driver = start_firefox(url, headless=False)
driver = start_firefox(url, headless=True)

# time.sleep(1)


# login
write(os.getenv("UN"), into="email:")
write(os.getenv("PW"), into="password:")
click(S("#buttonLogin"))


# fill out form
click(S("//html/body/section/div[2]/div[3]/div[1]/form/div[1]/a[2]"))
write(compname, into=S("#Keywords"))
click(compname)

# # click low bid
# click("low Bids")

# click print
click("Print")

time.sleep(3)

# grab tables
# lowbids_cells = find_all(Text(S("td", below="Other Bids", above="Location/Bid")).value)
# lowbids_cells = find_all(Text("$").value)
# lowbids_cells = Text(to_right_of="2/21/23").value

# print(len(lowbids_cells))
# print(lowbids_cells)


# save html
html = driver.page_source
# print(html)

print("done helium")

kill_browser()


# _____________________________________________________


soup = BeautifulSoup(html, 'html.parser')
# print(soup)

getTables = soup.find_all("table")
print(f'getTables len is {len(getTables)}')

Tables = [getTables[2], getTables[3]] 

print(f'Tables len is {len(Tables)}')


with open('lowbids.html', 'w') as f:
    data = str(Tables[0])
    f.write(data)

with open('otherbids.html', 'w') as f:
    data = str(Tables[1])
    f.write(data)


# get prices
prices = []


with open("otherbids.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    prices.append(soup.find_all("td", class_="locbid-cell"))


with open("lowbids.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    prices.append(soup.find_all("td", class_="locbid-cell"))

print(f'prices len is {len(prices)}')


with open('lowbids.html', 'w') as f:
    f.write(str(prices[0]))

with open('otherbids.html', 'w') as f:
    f.write(str(prices[1]))



# grab prices

with open("otherbids.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    prices[0] = soup.find_all("strong")


with open("lowbids.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    prices[1] = soup.find_all("strong")


with open('lowbids.html', 'w') as f:
    f.write(str(prices[0]))

with open('otherbids.html', 'w') as f:
    f.write(str(prices[1]))

