import os, time, re, sys
from dotenv import load_dotenv
from helium import *

compname = "JRCRUZ Corp"

load_dotenv()  # take environment variables from .env.


url = "https://cisleads.com/?login=1"

driver = start_firefox(url, headless=False)

time.sleep(1)

# login
write(os.getenv("UN"), into="email:")
write(os.getenv("PW"), into="password:")
click(S("#buttonLogin"))


# fill out form
click(S("//html/body/section/div[2]/div[3]/div[1]/form/div[1]/a[2]"))
write(compname, into=S("#Keywords"))
click(compname)

# click low bid
click("low Bids")

# click print
click("Print")

# lowbids_cells =find_all(S(".locbid-cell", below="low bids", above="other bids"))
# lowbids = [cell.web_element.text for cell in lowbids_cells]
# print(lowbids)

# save html
html = driver.page_source
print(html)

kill_browser()




