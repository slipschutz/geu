
################################################################################################################
################################################################################################################
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#


class CBU_Line:
    def __init__(self):
       self.LastName=""
       self.FirstName=""
       self.Email=""
       self.SalaryLevel=0
       self.GA_Percentage=0
       self.PayRate=0
       self.TotalGATerms=0
       self.PayrollRestrict=0
       self.LocalAddressLine1=""
       self.LocalAddressLine2=""
       self.LocalCityName=""
       self.LocalStateCode=""
       self.LocalZipCode=""
       self.CountryCode=""
       self.LocalId=0
       self.PermAddressLine1=""
       self.PermAddressLine2=""
       
       self.PermCityName=""
       self.PermStateCode=""
       self.PermZipCode=""
       self.PermCountryCode=""
       self.PermId=0
       self.NetId=""
       self.EnrolledUnit=""
       self.EnrolledUnitName=""
       self.EmployedUnit=""
       self.EmployedUnitName=""
       self.JobKey=""
       self.MemberType=""
       self.DuesType=""
       ##Things that aren't in the spread sheet
       self.UpdatedDuesType=""
       self.WasUpdated="No"
    
    def SetValue(self,i,v):
        if i==0:
            self.LastName=v
        elif i==1:
            self.FirstName=v
        elif i==2:
            self.Email=v
        elif i==3:
            self.SalaryLevel=v
        elif i==4:
            self.GA_Percentage=v
        elif i==5:
            self.PayRate=v
        elif i==6:
            self.TotalGATerms=v
        elif i==7:
            self.PayrollRestrict=v
        elif i==8:
            self.LocalAddressLine1=v
        elif i==9:
            self.LocalAddressLine2=v
        elif i==10:
            self.LocalCityName=v
        elif i==11:
            self.cLocalStateCode=v
        elif i==12:
            self.LocalZipCode=v
        elif i==13:
            self.CountryCode=v
        elif i==14:
            self.LocalId=v
        elif i==15:
            self.PermAddressLine1=v
        elif i==16:
            self.PermAddressLine2=v
        elif i==17:
            self.PermCityName=v
        elif i==18:
            self.PermStateCode=v
        elif i==19:
            self.PermZipCode=v
        elif i==20:
            self.PermCountryCode=v
        elif i==21:
            self.PermId=v
        elif i==22:
            self.NetId=v
        elif i==23:
            self.EnrolledUnit=v
        elif i==24:
            self.EnrolledUnitName=v
        elif i==25:
            self.EmployedUnit=v
        elif i==26:
            self.EmployedUnitName=v
        elif i==27:
            self.JobKey=v
        elif i==28:
            self.MemberType=v
        elif i==29:
            self.DuesType=v
        else:
            print "NO DICE"



    def GetValue(self,i):
        if i==0:
            return self.LastName 
        elif i==1:
            return self.FirstName 
        elif i==2:
            return self.Email 
        elif i==3:
            return self.SalaryLevel 
        elif i==4:
            return self.GA_Percentage 
        elif i==5:
            return self.PayRate 
        elif i==6:
            return self.TotalGATerms 
        elif i==7:
            return self.PayrollRestrict 
        elif i==8:
            return self.LocalAddressLine1 
        elif i==9:
            return self.LocalAddressLine2 
        elif i==10:
            return self.LocalCityName 
        elif i==11:
            return self.cLocalStateCode 
        elif i==12:
            return self.LocalZipCode 
        elif i==13:
            return self.CountryCode 
        elif i==14:
            return self.LocalId 
        elif i==15:
            return self.PermAddressLine1 
        elif i==16:
            return self.PermAddressLine2 
        elif i==17:
            return self.PermCityName 
        elif i==18:
            return self.PermStateCode 
        elif i==19:
            return self.PermZipCode 
        elif i==20:
            return self.PermCountryCode 
        elif i==21:
            return self.PermId 
        elif i==22:
            return self.NetId 
        elif i==23:
            return self.EnrolledUnit 
        elif i==24:
            return self.EnrolledUnitName 
        elif i==25:
            return self.EmployedUnit 
        elif i==26:
            return self.EmployedUnitName 
        elif i==27:
            return self.JobKey 
        elif i==28:
            return self.MemberType 
        elif i==29:
            return self.DuesType 
        elif i==30:
            return self.UpdatedDuesType
        elif i==31:
            return self.WasUpdated
        else:
            return "ERROR"



    def PrintShort(self):
        if self.WasUpdated == False :
            print "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
            print self.FirstName," ",self.LastName
            print "NETID=",self.NetId
            print "DuesType=",self.DuesType
            print "EnrolledUnit=",self.EnrolledUnitName
            print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        else :
            print "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
            print self.FirstName," ",self.LastName
            print "NETID=",self.NetId
            print "DuesType=",self.DuesType," UpdatedDues=",self.UpdatedDuesType
            print "EnrolledUnit=",self.EnrolledUnitName
            print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^a#
################################################################################################################
################################################################################################################
