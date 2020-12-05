import re
class PhysicalInfo:
    def __init__(self):
        self.date=0
        self.name=0 
        self.gender=0
        self.height=0
        self.temperature=0
    # def __init__ (self, date, name, gender, height, temperature):
    #     self.date=date
    #     self.name=name 
    #     self.gender=gender
    #     self.height=height
    #     self.temperature=temperature
    #must be string
    # Date will be "MM-DD-YYYY" or "DD-MM-YYYY"
    def set_date(self, newDate):
        print("Date", self.date)
        #Check string type
        if (not isinstance(newDate,str)):
            raise ValueError("Need to be str instance")
        #Search for differences 
        x=re.search('[^0-9-]', newDate)
        temp=newDate.split("-")
        #Check 1) valid characters used 
        #Check 2) - is exactly 3
        #Validation of day/month 
        if (x!=None or  len(temp)!=3):
            raise ValueError("Only numbers are allowed or Less than 10 characters") 
        day=( len(str(int(temp[0])))==0 or len(str(int(temp[0])))>2)
        month=( len(str(int(temp[1])))==0 or len(str(int(temp[1])))>2)
        # Check valid year,day, month
        if ( len(str(int(temp[2])))!=4 and  day and month):
            raise ValueError("Year, month, and day must be valid") 
        # Check valid months 
        if ( int(temp[0])>=1 and int(temp[0])<=31 and int(temp[1])>=1 and int(temp[1])<=12 ):
             self.date=newDate
             print("Date", self.date)
             return 
        # Check valid days
        if ( int(temp[1])>=1 and int(temp[1])<=31 and int(temp[0])>=1 and int(temp[0])<=12 ):
             self.date=newDate
             print("Date", self.date)
             return 
        raise ValueError("Date: Invalid numbers for date for days, month, year.")
    #must be string
    def set_name(self, newName):
        
        if (not isinstance(newName,str) ):
            raise ValueError("Name: Must be str instance and must be valid characters.")
        x=re.search('[^0-9a-zA-Z -]', newName)
        if(x!=None):
            raise ValueError("Name: must be valid characters.")
        #y=check at least two alphanumeric characters
        #x=check at least one English characters
        y=re.findall('[0-9a-zA-Z]', newName)
        x=re.search('[a-zA-Z]', newName)
        if (x!=None and len(y)>1):
            self.name=newName
            return
        else: 
            raise ValueError("Name: Must meet requirements")
        
    #must be string
    def set_gender(self, newGender):
        if (isinstance(newGender,str) and (newGender=="M" or newGender=="F" )):
            self.gender=newGender
            return
        else: 
            raise ValueError("Gender: Must string instance and M/F")
    #must be int 
    def set_height(self, newHeight):
        if (isinstance(newHeight,int) and newHeight>=17 and newHeight<=84 ):
            self.height=newHeight
            return
        else: 
            raise ValueError("Height: Must int instance and between 17 and 84")
    #must be float
    def set_temperature(self, newTemperature):
        if (isinstance(newTemperature,float) and newTemperature>=95.0 and newTemperature<=104.0) :
            self.temperature=newTemperature
            return
        else: 
            raise ValueError("Temperature: Must float instance and between 95.0 and 104.0")
# x=PhysicalInfo("06-09-2000","Justin", "F", 65, "97")
# x.set_date("001-001-02020")