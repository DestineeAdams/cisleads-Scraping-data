# import os, time
# from playwright.sync_api import sync_playwright 
# from dotenv import load_dotenv
# from fillSheet import *
# from bs4 import BeautifulSoup
# load_dotenv()  # take environment variables from .env.

# # the vars will be passed in by the user later
# gcn = fillSheet('Perfetto Bid History Template.xlsx', "Competitor Analysis")



# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=50)
#     page = browser.new_page()
    
#     # login page nav
#     page.goto("file:///C:/Users/des11/Downloads/JRCRUZ%20Corp%20-%20Construction%20Information%20Systems%20(2_26_2023%2010_07_47%20PM).html")


    
#     # grab text
#     tablehtml = page.inner_html(".pc-print-report-table")
      
#     # tablelist.append(getTR)
#     print(tablehtml)



# # iterable = 36
# # for i in range(iterable + 1):
# #     print(i) 


import re


text = '$7,249,433'

print(re.sub('[$,]', '', text))


