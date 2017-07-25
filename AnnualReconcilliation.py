#!/usr/bin/env python3






import DeductionLoader
from os import listdir
from os.path import isfile, join
import datetime


class PerCapParameters:
    def __init__(self):
        PayLevels=["FullTime","HalfTime","QuarterTime","EighthTime"]
        Things=["CutOff","AFTMemPerCap","AFTFeePerCap","AFTMIMemPerCap","AFTMIFeePerCap"]
        for p in PayLevels:
            for th in Things:
                s="{0}_{1}".format(p,th)
                setattr(self,s,0)



def DoAnnualReconcilliation(deductionFileNames,TheParams):
    # PayLevels=["FullTime","HalfTime","QuarterTime","EighthTime"]
    # Things=["CutOff","AFTMemPerCap","AFTFeePerCap","AFTMIMemPerCap","AFTMIFeePerCap"]
    # for p in PayLevels:
    #     for th in Things:
    #         s="{0}_{1}".format(p,th)
    #         print(s,getattr(TheParams,s))
    # print("----")
    
    # return

    MapForAllDeductionFiles={}
    for i in deductionFileNames:
        splitName=i.split("-")
        datePart=splitName[0].strip()

        dateTemp=datetime.datetime.strptime(datePart,"%Y%m%d")
        DeductionWrap=DeductionLoader.LoadDeduction(join("DeductionData",i))
        MapForAllDeductionFiles[dateTemp]=DeductionWrap
            

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

    FullCutOff=TheParams.FullTime_CutOff
    HalfCutOff=TheParams.HalfTime_CutOff
    QuarterCutOff=TheParams.QuarterTime_CutOff
    EighthCutOff=TheParams.EighthTime_CutOff


    FullTimeMap={}
    HalfTimeMap={}
    QuarterTimeMap={}
    EighthTimeMap={}
    
    for netid,Total in SalaryTotals.items():
        if Total >= FullCutOff:
            FullTimeMap[netid]=Total
        elif Total >= HalfCutOff:
            HalfTimeMap[netid]=Total
        elif Total >= QuarterCutOff:
            QuarterTimeMap[netid]=Total
        elif Total >=EighthCutOff:
            EighthTimeMap[netid]=Total


    FullDuesAFT=TheParams.FullTime_AFTMemPerCap
    HalfDuesAFT=TheParams.HalfTime_AFTMemPerCap
    QuarterDuesAFT=TheParams.QuarterTime_AFTMemPerCap
    EighthDuesAFT=TheParams.EighthTime_AFTMemPerCap


    monthChecker={}

    orderedDateList=[]
    for date,DedWrap in MapForAllDeductionFiles.items():
        orderedDateList.append(date)

    orderedDateList= sorted(orderedDateList)

    total=0
    for date in orderedDateList:
        DedWrap=MapForAllDeductionFiles[date]
        NumFull=0
        NumHalf=0
        NumQuarter=0
        NumEighth=0

        for netid,info in DedWrap.NetIdMap.items():
            if netid in FullTimeMap:
                NumFull=NumFull+1
            elif netid in HalfTimeMap:
                NumHalf=NumHalf+1
            elif netid in QuarterTimeMap:
                NumQuarter=NumQuarter+1
            elif netid in EighthTimeMap:
                NumEighth=NumEighth+1
        
        month=date.month 
        if month not in monthChecker:
            monthChecker[month]=1
        elif monthChecker[month]==1:
            monthChecker[month]=2
            Orig = (NumFull +NumHalf+NumQuarter+NumEighth)*QuarterDuesAFT
            New = NumFull*FullDuesAFT+NumHalf*HalfDuesAFT + NumQuarter*QuarterDuesAFT + NumEighth*EighthDuesAFT
            print(date,"Full ",NumFull,"Half",NumHalf,"Quarter",NumQuarter,"Eighth",NumEighth,"Orig {0:5.2f}".format(Orig)," new {0:5.2f}".format(New))
            total=total+(new-Orig)

    
if __name__=='__main__':
    Test()



    
