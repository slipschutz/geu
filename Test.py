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



listOfYellowCards=["AJALAADE ",
                   "ALHOSSEI ",
                   "ALLENKR7 ",
                   "AMELIREN ",
                   "ANDERSB  ",
                   "ARMST116 ",
                   "ASHTAWY  ",
                   "ASSARZAH ",
                   "HABAZADE ",
                   "BABCO121 ",
                   "BAKERAA1 ",
                   "BAKSHISA ",
                   "BANIKASI ",
                   "BARJASTE ",
                   "BARKMANJ ",
                   "BARRE206 ",
                   "BARRYBAD ",
                   "BEAUDIN1 ",
                   "BENDER13 ",
                   "BERNARDN ",
                   "BERRIOSC ",
                   "BERRYCAM ",
                   "BETHELKA ",
                   "BICHAYNI ",
                   "BOUSLEYC ",
                   "BRATTAPH ",
                   "BRAXTON7 ",
                   "BRENTNEL ",
                   "BROOKEJ1 ",
                   "BROWNT61 ",
                   "BROWNH13 ",
                   "BRUNFELD ",
                   "BUCKPAT1 ",
                   "BUEHLCHR ",
                   "BUERGELB ",
                   "BUHROWAL ",
                   "BUNDYJAS ",
                   "CGNITASH ",
                   "CASTIAUX ",
                   "CASTROG4 ",
                   "CHAKKEDA ",
                   "CHARBO24 ",
                   "CHAUSHER ",
                   "CHAVANKA ",
                   "CHENZIXZ ",
                   "CHILDSB1 ",
                   "CHINGKA  ",
                   "CHITWANG ",
                   "CHOWDH48 ",
                   "CHUNJI1  ",
                   "CLARKC60 ",
                   "CLARKOLI ",
                   "CLEME185 ",
                   "COLASAN2 ",
                   "COLESZAC ",
                   "COLONRO1 ",
                   "MCOSBY   ",
                   "COSSEYAL ",
                   "CREDITKE ",
                   "CUEVASEV ",
                   "CUNNI290 ",
                   "DANNATTJ ",
                   "DAYTHOMA ",
                   "DESOSTOA ",
                   "DECIECH3 ",
                   "DEGERMA1 ",
                   "DELOSSA9 ",
                   "DESROC13 ",
                   "DILLMANB ",
                   "DINGXINL ",
                   "DINSMOO2 ",
                   "DIXONEL7 ",
                   "DOKESTAL ",
                   "DOYLERAS ",
                   "DUJUN1   ",
                   "DUBBSCHR ",
                   "DUNBARB3 ",
                   "EDUSEIKW ",
                   "JANELLE  ",
                   "EICKHOF6 ",
                   "ELDERRO1 ",
                   "ELLIOTME ",
                   "ELUYAEINO",
                   "ESCHMIC1 ",
                   "ESPINO66 ",
                   "ESTRAD43 ",
                   "FABERMAT ",
                   "FAKEKIMB ",
                   "FELDSCH3 ",
                   "FELIXDES ",
                   "FERGUSCA ",
                   "FIREST16 ",
                   "GAOJIA1  ",
                   "GARCHIC1 ",
                   "GAUTHI79 ",
                   "GENGPEI  ",
                   "GHADERIA ",
                   "GILETTO1 ",
                   "GLAUSEKA ",
                   "GOODVALE ",
                   "GOODEMI1 ",
                   "GREENMCK ",
                   "GREEN121 ",
                   "SGRETTER ",
                   "GRISHAMH ",
                   "GROVESA2 ",
                   "GUZHENG2 ",
                   "GUENTH8  ",
                   "GUNDLAC4 ",
                   "GUYNESSE ",
                   "MADISONH ",
                   "HANSONG7 ",
                   "HAOYUNIN ",
                   "ALANAHAR ",
                   "HARVEYT3 ",
                   "HETIANY2 ",
                   "HELLERA2 ",
                   "HERRYMAN ",
                   "HOSSAIN9 ",
                   "HOUNYOJO ",
                   "HSIAOJAN ",
                   "HUIZEN20 ",
                   "HUNTERG2 ",
                   "IQBALAS2 ",
                   "LAMARALB ",
                   "ISENEKER ",
                   "JOHN3438 ",
                   "JONESLEE ",
                   "JONESC96 ",
                   "JUERGEN3 ",
                   "KMK      ",
                   "KANVERDU ",
                   "KARIMIHA ",
                   "KEJZLARV ",
                   "KELLYSA7 ",
                   "KESHAVA2 ",
                   "KHADEMIV ",
                   "KHLILAR  ",
                   "KIMJAERI ",
                   "KIRKDAN2 ",
                   "KIRKPA48 ",
                   "KOBAYA34 ",
                   "KRANSSUS ",
                   "KREIDEL  ",
                   "KUMARPU2 ",
                   "KUMBARGE ",
                   "KUNAPULL ",
                   "CHERCHIG ",
                   "LARSON126",
                   "LEAGERRO ",
                   "LEAMANNA ",
                   "CULLINJO ",
                   "LEIJASIL ",
                   "LIRUIXUE ",
                   "LIENYU   ",
                   "LINGYINGJ",
                   "LINQINYU ",
                   "LINYICH5 ",
                   "LINSAMUE ",
                   "LITERADA ",
                   "LIULANXI ",
                   "LIULANQI ",
                   "LLOYDJO1 ",
                   "GONDHAI1 ",
                   "YANGLU3  ",
                   "LUNAGAGN ",
                   "LUNDEENJ ",
                   "LVEDTKEA ",
                   "MAGOULAS ",
                   "MAHNKES1 ",
                   "MARRAMI1 ",
                   "MARSHREB ",
                   "BRYANT22 ",
                   "MAVIMABL ",
                   "MAYLEEER ",
                   "MCCALLCA ",
                   "MCCUL121 ",
                   "MCDAVIDP ",
                   "MCKEN156 ",
                   "MCLEANT2 ",
                   "MEEKSROM ",
                   "MEHTASWA ",
                   "MEHTARO3 ",
                   "MESSELEM ",
                   "MILL2735 ",
                   "MONREALE ",
                   "MONROYMI ",
                   "MOOREBER ",
                   "MORRAKAY ",
                   "MOUAWADR ",
                   "MOULDIN1 ",
                   "MURUIPEN ",
                   "MUNDELJU ",
                   "NASERMOH ",
                   "NASHMADE ",
                   "NESBIT17 ",
                   "NGASALAT ",
                   "NICHO381 ",
                   "NISBETMI ",
                   "CHNITASH ",
                   "NJOMENEV ",
                   "NOHEUN2  ",
                   "EGBOLUCHE",
                   "OHARAPA1 ",
                   "AOKASHA  ",
                   "OLENICK  ",
                   "OSBORNR3 ",
                   "OUNAMIRA ",
                   "OVIATTRA ",
                   "PADMAN13 ",
                   "PAKDAEWO ",
                   "PALPALLA ",
                   "PANG     ",
                   "PARIGIAB ",
                   "PARISKAT ",
                   "PEFFERCH ",
                   "PEREZAMY ",
                   "PHILHOWE ",
                   "PIERCEMO ",
                   "PIERRELI ",
                   "PINGERCO ",
                   "POPEPERI ",
                   "PRCHALBE ",
                   "PRESBER2 ",
                   "QUANZHIY ",
                   "RACZKOW8 ",
                   "RAFATNED ",
                   "RAIHERKI ",
                   "RAJAEI   ",
                   "RANJANNA ",
                   "RANNCHRI ",
                   "REY440   ",
                   "RICHA939 ",
                   "RILEYEM2 ",
                   "ROSSDENN ",
                   "KROWE    ",
                   "ROWENIC2 ",
                   "ROYSTON7 ",
                   "SABUDAMA ",
                   "SALAZA63 ",
                   "SALMONRA ",
                   "SANDLE13 ",
                   "SANIEPAY ",
                   "SANTOSHA ",
                   "SANTOSKR ",
                   "SANTOSE2 ",
                   "SAVAGED5 ",
                   "SCHARNAG ",
                   "SCHIRESS ",
                   "SCHULE35 ",
                   "SELLNOWR ",
                   "SENGINJE ",
                   "SENTURKG ",
                   "ZIMMERST ",
                   "SHAPIR98 ",
                   "SHENFANG ",
                   "SHIGUILI ",
                   "SHIHANG2 ",
                   "CAPALBO  ",
                   "SINGHPR  ",
                   "SINGHSH6 ",
                   "SLOCUMCL ",
                   "SMIT2297 ",
                   "SMIT2432 ",
                   "SOLEIMA1 ",
                   "SOLHMIRZ ",
                   "SOLTANZA ",
                   "SPENC315 ",
                   "STACYSAR ",
                   "STAHLKA2 ",
                   "STEHRERY ",
                   "STOJANO8 ",
                   "SUSSMAN7 ",
                   "SWETSBRI ",
                   "SZCZYGI7 ",
                   "TANHAMAH ",
                   "TANNERM2 ",
                   "THOM1356 ",
                   "TODDROBI ",
                   "VANGIESO ",
                   "VERHAEG7 ",
                   "VOLLINGE ",
                   "WALKE668 ",
                   "WALKE678 ",
                   "WALKE670 ",
                   "WANGMIA3 ",
                   "WATSO220 ",
                   "WATSO182 ",
                   "WHEATL36 ",
                   "WILS1257 ",
                   "WUKEDI   ",
                   "WUHUIYUN ",
                   "YANSHUTI ",
                   "YARRANTO ",
                   "YOOKJI   ",
                   "YOUSIFAH ",
                   "YUJING5  ",
                   "EBZ      ",
                   "ZAMANIVA ",
                   "ZHANG317 ",
                   "ZHANG318 ",
                   "ZHANGZER ",
                   "ZHANG321 "]





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

    
    NetIdMapJan22,LastFirstMapJan22=DeductionLoader.LoadDeduction("./DeductionData/20160122-GEUDues.xlsx");
    NetIdMapFeb5,LastFirstMapFeb5=DeductionLoader.LoadDeduction("./DeductionData/20160205-GEUDues.xlsx");

    CBUMapSpring,EmptyNetId,CBUFirstLastSpring = CBULoader.LoadCBU("./CBUData/20160119-GEUCBU.xlsx")
    CBUMap2,EmptyNetId2,CBUFirstLast2 = CBULoader.LoadCBU("./CBUData/20160104-GEUCBU.xlsx")

    CBUMapFall,EmptyNetIdFall,CBUFirstLastFall = CBULoader.LoadCBU("./CBUData/20151201-GEUCBU.xlsx")

    mapOfPeopleWhoLeftUnit={}
    for key,info in CBUFirstLastFall.iteritems():
        if key not in CBUFirstLastSpring:
            mapOfPeopleWhoLeftUnit[key]=info

    print "According to december CBU and jan 19 CBU ", len(mapOfPeopleWhoLeftUnit), "who were TAs in fall but are no longer"
    
    mapOfPeopleWhoAreNew={}
    for key,info in CBUFirstLastSpring.iteritems():
        if key not in CBUFirstLastFall:
            mapOfPeopleWhoAreNew[key]=info
            
    print "According to december CBU and jan 19 CBU ", len(mapOfPeopleWhoAreNew), "are new TAs this spring"
        
    #check that people who left the unit are listed as non-union for Jan22 pay day
    count=0
    for key, info in mapOfPeopleWhoLeftUnit.iteritems():
        if key not in LastFirstMapFeb5:
            count=count+1
        else:
            print key
    print "Number of people who left according to CBUs and who were not in feb 5th pay roll (good thing)",count
    


    
    listOfQuestions=[]
    for key,info in LastFirstMapJan22.iteritems():
        if key not in CBUFirstLastSpring and info.Lines[0].EmployeeGroup=="Union":
            #print info.Lines[0].FirstName, info.Lines[0].LastName, info.Lines[0].EmployeeGroup
            listOfQuestions.append(key)

    print "number of people who were listed as in union positions on Jan22 but were not in CBU as of jan19", len(listOfQuestions)

    for key in listOfQuestions:
        if key in LastFirstMapFeb5:
            pass 

    mapOfYellowCards={}
    for i in listOfYellowCards:
        key=i.strip().lower()
        mapOfYellowCards[key]=0
    print "******************"
    for key,info in CBUMapSpring.iteritems():
        if key not in NetIdMapFeb5:
            if key in mapOfYellowCards:
                print key
    exit()
    count=0
    for i in listOfQuestions:
        if i not in CBUFirstLast2:
            count=count+1

    print count
    exit()








    print "I know how to program"
    x=0
    Reconcile("./CBUData/20160119-GEUCBU.xlsx","./DeductionData/20160122-GEUDues.xlsx",x)
    exit()

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

    












