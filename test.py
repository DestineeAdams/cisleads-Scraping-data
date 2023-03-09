import os, time, re, sys
from dotenv import load_dotenv
from helium import *
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.utils import get_column_letter

import tkinter as tk

someText = "this is label 2"

root = tk.Tk()

root.geometry("800x500")
root.title("cis webspacing")

label1 = tk.Label(root, text="hello world", font=("san-seif", 12))
# label1.pack(padx=20, pady=20)

label2 = tk.Label(root, text=someText, font=("san-seif", 12))
# label2.pack(padx=20, pady=20)


textBox = tk.Text(root, height=3, font=("san-seif", 12))
# textBox.pack(padx=20, pady=20)


label3 = tk.Label(root, text="input box: ", font=("san-seif", 12))
# label3.pack(padx=20, pady=20)
label3.grid(row = 1, column = 1, pady=2)


input = tk.Entry(root, width=50, font=("san-seif", 12))
# input.pack(padx=20, pady=20)
input.grid(row = 1, column = 2, pady = 2)



button = tk.Button(root, text="click me", font=("san-seif", 12))
# button.pack(padx=20, pady=20)
button.grid(row = 2, column = 1, pady = 2)


root.mainloop()