#1. Class Defination



class Car: # PascleCase
    #1.1 Property = Variable
    brand="TATA"
    model='2024' # variable
    
    #1.2 Constructor
    
    
    #1.3 Method = Functions
    def getMyBrand(self): # camleCase
        # self is internal class object
        print(f"Brand is {self.brand}")
        print(f"Model year is {self.model}")
        pass
    
    pass
#2 Create Class Object
# classObject = ClassName()
#co is external class object
co = Car()

# Call the method with classObjectcls
co.getMyBrand()