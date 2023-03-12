import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
from ExcelInfo import *

load_dotenv()  # take environment variables from .env.


e = ExcelInfo()


class scrape:

    def __init__(self, index):
      
        # print(e.getHeadersName()[0])
        
        print(e.getAcol(e.getHeadersName()))
        # self.gethtml()
        
    
    
    def gethtml(self, compName):
        driver = start_firefox("https://cisleads.com/?login=1", headless=False)
        # driver = start_firefox("https://cisleads.com/?login=1", headless=True)
    
        # login
        write(os.getenv("UN"), into="email:")
        write(os.getenv("PW"), into="password:")
        click(S("#buttonLogin"))
        
    
        # fill out form
        click(S("//html/body/section/div[2]/div[3]/div[1]/form/div[1]/a[2]"))
        write(compName, into=S("#Keywords"))
        
        time.sleep(1)
        click(compName)
        
        # click print
        click("Print")
        
        time.sleep(5) # with for page to load
        
        # save html
        html = driver.page_source
        # print(html)
        
        # end
        kill_browser()
        # print("done helium")
        
        return html



    
    

c = scrape(9)
