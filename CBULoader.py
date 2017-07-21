
import sys
sys.path.append("xlrd-0.9.3")
import xlrd

from CBULine import *

class CBUWrap:
    pass


def LoadCBU(FileName):
    #Open the Excell Book
    book = xlrd.open_workbook(FileName) #"GEU_CBU.xlsx")

    #Open the first sheet 
    sh = book.sheet_by_index(0)

    NetIdMap={}
    MapForEmptyNetIdCBU={}
    FirstLastNameCBU={}

    firstRow=sh.row(0)
    HeaderMapName2Num={}
    HeaderMapNum2Name={}
    for i in range(0,len(firstRow)):
        if firstRow[i].ctype == 1 : #Text
            HeaderMapName2Num[firstRow[i].value.strip().lower()]=i
            HeaderMapNum2Name[i]=firstRow[i].value.strip().lower()

            

    #Skip the first line, where there should be 
    #the titles for the colums
    for rowNumber in range(1,sh.nrows):
        theRow=sh.row(rowNumber)
        temp = CBU_Line()
        for i in range(0,len(theRow)):
            if theRow[i].ctype == 0 : # for empty cells
                temp.SetValueWithMap(HeaderMapNum2Name,i," ")
            elif theRow[i].ctype == 1: # for text
                temp.SetValueWithMap(HeaderMapNum2Name,i,theRow[i].value.strip())
            elif theRow[i].ctype==3: # for excell dates
                dateTEMP =theRow[i].value
                tupleThing =xlrd.xldate.xldate_as_datetime(dateTEMP, book.datemode)
                temp.SetValueWithMap(HeaderMapNum2Name,i,tupleThing.date().strftime("%m/%d/%Y"))#str(tupleThing.date())
            else:#everything else
                temp.SetValueWithMap(HeaderMapNum2Name,i,theRow[i].value)

        if temp.EmployedUnit == " ":
            print ("Error in CBULoader: Missing Employ Unit code")

        if temp.NetId == " " :
            if temp.LastName != " ":
                firstLastKey=str(temp.FirstName).lower()+str(temp.LastName).lower()
                MapForEmptyNetIdCBU[firstLastKey]=temp
            else:
                print ("Error in CBULoader: CBU Line",rowNumber,"has no netId and no lastName")
        else:
            NetIdMap[temp.NetId.lower()]=temp
        
        #Always make a entry in the first Last Name Map
        firstLastKey=str(temp.FirstName).lower()+str(temp.LastName).lower()
#        if firstLastKey in FirstLastNameCBU:
#            print "Name already there", firstLastKey
#            print "netid ",temp.NetId,FirstLastNameCBU[firstLastKey].NetId
        FirstLastNameCBU[firstLastKey]=temp


    ACBUWrap=CBUWrap()
    ACBUWrap.NetIdMap=NetIdMap
    ACBUWrap.FirstLastNameMap=FirstLastNameCBU
    ACBUWrap.EmptyNetId=MapForEmptyNetIdCBU
    
    return ACBUWrap


