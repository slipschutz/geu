
import sys
sys.path.append("xlrd-0.9.3")
import xlrd

from CBULine import *



def LoadCBU(FileName):

    book = xlrd.open_workbook(FileName) #"GEU_CBU.xlsx")


    sh = book.sheet_by_index(0)

    MapForCBU={}
    MapForEmptyNetIdCBU={}
    FirstLastNameCBU={}
    #Skip the first line, where there should be 
    #the titles for the colums
    for rowNumber in range(1,sh.nrows):
        theRow=sh.row(rowNumber)
        temp = CBU_Line()
        for i in range(0,len(theRow)):
            if theRow[i].ctype == 0 : # for empty cells
                temp.SetValue(i," ")
            elif theRow[i].ctype == 1: # for text
                temp.SetValue(i,theRow[i].value.strip())
            else:#everything else
                temp.SetValue(i,theRow[i].value)

        if temp.NetId == " " :
            if temp.LastName != " ":
                MapForEmptyNetIdCBU[temp.LastName.lower()]=temp
            else:
                print "CBU has no netId and no lastName"
        else :
            MapForCBU[temp.NetId.lower()]=temp
            
        FirstLastNameCBU[str(temp.FirstName).lower()+str(temp.LastName).lower()]=temp
            
    return MapForCBU,MapForEmptyNetIdCBU,FirstLastNameCBU


