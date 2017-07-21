
import ReconciledEntry
from os import listdir
from os.path import isfile, join
import datetime
import ReconciledEntryLoader

def LoadDataBase(GuiWindow):
    #Find all the files in the deduction data directory
    FileNames = [ f for f in listdir("ReconciledData") if isfile(join("ReconciledData",f)) ]
    print ("Loading All Reconciled files")
    GuiWindow.ui.ReconciledList.clear()
    GuiWindow.ui.ReconciledList.setSortingEnabled(True)#sort the suff
    MapForAllFiles={}
    for i in FileNames:
        splitName=(i.split("_")[1]).split("-")
        datePart=splitName[0].strip()
        GuiWindow.ui.ReconciledList.addItem(i)

        NormalMap=ReconciledEntryLoader.Load(join("ReconciledData",i))        
        dateTemp=datetime.datetime.strptime(datePart,"%Y%m%d").date()
                
        MapForAllFiles[dateTemp]=NormalMap


    return MapForAllFiles

end_Function_LoadDataBase=0
