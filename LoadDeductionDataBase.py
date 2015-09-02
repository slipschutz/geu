
import DeductionLoader
from os import listdir
from os.path import isfile, join
import datetime

def LoadDataBase(GuiWindow):
    #Find all the files in the deduction data directory
    deductionFileNames = [ f for f in listdir("DeductionData") if isfile(join("DeductionData",f)) ]
    print "Loading Entire DataBase"
    GuiWindow.ui.listWidget.clear()
    GuiWindow.ui.listWidget.setSortingEnabled(True)#sort the suff
    MapForAllDeductionFiles={}
    for i in deductionFileNames:
        splitName=i.split("-")
        datePart=splitName[0].strip()
        GuiWindow.ui.listWidget.addItem(i)
        NormalMap,LastFirstNameMap=DeductionLoader.LoadDeduction(join("DeductionData",i))
        
        dateTemp=datetime.datetime.strptime(datePart,"%Y%m%d").date()
                
        MapForAllDeductionFiles[dateTemp]=NormalMap

    return MapForAllDeductionFiles
    

end_Function_LoadDataBase=0
