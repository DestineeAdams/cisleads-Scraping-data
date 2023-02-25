import os, time
from playwright.sync_api import sync_playwright 
from dotenv import load_dotenv
import getCompanyNames as gcn

load_dotenv()  # take environment variables from .env.

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()

    # login page nav
    page.goto("https://cisleads.com/?login=1")

    # login
    page.fill('input#UserName',  os.getenv("UN"))
    page.fill('input#Password',  os.getenv("PW"))
    page.click('#buttonLogin')
    time.sleep(5)

    # fill out se
    page.goto("https://cisleads.com/desktop")
    page.get_by_title('GCs & Subs').click()

    time.sleep(5)