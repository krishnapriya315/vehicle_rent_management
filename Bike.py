
from Vehicle import Vehicle

class Bike(Vehicle):
    def calculate_rent(self,day):

        total_rent=self.rental_price*day+500
        print('total rent:',total_rent)
        return total_rent

    def display_vehicle_details(self):
        print('name:',self.name)
        print('rental_price:',self.rental_price)
