

import sys
sys.path.append("xlrd-0.9.3")
import xlrd
import datetime

from DeductionLine import *


class PersonInfoFromDeductionFile:
    def __init__(self):
       self.Lines=[]


def SplitName(temp,unsplitName,splitChar):    
    nameList =unsplitName.split(splitChar)
    if len(nameList) == 2:
        temp.LastName=nameList[0].strip()
        temp.FirstName=nameList[1].strip()
    elif len(nameList)== 3 and splitChar==" ":
        temp.FirstName=nameList[0].strip()
        temp.LastName=nameList[1].strip()+nameList[2].strip()
    else:
        temp.LastName= "ErrorCouldNotParseLastAndFirstName"
        temp.firstName="ErrorCouldNotParseLastAndFirstName"




def LoadDeduction(FileName):
    book2 = xlrd.open_workbook(FileName)
    sh1 = book2.sheet_by_index(0)
    
    print FileName    
    MapForDeductionsList={} #Map from NetID 2 all information found in dues deduction line
    FirstNameLastNameList={}#Map from firstname+lastname to all info

    HeaderMap={}
    ###Look in the first 10 rows for the good stuff
    for rowNumber in range (1,10):
        theRow=sh1.row(rowNumber)
        if theRow[0].value.strip() == "Employee No":
            startRow=rowNumber
            ###this is the row with the column headers
            for i in range (0,len(theRow)):
                HeaderMap[theRow[i].value.strip().lower()]=i
            break #end the for loop
                                

    for rowNumber in range(startRow+1,sh1.nrows):

        theRow=sh1.row(rowNumber)
        numberOfCols =len(theRow)
        ##check to seee if the line is a good entry line
        if theRow[HeaderMap["pers.subarea"]].ctype !=0 and theRow[HeaderMap["pay date"]].ctype!=0 and theRow[HeaderMap["employeegroup"]].ctype !=0:
            temp = DeductionLine()
            ###first Deal with the Last name first name issue
            if "lastname" in HeaderMap:
                if theRow[HeaderMap["firstname"]].ctype==0:
                    #This catch is for the following case.  The main part of the sheet has firstname then lastname
                    #in different columns but the bottom corrections part of the sheet has firstnma,lastname than a blank
                    SplitName(temp,theRow[HeaderMap["lastname"]].value.strip()," ")
                else:
                    #Last name is in one column and first name is in one column
                    temp.LastName=theRow[HeaderMap["lastname"]].value.strip()
                    temp.FirstName=theRow[HeaderMap["firstname"]].value.strip()              
                
                

            elif "lastname, firstname" in HeaderMap:
                unsplitName=theRow[HeaderMap["lastname, firstname"]].value.strip()
                SplitName(temp,unsplitName,",")
                # nameList =unsplitName.split(",")
                # if len(nameList) == 2:
                #     temp.LastName=nameList[0].strip()
                #     temp.FirstName=nameList[1].strip()
                # else:
                #     temp.LastName= "ErrorCouldNotParseLastAndFirstName"
                #     temp.firstName="ErrorCouldNotParseLastAndFirstName"


            #now the other fields 
            temp.NetId=str(theRow[HeaderMap["msu netid"]].value).strip()
            temp.EmployeeNumber=theRow[HeaderMap["employee no"]].value
            dateTEMP =theRow[HeaderMap["pay date"]].value

            tupleThing =xlrd.xldate.xldate_as_datetime(dateTEMP, book2.datemode)
            temp.PayDay=tupleThing.date().strftime("%m/%d/%Y") # str(tupleThing.date())
            
            temp.SubArea=theRow[HeaderMap["pers.subarea"]].value
            temp.EmployeeGroup=theRow[HeaderMap["employeegroup"]].value
            temp.WageTypeNum=theRow[HeaderMap["wagetype"]].value
            temp.WageTypeText=theRow[HeaderMap["wagetype text"]].value
            
            #deduction amount line doesn't always look the same 

            for key,value in HeaderMap.iteritems():
                if str(key).find("ded") != -1:
                    #this is the one
                    magicIndex=value
                    break
                
            temp.DeductionAmt=theRow[magicIndex].value
            

            
            netid=temp.NetId.lower()
            tempNameKey=temp.FirstName+temp.LastName
            tempNameKey=tempNameKey.lower()
            
            if netid in MapForDeductionsList:
                #the netid is already in the file
                #apppend the deduction line object the personInfo's
                #list of lines
                MapForDeductionsList[netid].Lines.append(temp)
            else:
                personInfo=PersonInfoFromDeductionFile()
                personInfo.Lines.append(temp)
                MapForDeductionsList[netid]=personInfo


            if tempNameKey in FirstNameLastNameList:
                FirstNameLastNameList[tempNameKey].Lines.append(temp)
            else:
                personInfo=PersonInfoFromDeductionFile()
                personInfo.Lines.append(temp)
                FirstNameLastNameList[tempNameKey]=personInfo

            
    endFor=0

    return MapForDeductionsList,FirstNameLastNameList

