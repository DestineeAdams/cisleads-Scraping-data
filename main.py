import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import openpyxl

load_dotenv()  # take environment variables from .env.

info = [[],[],[]] #name and prices in a this fromat [[{"name":"sum of prices low"},{...}],[{"name":"sum of prices other"},{...}]]
info2 = [] # {"name":"compname", "low":0, "other":0}

headerValues = []
listOfCompNames = []
html = None
compname = None
index = 4

# grab excel file
filepath = r"Perfetto Bid History Template.xlsx"
sheetname = "Competitor Analysis"
    
wb = openpyxl.load_workbook(filepath)
ws = wb[sheetname]


# get sheet dimensionm
dimensions = (ws.max_row+1, ws.max_column+1)
# print(dimensions)


# get header row coordinate and row values put then in dict
for y in range (1, dimensions[1]):
    headerValues.append({  
        ws.cell(row=1,column=y).value : ws.cell(row=1,column=y).coordinate
    })
    
# print(headerValues)
# print("--------------")

# import names of companies into dict and into list

for i in range(1, dimensions[0]):
 
    if ws.cell(row=i,column=1).value.lower() != "name":      
    
        print(ws.cell(row=i,column=1).value)
        
        info2.append({
            "name": ws.cell(row=i,column=1).value, 
            "low": 0, 
            "other":0
        })
    

# print(info[0])
# print("--------------")
# print(info[1])
# print("--------------")
# print(info[2])



# compname = info[0][index]

# grab table html for each name on list on site
def grabTableHtml(index):
    
    driver = start_firefox("https://cisleads.com/?login=1", headless=False)
    # driver = start_firefox("https://cisleads.com/?login=1", headless=True)

    
    # login
    write(os.getenv("UN"), into="email:")
    write(os.getenv("PW"), into="password:")
    click(S("#buttonLogin"))
    
    
    # fill out form
    click(S("//html/body/section/div[2]/div[3]/div[1]/form/div[1]/a[2]"))
    write(info[0][index], into=S("#Keywords"))
    
    time.sleep(1)
    click(info[0][index])
    
    # click print
    click("Print")
    
    time.sleep(5) # with for page to load
    
    # save html
    html = driver.page_source
    # print(html)
    
    # end
    kill_browser()
    print("done helium")
    
    return html


# put raw table html into a file
def prase():
    soup = BeautifulSoup(html, "html.parser")
    getTables = soup.find_all("table")
    Tables = [getTables[2], getTables[3]]
    
    print(Tables)
    
    with open("lowbids.html", "w") as f:
        data = str(Tables[0])
        f.write(data)
        
    with open("otherbids.html", "w") as f:
        data = str(Tables[1])
        f.write(data)
             
           

# prase the rawHTML.html for price of low bids
    # put sum in dict with company name
def getlowBidsSum(compname, index):
    
    tds = None
    prices = []

    with open("lowbids.html") as fp:
        # get locbid-cell
        soup = BeautifulSoup(fp, "html.parser")
        tds = str(soup.find_all(class_="locbid-cell"))
 
        with open("low.html", "w") as f:
            f.write(tds)
    
    with open("low.html") as fq: 
        soup = BeautifulSoup(fq, "html.parser")
        strongs = list(soup.find_all("strong"))
        
        for i in range(len(strongs)):
            prices.append(strongs[i].get_text())
            
        for i in range(len(prices)):
            prices[i] = int(re.sub("[$,]", "", prices[i]))


    info[1][index][compname] = sum(prices)
    print(info[1][index])



   

# prase the html for price of Other bids
    # put sum in dict with company name
def getotherBidsSum(compname, index):
    tds = None
    prices = []

    with open("otherbids.html") as fp:
        # get locbid-cell
        soup = BeautifulSoup(fp, "html.parser")
        tds = str(soup.find_all(class_="locbid-cell"))
 
        with open("other.html", "w") as f:
            f.write(tds)
    
    with open("other.html") as fq: 
        soup = BeautifulSoup(fq, "html.parser")
        strongs = list(soup.find_all("strong"))
        
        for i in range(len(strongs)):
            prices.append(strongs[i].get_text())
            
        for i in range(len(prices)):
            prices[i] = int(re.sub("[$,]", "", prices[i]))


    info[1][index][compname] = sum(prices)
    print(info[1][index])

 
            


# update excel file


# display in gui


# for loop to cylce thought list of name and grab html

# for i in range(0, len(info[0])):
    
#     # html = grabTableHtml(index)
#     # print(html)
    
#     # prase()
    
#     getlowBidsSum(compname, index)
#     getotherBidsSum(compname, index)
    
for i in range(0, len(info2)):   
    print(info2[i]["name"])
    
