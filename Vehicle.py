from abc import ABC,abstractmethod

class  Vehicle(ABC):
    @abstractmethod

    def calculate_rent(day):
        pass
    def display_vehicle_detialc(self):
        pass
    def __init__(self,name,rental_price):
        self.name=name
        self.__rental_price=rental_price

    @property
    def rental_price(self):
        return self.__rental_price
    