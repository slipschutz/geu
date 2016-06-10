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

import datetime

from Reconcile import Reconcile

dict ={"ZIMMERST":"09/22/2015",
"YUJING5	":"09/24/2015",
"YUJING5	":"09/24/2015",
"YOUSIFAH":"08/24/2015",
"YOOKJI	":"08/23/2015",
"YARRANTO":"10/07/2015",
"WUHUIYUN":"08/23/2015",
"WITCOMBE":"08/29/2015",
"WILS1257":"09/21/2015",
"WHEATL36":"08/19/2015",
"WATSO220":"08/19/2015",
"WALKE670":"08/27/2015",
"WALKE668":"08/27/2015",
"VANCEKZ2":"08/17/2015",
"TODDROBI":"08/23/2015",
"THOM1356":"08/23/2015",
"TANNERM2":"08/31/2015",
"SZCZYGI7":"08/27/2015",
"SWETSBRI":"08/19/2015",
"SUSSMAN7":"09/08/2015",
"STEHRERY":"08/31/2015",
"STAHLKA2":"08/17/2015",
"SPENC315":"08/23/2015",
"SOLEIMA1":"09/28/2015",
"SMIT2432":"08/28/2015",
"SLOCUMCL":"08/27/2015",
"SINGSH6	":"08/31/2015",
"SINGHPR	":"08/23/2015",
"SHIHANG2":"10/09/2015",
"SHENFANG":"10/08/2015",
"SHAPIR98":"08/27/2015",
"SGRETTER":"08/24/2015",
"SENGINJE":"08/31/2015",
"SELLNOWR":"08/27/2015",
"SCHULE35":"08/26/2015",
"SCHIRESS":"08/17/2015",
"SAVAGED5":"08/27/2015",
"SANIEPAY":"09/16/2015",
"SANDLE13":"09/10/2015",
"SALAZA63":"09/10/2015",
"SABUDAMA":"08/27/2015",
"ROYSTON7":"08/23/2015",
"ROYPROTE":"08/29/2015",
"ROWENIC2":"08/19/2015",
"ROSSDENN":"09/24/2015",
"ROBIN994":"09/05/2015",
"RICHA934":"08/29/2015",
"RICHA934":"08/29/2015",
"REY440	":"08/29/2015",
"RANJANNA":"08/23/2015",
"RAJAEI	":"08/23/2015",
"RAIHERKI":"08/23/2015",
"RAFATNED":"08/23/2015",
"RACZKOW8":"08/29/2015",
"PRESBER2":"08/27/2015",
"PRCHALBE":"08/27/2015",
"PRABHANU":"09/24/2015",
"PIERRELI":"08/27/2015",
"PIERCEMO":"08/19/2015",
"PHILHOWE":"08/23/2015",
"PHAMTHA1":"09/24/2015",
"PEREZAMY":"08/29/2015",
"PARISKAT":"09/16/2015",
"PARIGIAB":"09/08/2015",
"PAREDE12":"08/31/2015",
"PANG	":"09/08/2015",
"PADMAN13":"08/26/2015",
"OVIATTRA":"08/27/2015",
"OSBORNR3":"08/27/2015",
"OLENICK	":"08/23/2015",
"OHARAPA1":"10/09/2015",
"NOHEUN2	":"08/31/2015",
"NICHO381":"08/31/2015",
"NGASALAT":"10/01/2015",
"NGASALAT":"10/01/2015",
"NESBIT17":"08/27/2015",
"NASHMADE":"08/23/2015",
"NASERMOH":"09/22/2015",
"MURUIPEN":"10/07/2015",
"MUNIRALI":"09/24/2015",
"MOULDIN1":"08/27/2015",
"MORRAKAY":"08/31/2015",
"MOOREBER":"10/07/2015",
"MONROYMI":"08/27/2015",
"MONREALE":"08/31/2015",
"MILL2735":"08/29/2015",
"MESSEIEM":"08/23/2015",
"MEHTASWA":"08/23/2015",
"MCOSBY	":"08/27/2015",
"MCKEN156":"09/10/2015",
"MCDAVIDP":"09/15/2015",
"MCCALLCA":"10/01/2015",
"MCCALLCA":"10/01/2015",
"MAYLEEER":"09/08/2015",
"MARSHREB":"08/31/2015",
"MARRAMI1":"08/23/2015",
"MANSKEJI":"08/19/2015",
"MAITITIA":"09/24/2015",
"MAHNKES1":"08/27/2015",
"MAGOULAS":"10/07/2015",
"MADISONH":"09/29/2015",
"LVEDTKEA":"08/23/2015",
"LUNAGAGN":"08/31/2015",
"LLOYDJO1":"09/04/2015",
"LIUSHIZH":"08/23/2015",
"LIULANXI":"08/27/2015",
"LIULANQI":"09/30/2015",
"LINQINYU":"08/23/2015",
"LINGYING":"08/23/2015",
"LEIJASIL":"08/23/2015",
"LEAMANNA":"08/27/2015",
"LEAGERRO":"08/27/2015",
"LARSON12":"08/31/2015",
"LANEELI1":"09/08/2015",
"LAMARALB":"08/19/2015",
"KUNAPULL":"08/23/2015",
"KUMARPU2":"09/22/2015",
"KROWE	":"10/01/2015",
"KREIDEL	":"08/23/2015",
"KRANSSUS":"09/11/2015",
"KORNELI1":"08/29/2015",
"KOBAYA34":"08/17/2015",
"KMK	":"08/29/2015",
"KIRKPA48":"08/27/2015",
"KIMJAERI":"08/23/2015",
"KHLILAR	":"08/23/2015",
"KHADEMIV":"09/24/2015",
"KESHAVA2":"10/07/2015",
"KELLYSA7":"08/27/2015",
"KEJZLARV":"09/15/2015",
"KEJZLARV":"09/10/2015",
"KEJZLARV":"09/10/2015",
"KARIMIHA":"09/10/2015",
"KARIMIHA":"09/10/2015",
"KANVERDU":"10/01/2015",
"JUERGEN3":"09/08/2015",
"JONESLEE":"08/17/2015",
"JOHN3438":"08/28/2015",
"JIANGY01":"08/17/2015",
"JARVIESE":"08/19/2015",
"ISENEKER":"09/08/2015",
"IQBALAS2":"08/23/2015",
"HUNTERG2":"08/17/2015",
"HSIAOJAN":"08/27/2015",
"HOUNYOJO":"08/31/2015",
"HOSSAIN9":"08/23/2015",
"HERRYMAN":"10/01/2015",
"HERRYMAN":"10/01/2015",
"HARVEYT3":"08/27/2015",
"HARDERJ3":"08/17/2015",
"HAISLIPA":"08/27/2015",
"HABAZADE":"08/23/2015",
"GUZHENG2":"08/27/2015",
"GUYNESSE":"08/27/2015",
"GUNDLAC4":"08/29/2015",
"GUENTH8	":"10/01/2015",
"GROVESA2":"08/31/2015",
"GRISHAMH":"08/19/2015",
"GREENWH	":"08/23/2015",
"GREENMCK":"08/27/2015",
"GREEN121":"08/19/2015",
"GOODVALE":"08/23/2015",
"GONDHAI1":"08/28/2015",
"GLAUSEKA":"08/19/2015",
"GHADERIA":"09/25/2015",
"GAUTHI79":"08/29/2015",
"GARCHIC1":"08/27/2015",
"FIREST16":"08/26/2015",
"FERGUSCA":"08/31/2015",
"FELIXDES":"08/18/2015",
"FAKEKIMB":"08/31/2015",
"ESTRAD43":"08/27/2015",
"ESPINO66":"08/27/2015",
"ESCHMIC1":"08/27/2015",
"ELUYAEIN":"08/23/2015",
"EICKHOF6":"08/29/2015",
"EGBOLUCH":"08/29/2015",
"EDUSEIKW":"08/29/2015",
"DUNBARB3":"08/28/2015",
"DOYLERAS":"08/27/2015",
"DIXONEL7":"08/26/2015",
"DINSMOO2":"08/27/2015",
"DINGXINL":"10/08/2015",
"DHEBARYA":"08/27/2015",
"DESOSTOA":"08/26/2015",
"DELIMAJO":"08/23/2015",
"DEGERMA1":"08/24/2015",
"DECIECH3":"08/31/2015",
"DANNATTJ":"10/08/2015",
"CUNNI290":"08/23/2015",
"CULLINJO":"08/31/2015",
"CUEVASEV":"08/26/2015",
"CREDITKE":"08/27/2015",
"COSSEYAL":"08/31/2015",
"COLONRO1":"08/29/2015",
"COLESZAC":"08/30/2015",
"COLASAN2":"09/22/2015",
"CLEME185":"08/27/2015",
"CLARKOLI":"08/31/2015",
"CLARKC60":"08/23/2015",
"CHOWDH48":"09/24/2015",
"CHOIJEO6":"08/19/2015",
"CHNITASH":"08/23/2015",
"CHITWANG":"08/29/2015",
"CHINGKA	":"08/23/2015",
"CHILDSB1":"09/08/2015",
"CHERCHIG":"08/23/2015",
"CHENZIXZ":"08/23/2015",
"CHAVANKA":"08/27/2015",
"CHAUSHER":"10/09/2015",
"CHARBO24":"10/01/2015",
"CHAKRA34":"09/24/2015",
"CHAKKEDA":"09/24/2015",
"CGNITASH":"09/10/2015",
"CASTROG4":"09/24/2015",
"CASAGRA3":"08/29/2015",
"CANTFIND":"08/28/2015",
"BUNDYJAS":"08/31/2015",
"BUHROWAL":"09/17/2015",
"BUERGELB":"10/01/2015",
"BUEHLCHR":"08/31/2015",
"BUCKPAT1":"08/27/2015",
"BRYANT22":"08/27/2015",
"BROWNT61":"08/27/2015",
"BROWNH13":"08/27/2015",
"BROOKEJ1":"08/29/2015",
"BRENTNEL":"08/27/2015",
"BRAXTON7":"08/27/2015",
"BRATTAPH":"08/27/2015",
"BRASSELS":"08/17/2015",
"BRASSELS":"09/17/2015",
"BICHAYNI":"09/08/2015",
"BETHELKA":"08/23/2015",
"BERRYCAM":"08/31/2015",
"BERRIOSC":"09/10/2015",
"BERNARDN":"08/29/2015",
"BENDER12":"08/24/2015",
"BEAUDIN1":"09/19/2015",
"BARRYBAD":"08/27/2015",
"BARKMANJ":"08/26/2015",
"BALAAHME":"09/24/2015",
"BAKSHISA":"08/28/2015",
"BABCO121":"08/27/2015",
"ASHTAWY	":"10/09/2015",
"ARNDTLIS":"08/29/2015",
"ARMST116":"09/10/2015",
"AOKASHA	":"08/23/2015",
"ANDERSB	":"08/27/2015",
"ALLENKR7":"08/17/2015",
"ALHOSSEI":"09/24/2015",
"ALANAHAR":"08/29/2015",
"AJALAADE":"10/07/2015"}



def PrintThing(List):
    sept4="Missing"
    sept18="Missing"
    oct2="Missing"
    oct16="Missing"
    
    for x in List:
        temp=datetime.datetime.strptime(x,"%Y-%m-%d")
        if temp.day==4:
            sept4="Paid"
        elif temp.day==18:
            sept18="Paid"
        elif temp.day==2:
            oct2="Paid"
        elif temp.day==16:
            oct16="Paid"

    if sept4=="Paid" and sept18=="Paid" and oct2=="Paid" and oct16=="Paid":
        ignore=True
    else:
        ignore=False
    
    s=sept4 +"," + sept18 +"," +oct2 +","+oct16
    return s,ignore


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
    NetIdMapOct16,LastFirstMapOct16=DeductionLoader.LoadDeduction("./DeductionData/20151016-GEUDues.xlsx");

    NetIdMapMay15,LastFirstMapMay15=DeductionLoader.LoadDeduction("./DeductionData/20150515-GEUDues.xlsx");

    CBUMapSept,trash,trash1 = CBULoader.LoadCBU("./CBUData/20151001-GEUCBU.xlsx")
    
    
    ##First find all the people who were are in the list  and september CBU list
    mapOfPeopleToCheck={}
    for netid,Date in dict.iteritems():
        if netid.strip().lower() in CBUMapSept:
            dateTemp=datetime.datetime.strptime(Date.strip(),"%m/%d/%Y")
            mapOfPeopleToCheck[netid.strip().lower()]=dateTemp




    print "length of check people ",len(mapOfPeopleToCheck)

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


    for netid,info in NetIdMapOct16.iteritems():
        if netid in mapOfPayDays:
            for x in info.Lines:
                mapOfPayDays[netid].ListOfDates.append(x.PayDay)
        else:
            temp111=TempInfo()
            for x in info.Lines:
                temp111.ListOfDates.append(x.PayDay)
            mapOfPayDays[netid]=temp111





    for netid, info in mapOfPayDays.iteritems():
        info.ListOfDates.sort()
  

    for netid,date in mapOfPeopleToCheck.iteritems():
        dateTemp=datetime.datetime.strptime("09/30/2015","%m/%d/%Y")
        dateTemp2=datetime.datetime.strptime("09/01/2015","%m/%d/%Y")
        
        if date <=dateTemp and date >=dateTemp2:
            if netid in mapOfPayDays:
                s,ignore=PrintThing(mapOfPayDays[netid].ListOfDates)
                if ignore==False:
                    print date.date(),",",netid,",",CBUMapSept[netid].FirstName,",",CBUMapSept[netid].LastName,",",s
            else:
                print date.date(),",",netid,",",CBUMapSept[netid].FirstName,",",CBUMapSept[netid].LastName,",","Missing,Missing,Missing,Missing"

            

    exit()














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

    












