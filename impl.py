import re
class PhysicalInfo(object):
    def __init__ (self, date, name, gender, height, temperature):
        self.date=date
        self.name=name 
        self.gender=gender
        self.height=height
        self.temperature=temperature
    #must be string
    # Date will be "MM-DD-YYYY" or "DD-MM-YYYY"
    def set_date(self, newDate):
        if (not isinstance(newDate,str)):
            raise ValueError
        x=re.search('[^0-9-]', newDate)
        temp=newDate.split("-")
        if (x!=None or len(newDate)!=10 and temp!=3):
            raise ValueError("Only numbers are allowed or Less than 10 characters") 
        if ( (temp[-1]) and len(temp[-1])==4):
            self.date=newDate
            return
        else: 
            raise ValueError
    #must be string
    def set_name(self, newName):
        if (not isinstance(newName,str)):
            raise ValueError
        x=re.search('[^0-9a-zA-Z -]', newName)
        if x!=None:
            raise ValueError
        #check at least two alphanumeric characters
        y=re.findall('[0-9a-zA-Z]', newName)
        #check at least one English characters
        x=re.search('[a-zA-Z]', newName)
        if (x!=None and len(y)>1):
            self.name=newName
            return
        else: 
            raise ValueError
        
    #must be string
    def set_gender(self, newGender):
        if (isinstance(newGender,str) and (newGender=="M" or newGender=="F" )):
            self.gender=newGender
            return
        else: 
            raise ValueError
    #must be int 
    def set_height(self, newHeight):
        if (isinstance(newHeight,int) and newHeight>=17 and newHeight<=84 ):
            self.height=newHeight
            return
        else: 
            raise ValueError
    #must be float
    def set_temperature(self, newTemperature):
        if (isinstance(newTemperature,float) and newTemperature>=95.0 and newTemperature<=104.0) :
            self.temperature=newTemperature
            return
        else: 
            raise ValueError
x=PhysicalInfo("06-09-2000","Justin", "F", 65, "97")
x.set_date("03-04-9999")