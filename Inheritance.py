class MyParent(): # Base Class
    #1.1. Property
    bloodGroup='+Bve'
    
    #1.2 Constructor
    
    #1.3 Method
    pass
class MyChild(MyParent): # derived class
    #1.1. Property
    
    #1.2 Constructor
    
    #1.3 Method
    def getMyBloodGroup(self):
        print(f'My Blood group is {self.bloodGroup}')

    pass

#Create Class Object
# We always create object of child class
co = MyChild()
co.getMyBloodGroup()