import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import copy
from fillSheet import *
import getotherbids as getother
import getlowbids as glow



load_dotenv()  # take environment variables from .env.

f = fillSheet(r'C:\Users\des11\OneDrive\Desktop\cisleads-Scraping-data\Perfetto Bid History Template.xlsx', "Competitor Analysis")
nameList = f.getNamesList()

for x in range(1, len(nameList)):
    driver = start_firefox("https://cisleads.com/?login=1", headless=False)
    
    # login
    write(os.getenv("UN"), into="email:")
    write(os.getenv("PW"), into="password:")
    click(S("#buttonLogin"))
    
    
    # fill out form
    click(S("//html/body/section/div[2]/div[3]/div[1]/form/div[1]/a[2]"))
    write(nameList[x], into=S("#Keywords"))
    
    time.sleep(1)
    click(nameList[x])
    
    # click print
    click("Print")
    
    time.sleep(1)
    
    # save html
    html = driver.page_source
    print(html)
    
    # end
    kill_browser()
    print("done helium")
    
    
    #   ----
    
    soup = BeautifulSoup(html, "html.parser")
    
    getTables = soup.find_all("table")
    Tables = [getTables[2], getTables[3]]
    
    print(f"getTables len is {len(getTables)}")
    print(f"Tables len is {len(Tables)}")
    
    with open("lowbids.html", "w") as f:
        data = str(Tables[0])
        f.write(data)
    
    with open("otherbids.html", "w") as f:
        data = str(Tables[1])
        f.write(data)
    
    # get prices
    prices = []
    
    with open("otherbids.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        prices.append(soup.find_all("td", class_="locbid-cell"))
    
    with open("lowbids.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        prices.append(soup.find_all("td", class_="locbid-cell"))
    
    print(f"prices len is {len(prices)}")
    
    with open("lowbids.html", "w") as f:
        f.write(str(prices[0]))
    
    with open("otherbids.html", "w") as f:
        f.write(str(prices[1]))
    
    # grab prices
    
    with open("otherbids.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        prices[0] = soup.find_all("strong")
    
    with open("lowbids.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        prices[1] = soup.find_all("strong")
    
    with open("lowbids.html", "w") as f:
        f.write(str(prices[0]))
    
    with open("otherbids.html", "w") as f:
        f.write(str(prices[1]))
    
    
    # ---
    
    getother.get()
    glow.get()