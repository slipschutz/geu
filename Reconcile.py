#!/usr/bin/env python3




import sys
sys.path.append("xlwt-0.7.5")
#sys.path.append("openpyxl-2.2.2")

from xlwt import *

from CBULine import *
from DeductionLine import *

import CBULoader
import DeductionLoader




def Reconcile(CBU_File,Dues_File,GuiWindow):
    MapForCBU,MapForEmptyNetIdCBU=  CBULoader.LoadCBU(CBU_File) # returns MapForCbu then MapForEmptyNetIdCbu
    MapForDeductionsList,FirstNameLastNameList= DeductionLoader.LoadDeduction(Dues_File)#returns MapForDeductonsList
    
#    print MapForDeductionsList
    

    MapForInCBUButNotInDeductions={}
    MapForInBothLists={}

    for NetId,CBULine in MapForCBU.iteritems():
        if NetId in MapForDeductionsList:         #NetId is in both lists
            if CBULine.DuesType != MapForDeductionsList[NetId].WageTypeText: ## CBU Entry needs updating
                CBULine.UpdatedDuesType =MapForDeductionsList[NetId].WageTypeText
                CBULine.WasUpdated="yes"
            else: # does not need updating in the CBU list 
                CBULine.UpdatedDuesType =CBULine.DuesType
                CBULine.WasUpdated="no"
            #now put entry in the MapFor Both Lists 
            MapForInBothLists[NetId]=CBULine

        else: #Entry is in CBU list but _NOT_ in deductions list
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

        if line.UpdatedDuesType == "geu dues":
            Department2Members[key] +=1
        elif line.UpdatedDuesType == "geu fees-c":
            Department2FeePayers[key] +=1
        elif line.UpdatedDuesType == "geu fees-nc":
            Department2NonComp[key] +=1

    
#########################Write everything to a file#######################
    wb = Workbook()
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
        if tot != 0 :
            ws4.write(count,1,(Department2Members[name]/tot) * 100)
            ws4.write(count,2,Department2FeePayers[name]/tot *100)
            ws4.write(count,3,Department2NonComp[name]/tot *100)
            ws4.write(count,4,tot )

        count=count+1


    temp =CBU_File.split('/')
    temp2=Dues_File.split('/')
    
    temp3 = temp[2].split('.')
    temp4 = temp2[2].split('.')

    outFileName="./ReconciledData/"+temp3[0]+"_"+temp4[0]+".xls"


    try: 
        wb.save(outFileName)
        #GuiWindow.DisplayMessageWindow("Created Reconciled File ")
    except IOError:
        print "You probabaly need to close the OutPut File"

        

