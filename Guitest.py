#!/usr/bin/env python2.7

import sys
from PyQt4 import uic, QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import LoadDeductionDataBase
import LoadCBUDataBase
import LoadReconciledDataBase

from os import listdir
from os.path import isfile, join

from AnnualReconcilliation import *

from Reconcile2 import Reconcile
# Load the GUI class from the .ui file
(Ui_MainWindow, QMainWindow) = uic.loadUiType('Test.ui')

# Define a class for the main window.
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # Initialize the GUI itself
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.DuesFileForReconcile="nothing"
        self.CBUFileForReconcile="nothing"



        self.DeductionData =0#LoadDeductionDataBase.LoadDataBase(self)
        self.CBUData = 0#LoadCBUDataBase.LoadDataBase(self)
        self.ReconciledData =0#LoadReconciledDataBase.LoadDataBase(self)


        for f in listdir("DeductionData"):
            if isfile(join("DeductionData",f)):
                temp=QListWidgetItem()
                temp.setText(f)
                tempFont=QFont()
                tempFont.setPointSize(16)
                temp.setFont(tempFont)
                self.ui.DuesListWidget.addItem(temp)

        for f in listdir("CBUData"):
            if isfile(join("CBUData",f)):
                temp=QListWidgetItem()
                temp.setText(f)
                tempFont=QFont()
                tempFont.setPointSize(16)
                temp.setFont(tempFont)
                self.ui.CBUListWidget.addItem(temp)

        
        


        # Connect a function to be run when a button is pressed.
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.DuesListWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ui.DuesListWidget.itemDoubleClicked.connect(self.ItemDoubleClickedInDuesFileList)
        self.ui.ToggleButton.clicked.connect(self.ToggleButtonClicked)


        
        self.ui.ReconcileButton.clicked.connect(self.ReconcileButtonClicked)
        

        self.ui.CBUListWidget.itemDoubleClicked.connect(self.ItemDoubleClickedInCBUFileList)

        self.ui.SelectedFilesForAnnualRec.itemDoubleClicked.connect(self.SelectedFilesClicked)


        self.ui.ReconcileEveryThingButton.clicked.connect(self.ReconcileEveryThingButton)
        self.ui.SearchLine.editingFinished.connect(self.ASearchWasDone)


        self.ui.FullTime_CutOff.setText("37642")
        self.ui.HalfTime_CutOff.setText("15157")
        self.ui.QuarterTime_CutOff.setText("9203")
        self.ui.EighthTime_CutOff.setText("0")

        self.ui.FullTime_AFTMemPerCap.setText("19.03")
        self.ui.HalfTime_AFTMemPerCap.setText("9.52")
        self.ui.QuarterTime_AFTMemPerCap.setText("4.62")
        self.ui.EighthTime_AFTMemPerCap.setText("2.38")

        self.ui.FullTime_AFTFeePerCap.setText("13.98")
        self.ui.HalfTime_AFTFeePerCap.setText("6.99")
        self.ui.QuarterTime_AFTFeePerCap.setText("3.50")
        self.ui.EighthTime_AFTFeePerCap.setText("1.75")


        self.ui.FullTime_AFTMIMemPerCap.setText("18.45")
        self.ui.HalfTime_AFTMIMemPerCap.setText("9.23")
        self.ui.QuarterTime_AFTMIMemPerCap.setText("4.62")
        self.ui.EighthTime_AFTMIMemPerCap.setText("4.62")
        
        self.ui.FullTime_AFTMIFeePerCap.setText("16.22")
        self.ui.HalfTime_AFTMIFeePerCap.setText("8.11")
        self.ui.QuarterTime_AFTMIFeePerCap.setText("4.06")
        self.ui.EighthTime_AFTMIFeePerCap.setText("4.06")


        
        self.ui.FullTime_CutOff.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.HalfTime_CutOff.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.QuarterTime_CutOff.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.EighthTime_CutOff.editingFinished.connect(self.UpdatePerCapInfo)

        self.ui.FullTime_AFTMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.HalfTime_AFTMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.QuarterTime_AFTMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.EighthTime_AFTMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)

        self.ui.FullTime_AFTFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.HalfTime_AFTFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.QuarterTime_AFTFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.EighthTime_AFTFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)

        
        self.ui.FullTime_AFTMIMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.HalfTime_AFTMIMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.QuarterTime_AFTMIMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.EighthTime_AFTMIMemPerCap.editingFinished.connect(self.UpdatePerCapInfo)

        self.ui.FullTime_AFTMIFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.HalfTime_AFTMIFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.QuarterTime_AFTMIFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)
        self.ui.EighthTime_AFTMIFeePerCap.editingFinished.connect(self.UpdatePerCapInfo)


        self.ui.runAnnualRec.clicked.connect(self.RunAnnualRec)

        self.ThePerCapParameters=PerCapParameters()
        self.UpdatePerCapInfo()

        self.DatesToSkip=[]
        self.DatesToDouble=[]

        
    end_init=0

    def SelectedFilesClicked(self,TheItem):
        if self.ui.skipButton.isChecked():
            if TheItem.font().bold():
                tempFont=TheItem.font()
                tempFont.setBold(False)
                TheItem.setFont(tempFont)
                self.DatesToSkip.remove(TheItem.text())
            else:
                tempFont=TheItem.font()
                tempFont.setBold(True)
                TheItem.setFont(tempFont)
                self.DatesToSkip.append(TheItem.text())
        elif self.ui.doubleButton.isChecked():
            if TheItem.backgroundColor()==QColor("yellow"):
                temp=QColor("white")
                TheItem.setBackgroundColor(temp)
                self.DatesToDouble.remove(TheItem.text())
            else:
                temp=QColor("yellow")
                TheItem.setBackgroundColor(temp)
                self.DatesToDouble.append(TheItem.text())

    
    def ToggleButtonClicked(self):
        for i in range(0,self.ui.DuesListWidget.count()):
            item=self.ui.DuesListWidget.item(i)
            if self.ui.DuesListWidget.isItemSelected(item):
                self.ProcessDuesClick(item)

        
            
    def RunAnnualRec(self):
        #Make a python list of strings from the
        #QListWidget
        num =len(self.ui.SelectedFilesForAnnualRec)
        self.ui.SelectedFilesForAnnualRec.sortItems()
        theList=[]
        for i in range(0,num):
            item=self.ui.SelectedFilesForAnnualRec.item(i)
            theList.append(item.text())

        DoAnnualReconcilliation(theList,self.ThePerCapParameters,self.DatesToSkip,self.DatesToDouble)
    

    def ProcessDuesClick(self,TheItem):
        if TheItem.font().bold():
            tempFont=TheItem.font()
            tempFont.setBold(False)
            TheItem.setFont(tempFont)
            foundItem=self.ui.SelectedFilesForAnnualRec.findItems(TheItem.text(),Qt.MatchExactly)
            self.ui.SelectedFilesForAnnualRec.takeItem(self.ui.SelectedFilesForAnnualRec.row(foundItem[0]))
        else:
            tempFont=TheItem.font()
            tempFont.setBold(True)
            TheItem.setFont(tempFont)
            
            newItem=QListWidgetItem(TheItem.text())
            temp=QFont()
            temp.setPointSize(16)
            newItem.setFont(temp)
            self.ui.SelectedFilesForAnnualRec.addItem(newItem)
        self.ui.SelectedFilesForAnnualRec.sortItems()

    def ProcessAnnualRecClick(self,TheItem):
        if TheItem.font().bold():
            tempFont=TheItem.font()
            tempFont.setBold(False)
            TheItem.setFont(tempFont)
        else:
            tempFont=TheItem.font()
            tempFont.setBold(True)
            TheItem.setFont(tempFont)


        
        
    def ItemDoubleClickedInDuesFileList(self,TheItem):
        # print "The Following item was selected"
        # print TheItem.text()
        self.DuesFileForReconcile=join("DeductionData",str(TheItem.text()))
        self.ui.labelDuesFile.setText(TheItem.text())
        self.ProcessDuesClick(TheItem)
        

    def UpdatePerCapInfo(self):
        print("HI")
        #self.FullTime_CutOff= float(str(self.ui.FullTime_CutOff.text()))
        PayLevels=["FullTime","HalfTime","QuarterTime","EighthTime"]
        Things=["CutOff","AFTMemPerCap","AFTFeePerCap","AFTMIMemPerCap","AFTMIFeePerCap"]
        for p in PayLevels:
            for th in Things:
                s="{0}_{1}".format(p,th)
                x=getattr(self.ui,s)
                if x.text() != "":
                    setattr(self.ThePerCapParameters,s,float(x.text()))
                


        

  

            
        
    def ItemDoubleClickedInCBUFileList(self,TheItem):
        self.CBUFileForReconcile=join("CBUData",str(TheItem.text()))
        self.ui.labelCBUFile.setText(TheItem.text())

        
    def ReconcileEveryThingButton(self):
        ReconciledFiles="The following files have been reconciled"
        for dateCBU,aMap in self.CBUData.items():
            for dateDues,otherMap in self.DeductionData.items():
                if dateDues.year == dateCBU.year and dateDues.month==dateCBU.month:
                    DuesFile = "%d%02d%02d-GEUDues" %(dateDues.year,dateDues.month,dateDues.day)
                    CBUFile = "%d%02d%02d-GEUCBU" %(dateCBU.year,dateCBU.month,dateCBU.day)
                    Reconcile(join("CBUData",CBUFile+".xlsx"),join("DeductionData",DuesFile+".xlsx"),self)
                    ReconciledFiles =ReconciledFiles+"\n"+DuesFile+"_"+CBUFile
                endif=0
        
        ##display message saying that things are done
        self.DisplayMessageWindow(ReconciledFiles)
    end=0

    def ASearchWasDone(self):
        theNetId= str(self.ui.SearchLine.text())
        theNetId = theNetId.strip().lower()
        aMap={}
        aList=[]
        for date, TheMap in self.ReconciledData.items():
            if theNetId in TheMap:
                #TheMap[theNetId].PrintShort()
                aList.append(date)
                aMap[date]=TheMap[theNetId]
            end_if=0
        end_for=0
        
        aList.sort()
        self.ui.searchOutputBox.clear()
        if len(aList) == 0:
            self.ui.searchOutputBox.append("No results found")
        else:
            theForm="%-16.16s %-8.8s %-10.10s %-7.7s %-5.5s %-5.5s %-5.5s %-5.5s %-8.8s %-8.8s"

            headerString = theForm %("Date","WageType","EmployedUnit","PayRate","GAPer","Terms","Group","Amt","OnlyCBU","OnlyDues")
            print (headerString)
            self.ui.searchOutputBox.textCursor().insertHtml(headerString)
            for x in aList:
                dateString=str(x.year)+ "-%02d" % x.month +"-%02d" % x.day
                infoString=theForm % (str(dateString),str(aMap[x].GetValueByTag("UpdatedWageType")),str(aMap[x].GetValueByTag("EmployUnitName")),str(aMap[x].GetValueByTag("GA_PAY_RATE")),str(aMap[x].GetValueByTag("GA_PERCENTAGE")),str(aMap[x].GetValueByTag("total_ga_terms")),str(aMap[x].GetValueByTag("EmployeeGroup")),str(aMap[x].GetValueByTag("DeductionAmt")),str(aMap[x].GetValueByTag("OnlyInCBU")),str(aMap[x].GetValueByTag("OnlyInDues")))
                print (QString(infoString))
                
                self.ui.searchOutputBox.append(infoString)#QString(infoString))
                #self.ui.searchOutputBox.textCursor().insertHtml('normal text')

        #self.ui.searchOutputBox.setPlainText("this is a test \n this is a new line")





    # Here, defining a method.
    # qt passes in additional arguments that this function does not need,
    # so I use *args to ignore them.
    def DoStuff(self,*args):
#        self.DisplayErrorWindow("DF")

        filetype = '.xlsx'
        filenameCBUList = str(QtGui.QFileDialog.getOpenFileName(self,'Open CBU_List','',
                                                         'CBU_List (*{})'.format(filetype)))
        print("The file name is ",filenameCBUList)
  
        if not filenameCBUList:
            #Cancel was pressed just return
            print("Cancel was pressed in the CBU file selection window")
            return 


        filenameDuesList = str(QtGui.QFileDialog.getOpenFileName(self,'Open Dues_List','',
                                                         'Dues_List (*{})'.format(filetype)))
        print("The file name is ",filenameDuesList)
  
        if not filenameDuesList:
            print("Cancel was pressed in the Dues deduction file selection window")
            return 

        if filenameDuesList and filenameCBUList:
            Reconcile(filenameCBUList,filenameDuesList,self)
            
        # filename is empty string if user hits cancel, so don't save anything
        # if filename:
        #     if not filename.endswith(filetype):
        #         filename += filetype
        #     self.SaveSettings(filename)



    def ReconcileButtonClicked(self):
        if self.DuesFileForReconcile != "nothing" and self.CBUFileForReconcile !="nothing":
            outname=Reconcile(self.CBUFileForReconcile,self.DuesFileForReconcile)
            self.DisplayMessageWindow(outname+" File Created")
    end_thing=0


    def DisplayErrorWindow(self,theError):
        QtGui.QMessageBox.about(self,"caption",theError)

    def DisplayMessageWindow(self,theText):
        QtGui.QMessageBox.about(self,"caption",theText)



end__Class_MainWindow=0











if __name__=='__main__':
    # Initialize the qt event loop.
    app = QtGui.QApplication(sys.argv)
    # Initialize and display our main window.
    w = MainWindow()
    w.show()
    # Run the qt event loop, exiting the script when done.
    sys.exit(app.exec_())
