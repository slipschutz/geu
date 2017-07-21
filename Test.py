#!/usr/bin/env python3




import sys


import Reconcile2

import DeductionLoader
from os import listdir
from os.path import isfile, join
import datetime

########            if str(dateTemp.date()).strip() == "2016-11-23" or str(dateTemp.date()).strip() == "2017-05-31":
def Test():

    beginDate=datetime.datetime.strptime("2016-09-01","%Y-%m-%d")
    endDate=datetime.datetime.strptime("2017-06-10","%Y-%m-%d")



    deductionFileNames = [ f for f in listdir("DeductionData") if isfile(join("DeductionData",f)) ]

    MapForAllDeductionFiles={}
    for i in deductionFileNames:
        splitName=i.split("-")
        datePart=splitName[0].strip()

        dateTemp=datetime.datetime.strptime(datePart,"%Y%m%d")
        if (dateTemp > beginDate and dateTemp<endDate):
            DeductionWrap=DeductionLoader.LoadDeduction(join("DeductionData",i))
            MapForAllDeductionFiles[dateTemp.date()]=DeductionWrap
            

    print ("Number Of Deduction Files",len(MapForAllDeductionFiles))
    SalaryTotals={}

    for date,DedWrap in MapForAllDeductionFiles.items():
        for netid,info in DedWrap.NetIdMap.items():
            ####For the netid in this deductionfile total up the lines
            ####Because remember there can be more than 1 line for a person
            ####in a file due to corrections given at bottom of file
            tempDeduction=0
            for line in info.Lines:
                tempDeduction=tempDeduction+line.DeductionAmt

            if info.Lines[0].WageTypeText=="GEU Dues":
                if netid in SalaryTotals:
                    SalaryTotals[netid]=SalaryTotals[netid]+tempDeduction/0.016
                else:
                    SalaryTotals[netid]=tempDeduction/0.016

    print("Size of Salary totals", len(SalaryTotals))

    FullCutOff=35537.
    HalfCutOff=14626.
    QuarterCutOff=8880.
    EighthCutOff=0.

    NumFull=0
    NumHalf=0
    NumQuarter=0
    NumEighth=0
    
    for netid,Total in SalaryTotals.items():
        print (netid,"Salary is ",Total)
        if Total >= FullCutOff:
            NumFull=NumFull+1
        elif Total >= HalfCutOff:
            NumHalf=NumHalf+1
        elif Total >= QuarterCutOff:
            NumQuarter=NumQuarter+1
        elif Total >=EighthCutOff:
            NumEighth=NumEighth+1

    print("Num Full",NumFull)
    print("Num Half",NumHalf)
    print("Num Quarter",NumQuarter)
    print("Num Eighth",NumEighth)

    
if __name__=='__main__':
    Test()



    
