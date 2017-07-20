#!/usr/bin/env python3




import sys


#from xlwt import *

from openpyxl import Workbook

from CBULine import *
from DeductionLine import *

import CBULoader
import DeductionLoader

import ReconciledEntry 

from os import listdir
from os.path import isfile, join
import os
import datetime

def Reconcile(CBU_File,Dues_File,GuiWindow):

    MapForCBU={}
    MapForEmptyNetIdCBU={}
    MapForFirstLastCBU={}
    MapForDeductionsList={}
    FirstNameLastNameList={}
    
    MapForCBU,MapForEmptyNetIdCBU,MapForFirstLastCBU=  CBULoader.LoadCBU(CBU_File) # returns MapForCbu then MapForEmptyNetIdCbu
    MapForDeductionsList,FirstNameLastNameList= DeductionLoader.LoadDeduction(Dues_File)#returns MapForDeductonsList
    
    Dues_File_Temp=os.path.basename(Dues_File)
    splitName=Dues_File_Temp.split("-")
    datePart=splitName[0].strip()
    dateTemp=datetime.datetime.strptime(datePart,"%Y%m%d").date()
    DefualtDate=str(dateTemp.strftime("%m/%d/%Y"))
    

    MapForInCBUButNotInDeductions={}
    ReconciledMap={}

    
    ##Loop over the CBU List Map
    for NetId,CBULine in MapForCBU.items():
        #First check to see if this entry is in the dues deduction list
        if NetId in MapForDeductionsList:         
            #NetId is in both lists

            #Make a reconciled Entry object
            temp=ReconciledEntry.ReconciledEntry()
            #first copy over info from CBULine to ReconciledEntry object
            temp.CopyCBUInfo(CBULine)
            temp.CopyDuesInfo(MapForDeductionsList[NetId])

            if CBULine.DuesType.lower() != MapForDeductionsList[NetId].Lines[0].WageTypeText.lower():
                ## CBU Entry needs updating
                temp.SetValueByTag("UpdatedWageType",MapForDeductionsList[NetId].Lines[0].WageTypeText)
                temp.SetValueByTag("WasUpdated","yes")
            else: # does not need updating in the CBU list 
                temp.SetValueByTag("UpdatedWageType",CBULine.DuesType)
                temp.SetValueByTag("WasUpdated","no")
            
            #now put entry in the MapFor Both Lists 
            ReconciledMap[NetId]=temp

        #Entry is in the CBU list but does not have a matching net ID in deductions
        else:
            MapForInCBUButNotInDeductions[NetId]=CBULine
            
    endfor=0



    ### Do search from the dues list.  Look to see if there are things in here 
    ### That are not in the CBU List
    for netid,deductionLine in MapForDeductionsList.items():
        if netid not in MapForCBU:
           tempKey=str(deductionLine.Lines[0].FirstName+deductionLine.Lines[0].LastName).lower()
           if tempKey not in MapForFirstLastCBU:
               temp=ReconciledEntry.ReconciledEntry()
               #There is a line in the deduction list that does
               #not match the CBU list by net id and does not match by first/last name
               temp.CopyDuesInfo(deductionLine)
               temp.SetValueByTag("OnlyInDues","yes")
               temp.SetValueByTag("UpdatedWageType",deductionLine.Lines[0].WageTypeText)
               temp.SetValueByTag("WasUpdated","no")
               temp.SetValueByTag("MSUNETID",deductionLine.Lines[0].NetId)
               temp.SetValueByTag("DuesFileNetId",deductionLine.Lines[0].NetId)
                
               ReconciledMap[netid]=temp
           else:
               pass
           #this is a entry that does not match by net id but DOES match on last/first
           #these entries were already taken care of

           
        


    #Look if the CBU lines with no NetId match a first/last name in deduction list
    for netid,line in MapForEmptyNetIdCBU.items():
        tempNameThing=line.FirstName+line.LastName
        tempNameThing=tempNameThing.lower()
        if tempNameThing in FirstNameLastNameList:
           print ("Found")

    
    Department2Members={}
    Department2FeePayers={}
    Department2NonComp={}


    
    for netid, line in ReconciledMap.items():
        key =str(line.GetValueByTag("EnrolledUnitName")).lower()

        if key in Department2Members:
            pass
        else:
            Department2Members[key]=0
            Department2FeePayers[key]=0
            Department2NonComp[key]=0

        if line.GetValueByTag("UpdatedWageType").lower() == "geu dues":
            Department2Members[key] +=1
        elif line.GetValueByTag("UpdatedWageType").lower() == "geu fees-c":
            Department2FeePayers[key] +=1
        elif line.GetValueByTag("UpdatedWageType").lower() == "geu fees-nc":
            Department2NonComp[key] +=1
        else:
            Department2NonComp[key] +=1

            
    for netid, line in ReconciledMap.items():
        for j in line.DuesPersonInfo.Lines:
            if j.WageTypeText.lower().strip() == "geu dues":
                j.WageTypeText = "GEU Dues"
            if j.WageTypeText.lower().strip() == "geu fees-c":
                j.WageTypeText = "GEU Fees-C"
            
#########################Write everything to a file#######################
    wb = Workbook()
    ws0 = wb.add_sheet('ReconciledCBU')
    
    count=0 
    for i in ReconciledEntry.ListOfKnackNames:
        ws0.write(0,count,i)
        count=count+1

    count=1
    for netid,line in ReconciledMap.items():
        if len(line.DuesPersonInfo.Lines) == 0:
            line.SetValueByTag("Date",DefualtDate)
            for i in range(len(ReconciledEntry.ListOfColumnNames)):
                ws0.write(count, i,line.GetValueByIndex(i))
            ws0.write(count,len(ReconciledEntry.ListOfColumnNames)+1,"Payroll Sheet Update")

            count=count+1
        else:
            for j in range(len(line.DuesPersonInfo.Lines)):
                line.SetDuesPersonInfo(j)#Choose one of the entries from the deduction file
                for i in range(len(ReconciledEntry.ListOfColumnNames)):
                    ws0.write(count, i,line.GetValueByIndex(i))
                ws0.write(count,len(ReconciledEntry.ListOfColumnNames)+1,"Payroll Sheet Update")
                count=count+1


    ws1 = wb.add_sheet('BlankNetIdInCBU')
    count=0
    for netid,line in MapForEmptyNetIdCBU.items():
        for i in range(32):
            ws1.write(count, i,line.GetValue(i))
        count=count+1


    # ws2 = wb.add_sheet('CBUNotDeductWithDuesStatus')
    # count=0
    # for netid,line in MapForInCBUButNotInDeductionsWithDuesStatus.iteritems():
    #     for i in range(32):
    #         ws2.write(count, i,line.GetValue(i))
    #     count=count+1

    # ws3 = wb.add_sheet('CBUNotDeductWithNoDuesStatus')
    # count=0
    # for netid,line in MapForInCBUButNotInDeductionsWithNoDuesStatus.iteritems():
    #     for i in range(32):
    #         ws3.write(count, i,line.GetValue(i))
    #     count=count+1
    

   # print len(Department2Members)," ",len(Department2FeePayers)," ",len(Department2NonComp)
    
    ws4 = wb.add_sheet('DepartStats')
    count=1
    ws4.write(0,0,"Department")
    ws4.write(0,1,"Members")
    ws4.write(0,2,"FeePayers")
    ws4.write(0,3,"Non-Compliant")
    ws4.write(0,4,"Total members")
    totalNumberOfPeople=0
    totalMembersEveryWhere=0
    for name,val in Department2Members.items():
        tot=float(Department2Members[name]+Department2FeePayers[name]+Department2NonComp[name])
        totalNumberOfPeople+=tot
        totalMembersEveryWhere+=float(Department2Members[name])
        ws4.write(count,0,name)
        if tot != 0 :
            ws4.write(count,1,(Department2Members[name]/tot) * 100)
            ws4.write(count,2,Department2FeePayers[name]/tot *100)
            ws4.write(count,3,Department2NonComp[name]/tot *100)
            ws4.write(count,4,tot )
        
        count=count+1

    ws4.write(count+1,1,totalMembersEveryWhere/totalNumberOfPeople)
    temp =os.path.split(CBU_File)[1]
    temp2=os.path.split(Dues_File)[1]
    
    temp3 = temp.split('.')
    temp4 = temp2.split('.')


    outFileName=join("ReconciledData",temp3[0]+"_"+temp4[0]+".xls")


    try: 
        wb.save(outFileName)
        #GuiWindow.DisplayMessageWindow("Created Reconciled File ")
    except IOError:
        print ("You probabaly need to close the OutPut File")
        

