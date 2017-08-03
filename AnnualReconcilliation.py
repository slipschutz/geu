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



def ProcessSalaryList(SalaryTotals,TheParams,MapForAllDeductionFiles,theName):

    FullCutOff=TheParams.FullTime_CutOff
    HalfCutOff=TheParams.HalfTime_CutOff
    QuarterCutOff=TheParams.QuarterTime_CutOff
    EighthCutOff=TheParams.EighthTime_CutOff


    FullRateAFT=getattr(TheParams,"FullTime_AFT{0}PerCap".format(theName))
    HalfRateAFT=getattr(TheParams,"HalfTime_AFT{0}PerCap".format(theName))
    QuarterRateAFT=getattr(TheParams,"QuarterTime_AFT{0}PerCap".format(theName))
    EighthRateAFT=getattr(TheParams,"EighthTime_AFT{0}PerCap".format(theName))


    FullRateAFTMI=getattr(TheParams,"FullTime_AFTMI{0}PerCap".format(theName))
    HalfRateAFTMI=getattr(TheParams,"HalfTime_AFTMI{0}PerCap".format(theName))
    QuarterRateAFTMI=getattr(TheParams,"QuarterTime_AFTMI{0}PerCap".format(theName))
    EighthRateAFTMI=getattr(TheParams,"EighthTime_AFTMI{0}PerCap".format(theName))

    
    
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
            totalNumberOfPeople=(NumFull +NumHalf+NumQuarter+NumEighth)
            Orig = totalNumberOfPeople*QuarterRateAFT
            New = NumFull*FullRateAFT+  NumHalf*HalfRateAFT +   NumQuarter*QuarterRateAFT +   NumEighth*EighthRateAFT
            OrigMI = totalNumberOfPeople*QuarterRateAFTMI
            NewMI = NumFull*FullRateAFTMI+  NumHalf*HalfRateAFTMI +   NumQuarter*QuarterRateAFTMI +   NumEighth*EighthRateAFTMI

            print(date,"Full ",NumFull,"Half",NumHalf,"Quarter",NumQuarter,"Eighth",NumEighth,"totPeps",totalNumberOfPeople,"Orig {0:5.2f}".format(Orig)," new {0:5.2f}".format(New),"OrigMI {0:5.2f}".format(OrigMI),"new MI {0:5.2f}".format(NewMI))


            total=total+(New-Orig) +(NewMI-OrigMI)

    print (total)
    

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
    SalaryTotalsFees={}

    for date,DedWrap in MapForAllDeductionFiles.items():
        for netid,info in DedWrap.NetIdMap.items():
            ####For the netid in this deductionfile total up the lines
            ####Because remember there can be more than 1 line for a person
            ####in a file due to corrections given at bottom of file
            tempDeduction=0
            for line in info.Lines:
                tempDeduction=tempDeduction+line.DeductionAmt
                

            if date.date()=="2017-02-03":
                factor=2
            else:
                factor=1

            if info.Lines[0].WageTypeText=="GEU Dues":
                rate=0.016*factor
                if netid in SalaryTotals:
                    SalaryTotals[netid]=SalaryTotals[netid]+tempDeduction/rate
                else:
                    SalaryTotals[netid]=tempDeduction/rate

            elif info.Lines[0].WageTypeText=="GEU Fees-C":
                rate=0.0144*factor
                if netid in SalaryTotalsFees:
                    SalaryTotalsFees[netid]=SalaryTotalsFees[netid]+tempDeduction/rate
                else:
                    SalaryTotalsFees[netid]=tempDeduction/rate

                    
    print("Size of Salary totals", len(SalaryTotals))
    print("Size of Salary totals fees", len(SalaryTotalsFees))

    ProcessSalaryList(SalaryTotals,TheParams,MapForAllDeductionFiles,"Mem")
    ProcessSalaryList(SalaryTotalsFees,TheParams,MapForAllDeductionFiles,"Fee")
    return





















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
            total=total+(New-Orig)

    print (total)
    
if __name__=='__main__':
    Test()



    
