#!/usr/bin/env python2.7



import DeductionLoader
from os import listdir
from os.path import isfile, join
import datetime

import sys
sys.path.append("xlrd-0.9.3")
import xlrd




if __name__=='__main__':

    deductionFileNames = [ f for f in listdir("DeductionData") if isfile(join("DeductionData",f)) ]
    print "Loading Entire DataBase"
    MapForAllDeductionFiles={}
    for i in deductionFileNames:
        splitName=i.split("-")
        datePart=splitName[0].strip()
        NormalMap,FirstLastNameMap=DeductionLoader.LoadDeduction(join("DeductionData",i))
        dateTemp=datetime.datetime.strptime(datePart,"%Y%m%d").date()
        MapForAllDeductionFiles[dateTemp]=FirstLastNameMap




    book2 = xlrd.open_workbook("./temp.xls")
    sh1 = book2.sheet_by_index(0)


    Answer={}
    rightOrderList=[]

    for rowNumber in range (0,sh1.nrows):
        theRow=sh1.row(rowNumber)
        firstName=str(theRow[1].value.strip())
        lastName=str(theRow[2].value.strip())
        firstLastKey=firstName+lastName
        firstLastKey=firstLastKey.lower()
        rightOrderList.append((firstName,lastName))
        for date,innermap in MapForAllDeductionFiles.iteritems():
            if firstLastKey in innermap:

                Answer[(firstName,lastName)]=innermap[firstLastKey].NetId
                break
            else:
                Answer[(firstName,lastName)]="NotThere"

    for thing in rightOrderList:
        print thing[0],thing[1],Answer[thing]

            


