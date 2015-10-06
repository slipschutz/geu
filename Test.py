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




if __name__=='__main__':
    ddd=0
    Reconcile("./CBUData/20150901-GEUCBU.xlsx","./DeductionData/20150918-GEUDues.xlsx",ddd)


    print "I know how to program"


    fileName1="./DeductionData/20150904-GEUDues.xlsx"
    fileName2="./DeductionData/20150918-GEUDues.xlsx"


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
    












