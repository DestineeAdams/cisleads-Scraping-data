import pandas as pd


# these vars will later be giving by the user form the GUI
filePath = "Perfetto Bid History Template.xlsx"
sheetName = "Competitor Analysis"




class ExcelInfo:

    def __init__(self):
        self.df = pd.read_excel(filePath, sheet_name=sheetName, engine='openpyxl')  
        
    def getHeadersName(self, index):
        headersName = self.df.keys()[index]
        return headersName

    def getAcol(self, colHeader):
        return self.df[colHeader]
        
    

c = ExcelInfo()
# print(c.getHeadersName())
print(c.getAcol(c.getHeadersName(0)))

