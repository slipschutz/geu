 

################################################################################################################
################################################################################################################
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#
class DeductionLine:
    def __init__(self):
       self.EmployeeNumber=0
       self.PayDay=0
       self.LastName=""
       self.FirstName=""
       self.SubArea=""
       self.EmployeeGroup=""
       self.WageTypeNum=0
       self.WageTypeText=""
       self.DeductionAmt=0
       self.NetId=""


    def PrintShort(self):
        print (self.FirstName," ",self.LastName)
        print ("NetId=",self.NetId)
        print ("WageType=",self.WageTypeText)
        print ("PayDate=",self.PayDay)
        print ("EmployeeGroup=",self.EmployeeGroup)
        print ("DeductionAmt=",self.DeductionAmt)

    def Print(self):
        print (self.LastName,  self.FirstName)
        print ("Employee Number=",self.EmployeeNumber)
        print ("PayDay=",self.PayDay)
        print ("SubArea=",self.SubArea)
        print ("EmployeeGroup=",self.EmployeeGroup)
        print ("WageTypeNum=",self.WageTypeNum)
        print ("WageTypeText=",self.WageTypeText)
        print ("DeductionAmy=",self.DeductionAmt)
        print ("NetId=",self.NetId)

        
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^a#
################################################################################################################
################################################################################################################

