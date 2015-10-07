
ListOfColumnNames=["Lastname",
                   "Firstname",
                   "Email",
                   "GA_SALARY_LEVEL",
                   "GA_PERCENTAGE",
                   "GA_PAY_RATE",
                   "total_ga_terms",
                   "payroll_restrict",
                   "Local_Line_Adr1",
                   "Local_Line_Adr2",
                   "Local_City_Name",
                   "Local_State_Code",
                   "Local_Zip_Code",
                   "Local_Cntry_Code",
                   "Local_Tlphn_Id",
                   "Perm_Line_Adr1",
                   "Perm_Line_Adr2",
                   "Perm_City_Name",
                   "Perm_State_Code",
                   "Perm_Zip_Code",
                   "Perm_Cntry_Code",
                   "Perm_Tlphn_Id",
                   "MSUNETID",
                   "EnrolledUnit",
                   "EnrolledUnitName",
                   "EmployUnit",
                   "EmployUnitName",
                   "JobKey",
                   "Membertype",
                   "DuesWageType",
                   "UpdatedWageType",
                   "WasUpdated",
                   "DuesFileNetId",
                   "EmployeeGroup",
                   "DeductionAmt",
                   "OnlyInCBU",
                   "OnlyInDues",
                   "blah",
                   "joe"]


from CBULine import *

class ReconciledEntry:
    def __init__(self):
        self.theStuff={}
        for i in ListOfColumnNames:
            self.theStuff[i]=" "

    def GetValueByIndex(self,i):
        if i < len(ListOfColumnNames):
            return self.theStuff[ListOfColumnNames[i]]
        else:
            return " "


    def SetValueByIndex(self,i,v):
        if i < len(ListOfColumnNames):
            self.theStuff[ListOfColumnNames[i]]=v
        else:
            print "can't set index ",i," in ReconciedEntry"
            raise

    def SetValueByTag(self,tag,val):
        if tag in self.theStuff:
            self.theStuff[tag]=val
        else:
            print "can't set tag ", tag, " in ReconciledEntry"
            raise

    def GetValueByTag(self,tag):
        if tag in self.theStuff:
           return self.theStuff[tag]
        else:
            print "can't get tag ", tag, " in ReconciledEntry"
            raise

            
    def CopyCBUInfo(self,CBUInfo):
        for i in range(NumberOfColumnsInCBU):
            self.SetValueByIndex(i,CBUInfo.GetValue(i))

    def CopyDuesInfo(self,DUESInfo):
        self.SetValueByTag("EmployeeGroup",DUESInfo.EmployeeGroup)
        self.SetValueByTag("DeductionAmt",DUESInfo.DeductionAmt)
        self.SetValueByTag("Lastname",DUESInfo.LastName)
        self.SetValueByTag("Firstname",DUESInfo.FirstName)
