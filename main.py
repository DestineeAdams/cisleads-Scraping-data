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



# try:
    
#     print("worked")

# except LookupError as e:
#     print(f"{e}, did not work")

# selcet search results
# wait_until(click(compname).exists)
click(compname)

# click low bid
click("low Bids")

# grab total number
# LowbidsTotal = Text(S('.number-total')).value
# print(LowbidsTotal)
# print(TextField(S('.number-total')).value)

# click print
click("Print")
time.sleep(3)

# save html
html = driver.page_source
print(html)

kill_browser()




