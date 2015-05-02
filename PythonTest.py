#!/usr/bin/env python3

#
# IMPORT THINGS or else
#
import sys
sys.path.append("xlwt-0.7.5")
import xlwt

from CBULine import *
from DeductionLine import *


import CBULoader
import DeductionLoader

from os import listdir
from os.path import isfile, join

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False




if __name__ == "__main__" :

    MapForCBU,MapForEmptyNetIdCBU=  CBULoader.LoadCBU("GEU_CBU.xlsx") # returns MapForCbu then MapForEmptyNetIdCbu
    MapForDeductionsList,FirstNameLastNameList= DeductionLoader.LoadDeduction("GEU_DUES.xlsx")#returns MapForDeductonsList

    

    deductionFileNames = [ f for f in listdir("./DeductionData") if isfile(join("./DeductionData",f)) ]

    MapForAllDeductionFiles={}
    for i in deductionFileNames:
        splitName=i.split("-")
        datePart=splitName[0].strip()

        MapForAllDeductionFiles[float(datePart)]=DeductionLoader.LoadDeduction(join("./DeductionData",i))


    for date,thing in MapForAllDeductionFiles.iteritems():
        
        for netId,line in thing[0].iteritems():
            if netId == "boldarie":
                print (date)
                line.PrintShort()
    
    exit


    MapForInCBUButNotInDeductions={}
    MapForInBothLists={}

    for NetId,CBULine in MapForCBU.iteritems():
        if NetId in MapForDeductionsList:         #NetId is in both lists
            if CBULine.DuesType != MapForDeductionsList[NetId].WageTypeText: ## CBU Entry needs updating
                CBULine.UpdatedDuesType =MapForDeductionsList[NetId].WageTypeText
                CBULine.WasUpdated="Yes"
            else:
                CBULine.UpdatedDuesType =CBULine.DuesType
                CBULine.WasUpdated="No"

            MapForInBothLists[NetId]=CBULine

        else:
            MapForInCBUButNotInDeductions[NetId]=CBULine

    #For the people in CBU but not in deductions seperate again based on whether there is a dues tpye listed
    MapForInCBUButNotInDeductionsWithDuesStatus={}
    MapForInCBUButNotInDeductionsWithNoDuesStatus={}

    for netid, line in MapForInCBUButNotInDeductions.iteritems():
        if line.DuesType == "empty": 
            MapForInCBUButNotInDeductionsWithNoDuesStatus[netid]=line
        else:
            MapForInCBUButNotInDeductionsWithDuesStatus[netid]=line


    #Look if the CBU lines with no NetId match a first/last name in deduction list
    for netid,line in MapForEmptyNetIdCBU.iteritems():
        tempNameThing=line.FirstName+line.LastName
        tempNameThing=tempNameThing.lower()

        if tempNameThing in FirstNameLastNameList:
            print ("Found")

    
    Department2Members={}
    Department2FeePayers={}
    Department2NonComp={}

    for netid, line in MapForInBothLists.iteritems():
        key =line.EnrolledUnitName.lower()

        if key in Department2Members:
            pass
        else:
            Department2Members[key]=0
            Department2FeePayers[key]=0
            Department2NonComp[key]=0

        if line.UpdatedDuesType == "GEU Dues":
            Department2Members[key] +=1
        elif line.UpdatedDuesType == "GEU Fees-C":
            Department2FeePayers[key] +=1
        elif line.UpdatedDuesType == "GEU Fees-NC":
            Department2NonComp[key] +=1





    style = xlwt.XFStyle()

    wb = xlwt.Workbook()
    ws0 = wb.add_sheet('ReconciledCBU')
    
    count=0
    for netid,line in MapForInBothLists.iteritems():
        for i in range(32):
            ws0.write(count, i,line.GetValue(i))
        count=count+1


    ws1 = wb.add_sheet('BlankNetIdInCBU')
    count=0
    for netid,line in MapForEmptyNetIdCBU.iteritems():
        for i in range(32):
            ws1.write(count, i,line.GetValue(i))
        count=count+1


    ws2 = wb.add_sheet('CBUNotDeductWithDuesStatus')
    count=0
    for netid,line in MapForInCBUButNotInDeductionsWithDuesStatus.iteritems():
        for i in range(32):
            ws2.write(count, i,line.GetValue(i))
        count=count+1

    ws3 = wb.add_sheet('CBUNotDeductWithNoDuesStatus')
    count=0
    for netid,line in MapForInCBUButNotInDeductionsWithNoDuesStatus.iteritems():
        for i in range(32):
            ws3.write(count, i,line.GetValue(i))
        count=count+1
    

   # print len(Department2Members)," ",len(Department2FeePayers)," ",len(Department2NonComp)
    
    ws4 = wb.add_sheet('DepartStats')
    count=1
    ws4.write(0,0,"Department")
    ws4.write(0,1,"Members")
    ws4.write(0,2,"FeePayers")
    ws4.write(0,3,"Non-Compliant")
    ws4.write(0,4,"Total members")
    for name,val in Department2Members.iteritems():
        tot=float(Department2Members[name]+Department2FeePayers[name]+Department2NonComp[name])
        ws4.write(count,0,name)
        ws4.write(count,1,(Department2Members[name]/tot) * 100)
        ws4.write(count,2,Department2FeePayers[name]/tot *100)
        ws4.write(count,3,Department2NonComp[name]/tot *100)
        ws4.write(count,4,tot )
        count=count+1
    


    

    wb.save("test.xls")


################################################################################################################



def temp():
    
    MapForElle = { (0.25,1):423.076, (0.25,2):444.2308,(0.25,3):465.3846,
                   (0.5,1):846.1538, (0.5,2):888.4615, (0.5,3):930.7692,
                   (0.75,1):1269.23, (0.75,2):1332.692,(0.75,3):1396.194}
    
    total=0
    totalWithMin=0
    numPeopleBelowMin=0
    for NetId,CBULine in MapForCBU.iteritems():
        if is_number(CBULine.PayRate ):
            temp =(CBULine.GA_Percentage/100,CBULine.SalaryLevel)
            minPay=MapForElle[temp]
            if CBULine.PayRate*1.05 < minPay:
                numPeopleBelowMin=numPeopleBelowMin+1
                totalWithMin=totalWithMin+minPay
            else:
                totalWithMin=totalWithMin+CBULine.PayRate*1.05

            total=total+float(CBULine.PayRate)
            

    print ("Total Byweekly amount paid to people", total)
    print (numPeopleBelowMin)
    print ("total with mins ",totalWithMin)
    print ("increase per 19.5 periods ", (totalWithMin-total)*19.5)

