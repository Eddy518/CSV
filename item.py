import csv
class Item:
    pay_rate=0.8 #class attribute(shared across instances)
    all=[] #list all
    def __init__(self,name:str,price:float,quantity=0):
        
        
        #quantity and price validation
        assert quantity>=0,f"quantity{quantity} is less than 0"
        assert price>=0,f"price {price} is less than 0"
        
        
        #assigning objects to self
        #underscore is used to enable property name to be able to set values since name in def name(): is read only
        self.__name=name
        self.quantity=quantity
        self.__price=price
        
        #add to all list each time an object is instanciated
        Item.all.append(self)
        
    #to set the name attribute to read-only(it can't be changed)
    #name of the value to set as read-only must be indicated
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    
    def discount(self): 
        self.__price=self.__price*self.pay_rate
        
    def apply_increment(self,increment_value):
        self.__price=self.__price+self.__price*increment_value
        return self.__price
    
    #using a setter to access private attribute self.__name
    @name.setter
    def name(self,value):
        if len(value) >10:
            raise Exception("the value is too long")
        else:
            self.__name=value
        
    def calculateTotalPrice(self):
        return self.quantity*self.__price
    
   
        
    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv','r')as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
               )
            
            
    @staticmethod
    def is_static(num):
        #we will count out the floats that are point zero
        
        #isinstance checks if a number is an instance of a float or an int
       if isinstance(num,float):
           return num.is_integer()     
       elif isinstance(num, int):
           return True       
       else:
           return False

    #takes list(Item.all) and represents it in a readable fashion    
    def __repr__(self):
        return f"{self.__class__.__name__}'{self.name}',{self.__price},{self.quantity}"
       #when item is used it will only return the name item to return the name of the class we can use
       # self._ _class_ _._ _name_ _
    
    #property name followed by name of the function is used to set the function to readonly. It can't be changed
    # @property   
    # def read_only_(self):
    #     return "AAA"