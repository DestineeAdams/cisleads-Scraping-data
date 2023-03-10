# from tkinter import *
# from tkinter import filedialog
# from tkinter import ttk

# root = Tk()
# root.geometry("100x200")
# root.title("cis webspacing")

# def openFile():
#     filepath = filedialog.askopenfilename()
#     print(filepath)

# label1= Label(root, text="Hello").pack()

# btn = Button(text="browse", command=openFile).pack()



# root.mainloop()

import pandas

excel_data_df = pandas.read_excel('text.xlsx',  sheet_name='Sheet1', header=1)

# print whole sheet data
print(excel_data_df)