# import os, time, re, sys
# from dotenv import load_dotenv
# from helium import *
# from bs4 import BeautifulSoup
# import openpyxl
# from openpyxl.utils import get_column_letter

# import tkinter as tk

# someText = "this is label 2"

# root = tk.Tk()

# root.geometry("800x500")
# root.title("cis webspacing")

# label1 = tk.Label(root, text="hello world", font=("san-seif", 12))
# # label1.pack(padx=20, pady=20)

# label2 = tk.Label(root, text=someText, font=("san-seif", 12))
# # label2.pack(padx=20, pady=20)


# textBox = tk.Text(root, height=3, font=("san-seif", 12))
# # textBox.pack(padx=20, pady=20)


# label3 = tk.Label(root, text="input box: ", font=("san-seif", 12))
# # label3.pack(padx=20, pady=20)
# label3.grid(row = 1, column = 1, pady=2)


# input = tk.Entry(root, width=50, font=("san-seif", 12))
# # input.pack(padx=20, pady=20)
# input.grid(row = 1, column = 2, pady = 2)



# button = tk.Button(root, text="click me", font=("san-seif", 12))
# # button.pack(padx=20, pady=20)
# button.grid(row = 2, column = 1, pady = 2)


# root.mainloop()


# from tkinter import *

# def my_fun():
#     print("Function called")
    

# win = Tk()

# button = Button(win, text="Click me", command = my_fun)
# button.pack()

# win.mainloop()


# # Importing tkinter module
# from tkinter import *
# # from tkinter.ttk import *

# # creating Tk window
# master = Tk()

# # creating a Fra, e which can expand according
# # to the size of the window
# pane = Frame(master)
# pane.pack(fill = BOTH, expand = True)

# # button widgets which can also expand and fill
# # in the parent widget entirely
# # Button 1
# b1 = Button(pane, text = "Click me !",
# 			background = "red", fg = "white")
# b1.pack(side = LEFT, expand = True, fill = BOTH)

# # Button 2
# b2 = Button(pane, text = "Click me too",
# 			background = "blue", fg = "white")
# b2.pack(side = LEFT, expand = True, fill = BOTH)

# # Button 3
# b3 = Button(pane, text = "I'm also button",
# 			background = "green", fg = "white")
# b3.pack(side = LEFT, expand = True, fill = BOTH)

# label = Label(master, text="im a label").pack()

# # Execute Tkinter
# master.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
# root.geometry("800x800")
root.title("cis webspacing")


label1= Label(root, text="hello").pack()

# form
ws = Frame(root)
ws.pack(fill = BOTH, expand = False)
        
ws['bg']='#111'


info = {
'Rank':{'Vineet','Anil','Vinod'}, 'Badge':{'Alpha','Bravo', "Charlie"}, 'id':{'3','2','1'}
}


tv = ttk.Treeview(ws)

tv['columns']=('Rank', 'Name', 'Badge')

tv.column('#0', width=0, stretch=NO)
tv.heading('#0', text='', anchor=CENTER)
tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))

tv.pack()


ws.mainloop()