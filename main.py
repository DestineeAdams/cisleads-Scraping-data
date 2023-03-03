import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import openpyxl

load_dotenv()  # take environment variables from .env.

info = [[],[]] #name and prices in a this fromat [[{"name":"sum of prices low"},{...}],[{"name":"sum of prices other"},{...}]]
headerValues = []

# grab excel file
filepath = r"Perfetto Bid History Template.xlsx"
sheetname = "Competitor Analysis"
    
wb = openpyxl.load_workbook(filepath)
ws = wb[sheetname]


# get sheet dimensionm
dimensions = (ws.max_row+1, ws.max_column+1)


# get header row coordinate
# get header row values

for y in range (1, dimensions[1]):
    headerValues.append({  
        ws.cell(row=1,column=y).value : ws.cell(row=1,column=y).coordinate
    })
    
# print(headerValues)
# print("--------------")

# import names of companies into dict

for i in range(1, dimensions[1]):
    info[0].append({
        ws.cell(row=1,column=y).value : ''
    }) 
    
    info[1].append({
        ws.cell(row=1,column=y).value : ''
    }) 

# print(info[0])
# print("--------------")
# print(info[1])


# grab table html for each name on list on site



# prase the html for price of low bids
    # put sum in dict with company name

# prase the html for price of Low + Other bids
    # put sum in dict with company name


# update excel file


# display in gui