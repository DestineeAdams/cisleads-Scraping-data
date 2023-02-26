import os, time
from playwright.sync_api import sync_playwright 
from dotenv import load_dotenv
from fillSheet import *

load_dotenv()  # take environment variables from .env.

# the vars will be passed in by the user later
gcn = fillSheet('Perfetto Bid History Template.xlsx', "Competitor Analysis")



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    # login page nav
    page.goto("https://cisleads.com/?login=1")

    # login
    page.fill('input#UserName',  os.getenv("UN"))
    page.fill('input#Password',  os.getenv("PW"))
    page.click('#buttonLogin')
    time.sleep(2)

    # fill out search form
    page.goto("https://cisleads.com/desktop")
    page.get_by_title('GCs & Subs').click()

    companyNamesList = gcn.getNamesList()
    page.fill('input#Keywords', companyNamesList[2])
    page.locator("xpath=/html/body/section/div[2]/div[3]/div[1]/form/div[2]/div/ul/div/p/a").click()

    # get to company
    page.locator(".column-name").locator("text=JRCRUZ Corp").click()
    print("done")

    time.sleep(5)

    # get to low bids
    page.locator("text=Low Bids").click()
    print("done")


    # get all list names
   
    # for i in companyNamesList:
    #   print(i)

    time.sleep(5)
    
