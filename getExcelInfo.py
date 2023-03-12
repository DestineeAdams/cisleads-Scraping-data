import os, time, re, sys, openpyxl
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import xlsxwriter
import pandas as pd
from openpyxl.utils import get_column_letter


load_dotenv()  # take environment variables from .env.
info = [] # {"name":"compname", "rowNumber": "row" ,"low":0, "other":0}

# these vars will later be giving by the user form the GUI
filePath = "Perfetto Bid History Template.xlsx"
sheetName = "Competitor Analysis"




class getExcelInfo:

    def __init__(self):
        self.df = pd.read_excel(filePath, sheet_name=sheetName, engine='openpyxl')  
        
    def getHeadersName(self):
        headersName = self.df.keys()
        return headersName

    def getARow(self, colHeader):
        return self.df[colHeader]
        
    
    



c = getExcelInfo()
print(c.getHeadersName()[0])
print(c.getARow(c.getHeadersName()[0]))

