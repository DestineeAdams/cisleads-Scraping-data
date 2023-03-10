import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import openpyxl
# from openpyxlutils import get_column_letter
from tkinter import *
import tkinter as tk
# import tkinter as tk
from functools import partial
import pandas as pd
from tkinter import ttk

textSize = 10


class MyGUI:

    def __init__(self):
        # setup gui
        self.root = Tk()
        self.root.geometry("1000x1000")
        self.root.title("cis webspacing")
        
        
        # form
        self.pane = Frame(self.root).pack(fill = BOTH, expand = False)
        self.wrapperdisplayData = LabelFrame(self.pane, text="data").pack(fill= "both", expand="yes", padx=20, pady=20)
        self.Form()
        
        
        # --------------------------------
        
        
        self.pane2 = Frame(self.root).pack(fill = BOTH, expand = True)
        self.wrapperForm = LabelFrame(self.pane2, text="form").pack(fill= "both", expand="yes", padx=20, pady=20)
        self.displayData()
        
        
        
        self.root.mainloop()
    
    def Getpath(self):
        path = self.filepath.get()
        print(path)
        
        return path
    
    def Getsheetname(self):
        sheetname = self.SheetNameEn.get()
        print(sheetname)
        
        return sheetname
    
    def displayData(self):
       
        excelFile = self.Getpath()
        # df = pd.read_excel(excelFile)
        df = pd.read_excel("Perfetto Bid History Template.xlsx")
        
        infodict = df.to_dict()
        
        keysTuple = tuple(infodict.keys())
        keysList = list(infodict.keys())
        
        
        # for i in range(len(infodict["Name"])):
        
        #     rowlist = []
            
        #     for j in range(len(keysList)):
        #         # currRow = ""
        #         # currRow = currRow + f"{infodict[keysList[i]][i]}"
                
        #         # (infodict["Name"][i], infodict["# Times Competed Against Perfetto Contracting Co"][i])
        #         rowlist.append(infodict[keysList[j]][i])
                
        #     rowTuple = tuple(rowlist)
        #     print(rowTuple)
        
        # print(len(infodict["Name"]))
        
        
        
        
        
        tv = ttk.Treeview(self.wrapperdisplayData , columns=keysTuple, show='headings' , height=20, selectmode="extended")
   
        tv.column('#0', width=0, stretch=YES)
        tv.heading('#0', text='', anchor=CENTER)
        
        for k in range(len(keysList)):
            tv.heading(k, text=keysList[k], anchor=CENTER)
            tv.column(keysList[k], anchor=CENTER, width=115)
        
        for i in range(len(infodict["Name"])):

       
            rowlist = []
            for j in range(len(keysList)):
                
                rowlist.append(infodict[keysList[j]][i])
                
            rowTuple = tuple(rowlist)
            tv.insert("", "end", values=rowTuple)

            print(rowTuple)
        
   
     
        tv.pack()
        
     
        scrollbar = ttk.Scrollbar(self.pane2, orient='horizontal', command=tv.xview)
        tv.configure(xscroll=scrollbar.set)
        scrollbar.pack(fill = X)
        
        scrollbar = ttk.Scrollbar(self.pane2, orient='vertical', command=tv.yview)
        tv.configure(yscroll=scrollbar.set)
        scrollbar.pack(fill = Y, side=LEFT)
        


    def Form(self):

        # grab excel file path
        self.filepathlabel = Label(self.pane, text="enter file path:", font=("san-seif", textSize)).pack()
        self.filepath = Entry(self.pane, width=20, font=("san-seif", textSize))
        self.filepath.pack()
        
        # GRAB SHEET NAME
        self.fileSheetName = Label(self.pane, text="enter sheetName:", font=("san-seif", textSize)).pack()
    
        self.SheetNameEn = Entry(self.pane, width=20, font=("san-seif", textSize))
        self.SheetNameEn.pack()
        
        # coordanate for Low bids
        self.lobBidcoor = Label(self.pane, text="enter lowbid sums header name:", font=("san-seif", textSize)).pack()
        
        self.lobBidcoorEn = Entry(self.pane, width=20, font=("san-seif", textSize))
        self.lobBidcoorEn.pack()
        
        
        # coordanate for Low + Other bids
        self.lobBidcoor = Label(self.pane, text="enter other plus low bid sums header name", font=("san-seif", textSize)).pack()
        
        self.lobBidcoorEn = Entry(self.pane, width=20, font=("san-seif", textSize))
        self.lobBidcoorEn.pack()
        
        
        self.btn = Button(self.pane, text="submit", command=self.Getpath).pack()
        
        
c = MyGUI()



# excelFile = "Perfetto Bid History Template.xlsx"
# df = pd.read_excel(excelFile)
# new_dict = df.to_dict()
        
# for item in range(0, 144):  
#     print(f'company name: {new_dict["Name"][item]} | low bids: {new_dict["2022 Low $ (Sum of all Low Bids)"][item]} | other + low bids: {new_dict["2022 $ Bid ($ Low + $ Other)"][item]}')
        