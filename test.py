import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import openpyxl

load_dotenv()  # take environment variables from .env.



# driver = start_firefox("https://cisleads.com/?login=1", headless=False)
driver = start_firefox("https://cisleads.com/?login=1", headless=True)


# login
write(os.getenv("UN"), into="email:")
write(os.getenv("PW"), into="password:")
click(S("#buttonLogin"))


# fill out form
click(S("//html/body/section/div[2]/div[3]/div[1]/form/div[1]/a[2]"))
write(info[index]["name"], into=S("#Keywords"))

time.sleep(1)
click(info[index]["name"])

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
