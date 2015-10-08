#!/usr/bin/env python2.7

import sys
from PyQt4 import uic, QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import LoadDeductionDataBase
import LoadCBUDataBase
import LoadReconciledDataBase

import DeductionLoader
import CBULoader

from os.path import join

import matplotlib.pyplot as plt

from Reconcile import Reconcile


class TempInfo:
    def __init__(self):
        self.ListOfDates=[]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__=='__main__':

    print "I know how to program"

    NetIdMapSept4,LastFirstMapSept4=DeductionLoader.LoadDeduction("./DeductionData/20150904-GEUDues.xlsx");
    NetIdMapSept18,LastFirstMapSept18=DeductionLoader.LoadDeduction("./DeductionData/20150918-GEUDues.xlsx");
    NetIdMapOct2,LastFirstMapOct2=DeductionLoader.LoadDeduction("./DeductionData/20151002-GEUDues.xlsx");

    NetIdMapMay15,LastFirstMapMay15=DeductionLoader.LoadDeduction("./DeductionData/20150515-GEUDues.xlsx");

    CBUMapSept,trash,trash1 = CBULoader.LoadCBU("./CBUData/20150901-GEUCBU.xlsx")
    
    
    ##First find all the people who were in 5/15 and september CBU list
    mapOfPeopleToCheck={}
    for netid,DeductionInfo in NetIdMapMay15.iteritems():
        if netid in CBUMapSept:
            mapOfPeopleToCheck[netid]=DeductionInfo



    print "There are ", len(mapOfPeopleToCheck), "who were TAs last may and are in SEPT CBU List"

    #loop over all the deductiions maps and build a map of dates
    mapOfPayDays={}
    for netid,info in NetIdMapSept4.iteritems():
        if netid in mapOfPayDays:
            for x in info.Lines:
                mapOfPayDays[netid].ListOfDates.append(x.PayDay)
        else:
            temp111=TempInfo()
            for x in info.Lines:
                temp111.ListOfDates.append(x.PayDay)
            mapOfPayDays[netid]=temp111


    for netid,info in NetIdMapSept18.iteritems():
        if netid in mapOfPayDays:
            for x in info.Lines:
                mapOfPayDays[netid].ListOfDates.append(x.PayDay)
        else:
            temp111=TempInfo()
            for x in info.Lines:
                temp111.ListOfDates.append(x.PayDay)
            mapOfPayDays[netid]=temp111

    for netid,info in NetIdMapOct2.iteritems():
        if netid in mapOfPayDays:
            for x in info.Lines:
                mapOfPayDays[netid].ListOfDates.append(x.PayDay)
        else:
            temp111=TempInfo()
            for x in info.Lines:
                temp111.ListOfDates.append(x.PayDay)
            mapOfPayDays[netid]=temp111





    for netid, info in mapOfPayDays.iteritems():
        print "VVVVVVVVVVV"
        print netid
        info.ListOfDates.sort()
        for x in info.ListOfDates:
            print x
        print"^^^^^^^^^^^"

    total=0
    for netid,DeductionInfo in mapOfPeopleToCheck.iteritems():
        if DeductionInfo.Lines[0].WageTypeText=="GEU Fees-C":
            if netid not in mapOfPayDays:
                money = CBUMapSept[netid].PayRate
                if is_number(money):
                    money=money*0.0144*3
                    #total=total+money
                else:
                    money="Salary not given in CBU"
                #print netid,",",DeductionInfo.Lines[0].FirstName,",",DeductionInfo.Lines[0].LastName,",",DeductionInfo.Lines[0].WageTypeText,",",money
            else: ##they are someweher in the lists
                if len(mapOfPayDays[netid].ListOfDates) == 1:
                    money = CBUMapSept[netid].PayRate
                    if is_number(money):
                        money=money*0.0144*2
                        total=total+money
                    else:
                        money="Salary not given in CBU"
                    s=netid
                    s=s+","+DeductionInfo.Lines[0].FirstName+"," +DeductionInfo.Lines[0].LastName+","+DeductionInfo.Lines[0].WageTypeText+","+DeductionInfo.Lines[0].EmployeeGroup
                    for x in mapOfPayDays[netid].ListOfDates:
                        s=s+","+str(x.date())
                    s=s+","+ str(money)
                    print s
                
            
    print "total is ",total
        



    exit()

    ddd=0
    Reconcile("./CBUData/20150901-GEUCBU.xlsx","./DeductionData/20150918-GEUDues.xlsx",ddd)


    print "I know how to program"



    fileName1="./DeductionData/20150904-GEUDues.xlsx"
    fileName2="./DeductionData/20150918-GEUDues.xlsx"






    NormalMap2,LastFirstNameMap=DeductionLoader.LoadDeduction(fileName2);

    CBUMap,trash,trash1 = CBULoader.LoadCBU("./CBUData/20150901-GEUCBU.xlsx")


    print len(NormalMap1)
    print len(NormalMap2)
    

    
    listOfPeople={}
    for netid,info in NormalMap1.iteritems():
        if netid in NormalMap2:
            pass
        else:
            if info.EmployeeGroup=="Union":
                listOfPeople[netid]=info


    for netid,info in listOfPeople.iteritems():
        if netid in CBUMap:
            print netid," ",info.FirstName," ",info.LastName," ",info.WageTypeText
        else:
            pass

    NormalMap2,LastFirstNameMap=DeductionLoader.LoadDeduction(fileName2);

    for netid,thing in NormalMap2.iteritems():
        if len(thing.Lines) !=1:
            print "VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"
            for x in thing.Lines:
                x.PrintShort()
            print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

    # NormalMap1,LastFirstNameMap=DeductionLoader.LoadDeduction(fileName1);
    # NormalMap2,LastFirstNameMap=DeductionLoader.LoadDeduction(fileName2);

    # CBUMap,trash,trash1 = CBULoader.LoadCBU("./CBUData/20150901-GEUCBU.xlsx")

    # print len(NormalMap1)
    # print len(NormalMap2)
    

    
    # listOfPeople={}
    # for netid,info in NormalMap1.iteritems():
    #     if netid in NormalMap2:
    #         pass
    #     else:
    #         if info.EmployeeGroup=="Union":
    #             listOfPeople[netid]=info


    # for netid,info in listOfPeople.iteritems():
    #     if netid in CBUMap:
    #         print netid," ",info.FirstName," ",info.LastName," ",info.WageTypeText
    #     else:
    #         pass

    












