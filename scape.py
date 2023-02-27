import os, time, sys
import pandas as pd
from playwright.sync_api import sync_playwright 
from dotenv import load_dotenv
from fillSheet import *
from bs4 import BeautifulSoup as bs

load_dotenv()  # take environment variables from .env.

# the vars will be passed in by the user later
gcn = fillSheet('Perfetto Bid History Template.xlsx', "Competitor Analysis")

lowbidsValues = []
otherbidsValues = []



def getvalues(ItemsTotal):

    tablehtml = page.inner_html("xpath=/html/body/section/div[3]/div[2]/div[2]/div/table")
    soup = bs(tablehtml, "html.parser")
    rows = soup.find_all('strong')

    print(len(rows))

    for row in rows:
      dic = {}
      dic["amount"] = row.get_text()

      lowbidsValues.append(dic)
      

    print(lowbidsValues)
    return lowbidsValues



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    # browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    # login page nav
    page.goto("https://cisleads.com/?login=1")

    # login
    page.fill('input#UserName',  os.getenv("UN"))
    page.fill('input#Password',  os.getenv("PW"))
    page.click('#buttonLogin')
    time.sleep(2) # don't touch this /desktop needs time to load

    # fill out search form
    page.goto("https://cisleads.com/desktop")
    page.get_by_title('GCs & Subs').click()

    companyNamesList = gcn.getNamesList()
    page.fill('input#Keywords', companyNamesList[2])
    page.locator("xpath=/html/body/section/div[2]/div[3]/div[1]/form/div[2]/div/ul/div/p/a").click()

    # get to company
    page.locator(".column-name").locator("text=JRCRUZ Corp").click()
    print("done")

    time.sleep(1)
    

    # get to low bids
    page.locator("text=Low Bids").click()

    time.sleep(2)

    # max out results show
    page.locator("span.num-page").locator("a").last.click()
    
    TotalItems = int(page.locator("span.number-total").first.text_content())
    print(TotalItems)

    getvalues(TotalItems)


    # # page.keyboard.press("Control+KeyR")
    # time.sleep(1)

    # # click on company profile
    # page.locator("text=Company Profile").last.click()

    # # get to other bids
    # page.locator("text=Other Bids").click()

    # numberOfOtherBids = int(page.locator("span.number-total").last.text_content())
    # print(numberOfOtherBids)



    # time.sleep(1)

  
    time.sleep(5)
    


print(sum(lowbidsValues))