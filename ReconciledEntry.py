
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
                   "Date"]

ListOfKnackNames=["Lastname",
                   "Firstname",
                   "MSU Email",
                   "Salary Level",
                   "GA Percentage",
                   "Pay Rate",
                   "Total GA Terms",
                   "Payroll Restrict",
                   "Local Address 1",
                   "Local Address 2",
                   "Local City Name",
                   "Local State Code",
                   "Local Zip Code",
                   "Local Cntry Code",
                   "Local Telephone",
                   "Permanent Address 1",
                   "Permanent Address 2",
                   "Permanent City Name",
                   "Permanent State Code",
                   "Permanent Zip Code",
                   "Permanent Country Code",
                   "Permanent Telephone",
                   "MSUNETID",
                   "Enrolled Unit Code",
                   "Enrolled Unit Name",
                   "Employed Unit Code",
                   "Employed Unit Name",
                   "JobKey",
                   "Member Type",
                   "Dues Wage Type",
                   "Updated Wage Type",
                   "Was Updated",
                   "DuesFile NetId",
                   "Employee Group",
                   "Deduction Amount",
                   "OnlyInCBU",
                   "OnlyInDues",
                   "PayRoll Date",
                   "Needs Updating"]


from CBULine import *
from DeductionLoader import *

class ReconciledEntry:
    def __init__(self):
        self.theStuff={}
        self.DuesPersonInfo=PersonInfoFromDeductionFile()
        for i in ListOfColumnNames:
            self.theStuff[i]=" "

    def GetValueByIndex(self,i):
        if ListOfColumnNames[i] =="Date":
            pass
        if i < len(ListOfColumnNames):
            return self.theStuff[ListOfColumnNames[i]]
        else:
            return " "


    def SetValueByIndex(self,i,v):
        if i < len(ListOfColumnNames):
#            print("Setting the value",v," in ",ListOfColumnNames[i])
            self.theStuff[ListOfColumnNames[i]]=v
        else:
            print ("can't set index ",i," in ReconciedEntry")
            raise

    def SetValueByTag(self,tag,val):
        if tag in self.theStuff:
            self.theStuff[tag]=val
        else:
            print ("can't set tag ", tag, " in ReconciledEntry")
            raise

    def GetValueByTag(self,tag):
        if tag in self.theStuff:
           return self.theStuff[tag]
        else:
            print ("can't get tag ", tag, " in ReconciledEntry")
            raise

            
    def CopyCBUInfo(self,CBUInfo):
        for i in range(NumberOfColumnsInCBU):
#            print("I is",i,"cbu value ",CBUInfo.GetValue(i), "colum name ",ListOfColumnNames[i])
            self.SetValueByIndex(i,CBUInfo.GetValue(i))


            

    def CopyDuesInfo(self,DUESInfo):
        self.DuesPersonInfo=DUESInfo

    def SetDuesPersonInfo(self,num):
        if num >= len(self.DuesPersonInfo.Lines):
            print ("ERROR CANT DO THAT num=",num)

        self.SetValueByTag("EmployeeGroup",self.DuesPersonInfo.Lines[num].EmployeeGroup)
        self.SetValueByTag("DeductionAmt",self.DuesPersonInfo.Lines[num].DeductionAmt)
        self.SetValueByTag("Lastname",self.DuesPersonInfo.Lines[num].LastName)
        self.SetValueByTag("Firstname",self.DuesPersonInfo.Lines[num].FirstName)
        self.SetValueByTag("UpdatedWageType",self.DuesPersonInfo.Lines[num].WageTypeText)
        self.SetValueByTag("Date",self.DuesPersonInfo.Lines[num].PayDay)


