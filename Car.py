from Vehicle import Vehicle      

class Car(Vehicle): #car child class
    def calculate_rent(self,day):       #method calculate rent per day 
        self.day=day

        total_rent=self.rental_price*self.day+500
        print('total rent:',total_rent)     #print the total rent 
        return total_rent       #return value so we can use it later

    def display_vehicle_details(self):      #method car details 
        print('name:',self.name)
        print('rental_price:',self.rental_price)