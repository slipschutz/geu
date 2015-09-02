
import sys
sys.path.append("xlrd-0.9.3")
import xlrd

from ReconciledEntry import *



def Load(FileName):

    book = xlrd.open_workbook(FileName) 


    sh = book.sheet_by_index(0)

    MapForCBU={}
    
    #Skip the first line, where there should be 
    #the titles for the colums
    for rowNumber in range(1,sh.nrows):
        theRow=sh.row(rowNumber)
        temp = ReconciledEntry()
        for i in range(0,len(theRow)):
            if theRow[i].ctype == 0 : # for empty cells
                temp.SetValueByIndex(i," ")
            elif theRow[i].ctype == 1: # for text
                temp.SetValueByIndex(i,theRow[i].value.strip().lower())
            else:#everything else
                temp.SetValueByIndex(i,theRow[i].value)

            MapForCBU[str(temp.GetValueByTag("MSUNETID")).lower()]=temp
            

    return MapForCBU


