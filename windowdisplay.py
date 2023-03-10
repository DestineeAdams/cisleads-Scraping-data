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
        self.Form()
        wrapperdisplayData = LabelFrame(self.pane, text="data").pack(fill= "both", expand="yes", padx=20, pady=20)

        
        
        # --------------------------------
        
        
        self.pane2 = Frame(self.root).pack(fill = BOTH, expand = True)
        wrapperForm = LabelFrame(self.pane2, text="form").pack(fill= "both", expand="yes", padx=20, pady=20)
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
        
        print(infodict[keysList[0]][0])
        
        tv = ttk.Treeview(self.pane2 , columns=keysTuple, show='headings' , height=len(keysTuple), selectmode="extended")
   
        tv.column('#0', width=0, stretch=YES)
        tv.heading('#0', text='', anchor=CENTER)
        
        for i in range(len(keysTuple)):
            tv.column(keysList[i], anchor=CENTER, width=80)
            tv.heading(keysList[i], text=keysList[i], anchor=CENTER)
            
            # tv.insert(parent='', index=1, iid=2, text='', values= (infodict[keysList[0]][0]))
        
     
        tv.pack()
        
        # for item in range(0, 144):
        #     insertInfo = ""
           
        #     for j in range(0, len(keys)):
        #         insertInfo = insertInfo + f'{keys[j]} is: {infodict[keys[j]][item]} | '
        
        #     self.lobBidcoor = Label(self.pane2, text=insertInfo, font=("san-seif", textSize)).pack()
        

    
        
        # keys = list(infodict.keys())
        
        # for item in range(0, 144):
        #     insertInfo = ""
           
        #     for j in range(0, len(keys)):
        #         insertInfo = insertInfo + f'{keys[j]} is: {infodict[keys[j]][item]} | '
        
        #     self.lobBidcoor = Label(self.pane2, text=insertInfo, font=("san-seif", textSize)).pack()
        

       
        
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
        