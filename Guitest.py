#!/usr/bin/env python2.7

import sys
from PyQt4 import uic, QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import LoadDeductionDataBase
import LoadCBUDataBase

from Reconcile import Reconcile
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


        self.ui.ReconcileButton.clicked.connect(self.ReconcileButtonClicked)
        self.DeductionData =LoadDeductionDataBase.LoadDataBase(self)
        self.CBUData = LoadCBUDataBase.LoadDataBase(self)

        # Connect a function to be run when a button is pressed.
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.listWidget.itemDoubleClicked.connect(self.ItemDoubleClickedInDuesFileList)
        self.ui.cbulistWidget.itemDoubleClicked.connect(self.ItemDoubleClickedInCBUFileList)
        
        self.ui.RemoveFileButton.clicked.connect(self.RemoveFileButtonClicked)

        self.ui.ReconcileEveryThingButton.clicked.connect(self.ReconcileEveryThingButton)
        self.ui.SearchLine.editingFinished.connect(self.ASearchWasDone)





    end_init=0
    def tabButton(self):
        print "AHDSSDG"
    
    def ItemDoubleClickedInDuesFileList(self,TheItem):
        # print "The Following item was selected"
        # print TheItem.text()
        self.DuesFileForReconcile="./DeductionData/"+str(TheItem.text())
        self.ui.labelDuesFile.setText(TheItem.text())

    def ItemDoubleClickedInCBUFileList(self,TheItem):
        self.CBUFileForReconcile="./CBUData/"+str(TheItem.text())
        self.ui.labelCBUFile.setText(TheItem.text())

    def RemoveFileButtonClicked(self):
        rowToKill=self.ui.listWidget.currentRow()
        print "Removing ",rowToKill, " from list"
        self.ui.listWidget.takeItem(rowToKill)
        
    def ReconcileEveryThingButton(self):
        ReconciledFiles="The following files have been reconciled"
        for dateCBU,aMap in self.CBUData.iteritems():
            for dateDues,otherMap in self.DeductionData.iteritems():
                if dateDues.year == dateCBU.year and dateDues.month==dateCBU.month:
                    DuesFile = "%d%02d%02d-GEUDues" %(dateDues.year,dateDues.month,dateDues.day)
                    CBUFile = "%d%02d%02d-GEUCBU" %(dateCBU.year,dateCBU.month,dateCBU.day)
                    Reconcile("./CBUData/"+CBUFile+".xlsx","./DeductionData/"+DuesFile+".xlsx",self)
                    ReconciledFiles =ReconciledFiles+"\n"+DuesFile+"_"+CBUFile
                endif=0
        
        ##display message saying that things are done
        self.DisplayMessageWindow(ReconciledFiles)
    end=0

    def ASearchWasDone(self):
        theNetId= str(self.ui.SearchLine.text())
        theNetId = theNetId.lower()
        aMap={}
        aList=[]
        for date, TheMap in self.DeductionData.iteritems():
            if theNetId in TheMap:
                #TheMap[theNetId].PrintShort()
                aList.append(date)
                aMap[date]=TheMap[theNetId]
            end_if=0
        end_for=0
        
        aList.sort()
        self.ui.searchOutputBox.clear()

        for x in aList:
            dateString=str(x.year)+ "-%02d" % x.month +"-%02d" % x.day
            infoString=str(aMap[x].WageTypeText)
            self.ui.searchOutputBox.append(QString(dateString)+"   "+QString(infoString))
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
            Reconcile(self.CBUFileForReconcile,self.DuesFileForReconcile,self)
    end_thing=0


    def DisplayErrorWindow(self,theError):
        QtGui.QMessageBox.about(self,"caption",QString(theError))

    def DisplayMessageWindow(self,theText):
        QtGui.QMessageBox.about(self,"caption",QString(theText))



end__Class_MainWindow=0











if __name__=='__main__':
    # Initialize the qt event loop.
    app = QtGui.QApplication(sys.argv)
    # Initialize and display our main window.
    w = MainWindow()
    w.show()
    # Run the qt event loop, exiting the script when done.
    sys.exit(app.exec_())
