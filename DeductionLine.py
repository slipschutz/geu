 

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
        print self.FirstName," ",self.LastName
        print "NetId=",self.NetId
        print "WageType=",self.WageTypeText
    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^a#
################################################################################################################
################################################################################################################

