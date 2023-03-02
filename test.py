import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from openpyxl import load_workbook, Workbook
import json
import pandas as pd
import xlwings as xw

load_dotenv()  # take environment variables from .env.


for item in range(5):

    try:
        driver = start_firefox("https://www.youtube.com/", headless=False)
        write("test", into="searwch") 
        driver.quit()
        print("done")

    except NameError:
        driver.quit()
    except LookupError:
        driver.quit()

    finally:
        driver.quit()
      
