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



def FunctionName(args):
    
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
    
    