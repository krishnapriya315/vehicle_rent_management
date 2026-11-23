
from Vehicle import Vehicle     #import vehicle parant class

class Bike(Vehicle):                # bike child class
    def calculate_rent(self,day):

        total_rent=self.rental_price*day+500
        print('total rent:',total_rent) #print the total rent
        return total_rent

    def display_vehicle_details(self):
        print('name:',self.name)    # print the bike name 
        print('rental_price:',self.rental_price)    #print bike rental price per day
