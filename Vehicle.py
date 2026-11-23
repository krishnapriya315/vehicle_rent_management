from abc import ABC,abstractmethod  #abstrac class

class  Vehicle(ABC):        #cannot create object from this
    @abstractmethod

    def calculate_rent(day):        #this is rule 
        pass
    def display_vehicle_detialc(self):
        pass
    def __init__(self,name,rental_price):       #runs when object is create 
        self.name=name
        self.__rental_price=rental_price    #store name as public variable 

    @property
    def rental_price(self):     #
        return self.__rental_price      #store price as private variable 
    