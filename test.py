import os, time, re, sys
from dotenv import load_dotenv
from helium import *

compname = "JRCRUZ Corp"

load_dotenv()  # take environment variables from .env.


url = "https://lifehacker.com/the-easiest-ways-to-dry-your-laundry-faster-1850082752"

driver = start_firefox(url, headless=False)

time.sleep(1)

click(Link('heading'))