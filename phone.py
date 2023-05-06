from item import Item



class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0,broken_phone=0):
        #call to super function to have access to all  attributes / methods
        super().__init__(name,price,quantity)
        
        #quantity and price validation
        assert broken_phone>=0,f"broken_phone {broken_phone} is less than 0"
        
        
        #assigning objects to self
     
        self.broken_phone=broken_phone
         
        
# #call instanciate_from_csv class method        
# Item.instanciate_from_csv()

# phone2=Phone("infinix", 800,3,4)
# #inserts into a list each time an object is created
# print(Phone.all)
# print(Item.is_static(7.0))