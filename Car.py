from Vehicle import Vehicle

class Car(Vehicle):
    def calculate_rent(self,day):
        self.day=day

        total_rent=self.rental_price*self.day+500
        print('total rent:',total_rent)
        return total_rent

    def display_vehicle_details(self):
        print('name:',self.name)
        print('rental_price:',self.rental_price)