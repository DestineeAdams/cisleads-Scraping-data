# import os, time
# from playwright.sync_api import sync_playwright 
# from dotenv import load_dotenv
# from fillSheet import *

# load_dotenv()  # take environment variables from .env.

# # the vars will be passed in by the user later
# gcn = fillSheet('Perfetto Bid History Template.xlsx', "Competitor Analysis")



# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=50)
#     page = browser.new_page()

#     # login page nav
#     page.goto("http://autopract.com/selenium/textmatch/")



#     page.keyboard.press("Control+KeyA")
#     print("Control+a")

#     page.keyboard.press("Control+KeyR")
#     print("Control+r")
#     time.sleep(5)
    
#         # grab text
#     text = page.locator("button.button").first.text_content()
#     print(text)



iterable = 36
for i in range(iterable + 1):
    print(i) 
