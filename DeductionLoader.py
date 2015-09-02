


import sys
sys.path.append("xlrd-0.9.3")
import xlrd

from DeductionLine import *


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
                #Last name is in one column
                temp.LastName=theRow[HeaderMap["lastname"]].value.strip()
                temp.FirstName=theRow[HeaderMap["firstname"]].value.strip()
                
            elif "lastname, firstname" in HeaderMap:
                unsplitName=theRow[HeaderMap["lastname, firstname"]].value.strip()
                nameList =unsplitName.split(",")
                if len(nameList) == 2:
                    temp.LastName=nameList[0].strip()
                    temp.FirstName=nameList[1].strip()
                else:
                    temp.LastName="empty"
                    temp.firstName="empty"
            
            #now the other fields 
            temp.NetId=str(theRow[HeaderMap["msu netid"]].value).strip()
            temp.EmployeeNumber=theRow[HeaderMap["employee no"]].value
            temp.PayDay=theRow[HeaderMap["pay date"]].value
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

            MapForDeductionsList[temp.NetId.lower()]=temp
            tempNameKey=temp.FirstName+temp.LastName
            tempNameKey=tempNameKey.lower()

            FirstNameLastNameList[tempNameKey]=temp

    endFor=0

    return MapForDeductionsList,FirstNameLastNameList

#         #first check to see if this sheet has lastname,firstname or lastname   firstname
#         tempForComma=theRow[2].value
#         if tempForComma.find(",") == -1:
#             ##there is no comma the names are in two colums
#             namesIn2Columns=True
#             offset=1
#         else:
#             namesIn2Columns=False
#             offset=0

#         #check for weird extra lines 
#         if 8+offset >= numberOfCols:
#             offset=0

# #        print "))))))))))))))))))))))))",rowNumber
# #        print theRow[8+offset], "               ",offset, "    ",numberOfCols
            

#         #check to see if the line has something in the netID field and the date field
#         if theRow[8+offset].ctype != 0 and theRow[1].ctype!=0:
#             temp = DeductionLine()
#             temp.EmployeeNumber=theRow[0].value
#             temp.PayDay=theRow[1].value
            
#             if namesIn2Columns:
#                 temp.LastName=theRow[2].value
#                 temp.FirstName=theRow[3].value
#             else:
#                 nameTemp =theRow[2].value
#                 nameList =nameTemp.split(",")
#                 if len(nameList) == 2:
#                     temp.LastName=nameList[0].strip()
#                     temp.FirstName=nameList[1].strip()
#                 else:
#                     temp.LastName="empty"
#                     temp.firstName="empty"
#             ####

#             temp.SubArea=str(theRow[3+offset].value).strip()
#             temp.EmployeeGroup=str(theRow[4+offset].value).strip()
#             temp.WageTypeNum=theRow[5+offset].value
#             temp.WageTypeText=str(theRow[6+offset].value).strip()
#             temp.DeductionAmt=theRow[7+offset].value
#             temp.NetId=str(theRow[8+offset].value).strip()


#             MapForDeductionsList[temp.NetId.lower()]=temp

#             tempNameKey=temp.FirstName+temp.LastName
#             tempNameKey=tempNameKey.lower()

#             FirstNameLastNameList[tempNameKey]=temp

#         elif theRow[8].ctype == 0 and theRow[2].ctype == 0: #probably a totaling line
#             pass
#         elif theRow[6].ctype!=0 and theRow[7].ctype!=0 and theRow[8+offset].ctype==0 : 
#             #There is a Deduction line that has no net id
#             print "Deduction line with no netid"
#             print "Found in sheet ",FileName



