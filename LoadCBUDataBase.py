
import CBULoader
from os import listdir
from os.path import isfile, join
import datetime

def LoadDataBase(GuiWindow):
    #Find all the files in the deduction data directory
    CBUFileNames = [ f for f in listdir("CBUData") if isfile(join("CBUData",f)) ]
    print "Loading All CBU files"
    GuiWindow.ui.cbulistWidget.clear()
    GuiWindow.ui.cbulistWidget.setSortingEnabled(True)#sort the suff
    MapForAllCBUFiles={}
    for i in CBUFileNames:
        splitName=i.split("-")
        datePart=splitName[0].strip()
        GuiWindow.ui.cbulistWidget.addItem(i)

        NormalMap,EmptyNetId,FirstLastList=CBULoader.LoadCBU(join("CBUData",i))        
        dateTemp=datetime.datetime.strptime(datePart,"%Y%m%d").date()
                
        MapForAllCBUFiles[dateTemp]=NormalMap


    return MapForAllCBUFiles

end_Function_LoadDataBase=0
