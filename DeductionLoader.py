


import sys
sys.path.append("xlrd-0.9.3")
import xlrd

from DeductionLine import *


def LoadDeduction(FileName):
    book2 = xlrd.open_workbook(FileName)
    sh1 = book2.sheet_by_index(0)
    
    
    MapForDeductionsList={}
    FirstNameLastNameList={}

    for rowNumber in range(1,sh1.nrows):#skip the first row

        theRow=sh1.row(rowNumber)
        #check to see if the line has something in the netID field and the date field
        if theRow[8].ctype != 0 and theRow[1].ctype!=0:
            temp = DeductionLine()
            temp.EmployeeNumber=theRow[0].value
            temp.PayDay=theRow[1].value
            
            nameTemp =theRow[2].value
            nameList =nameTemp.split(",")

            if len(nameList) == 2:
                temp.LastName=nameList[0].strip()
                temp.FirstName=nameList[1].strip()
            else:
                temp.LastName="empty"
                temp.firstName="empty"

            temp.SubArea=str(theRow[3].value).strip();
            temp.EmployeeGroup=str(theRow[4].value).strip();
            temp.WageTypeNum=theRow[5].value
            temp.WageTypeText=str(theRow[6].value).strip();
            temp.DeductionAmt=theRow[7].value
            temp.NetId=str(theRow[8].value).strip();

            MapForDeductionsList[temp.NetId.lower()]=temp

            tempNameKey=temp.FirstName+temp.LastName
            tempNameKey=tempNameKey.lower()

            FirstNameLastNameList[tempNameKey]=temp

        elif theRow[8].ctype == 0 & theRow[2].ctype == 0: #probably a totaling line do nothing
            pass
        else : #There is a Deduction line that has no net id
            print "Deduction line with no netid"

    return MapForDeductionsList,FirstNameLastNameList
