import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import openpyxl
# from openpyxlutils import get_column_letter
from tkinter import *
# import tkinter as tk
from functools import partial


sheetname = "Competitor Analysis"
# wb = openpyxlload_workbook(getfilepath)
# ws = wb[sheetname]



class MyGUI:

    def __init__(self):
        # setup gui
        self.root = Tk()
        self.root.geometry("800x500")
        self.root.title("cis webspacing")
        
        
        # grab excel file path
        self.filepathlabel = Label(self.root, text="enter file path:", font=("san-seif", 12)).grid(row = 1, column = 1, pady = 2)
        self.filepath = Entry(self.root, width=20, font=("san-seif", 12)).grid(row = 1, column = 2, pady = 2)
        
        # GRAB SHEET NAME
        self.fileSheetName = Label(self.root, text="enter sheetName:", font=("san-seif", 12)).grid(row = 2, column = 1, pady = 2)
        self.SheetNameEn = Entry(self.root, width=20, font=("san-seif", 12)).grid(row = 2, column = 2, pady = 2)
        
        # coordanate for Low bids
        self.lobBidcoor = Label(self.root, text="enter lowbid header coordanate:", font=("san-seif", 12)).grid(row = 3, column = 1, pady = 2)
        self.lobBidcoorEn = Entry(self.root, width=20, font=("san-seif", 12)).grid(row = 3, column = 2, pady = 2)
        
        
        # coordanate for Low + Other bids
        self.lobBidcoor = Label(self.root, text="enter lowbid header coordanate:", font=("san-seif", 12)).grid(row = 4, column = 1, pady = 2)
        self.lobBidcoorEn = Entry(self.root, width=20, font=("san-seif", 12)).grid(row = 4, column = 2, pady = 2)
        
        
        self.btn = Button(self.root, text="submit", command=self.Getpath).grid(row = 5, column = 2, pady = 5)
        
        self.root.mainloop()
    
    def Getpath(self):
        path = self.filepath.get()
        print(path)
        
        return path
    
    def Getsheetname(self):
        sheetname = self.SheetNameEn.get()
        print(sheetname)
        
        return sheetname
    

    
    def readexcel():
        pass
        

c = MyGUI()


