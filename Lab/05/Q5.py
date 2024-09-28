from datetime import date

class Vehicle:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.__rental_price = rental_price
        self.is_available = True

    def check_availability(self):
        return self.is_available

    def calculate_rental_cost(self, start_date, end_date):
        rental_days = (end_date - start_date).days
        if rental_days <= 0:
            return 0
        return rental_days * self.__rental_price

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Price per day: ${self.__rental_price}, Available: {self.is_available}")

    def rent_vehicle(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_vehicle(self):
        self.is_available = True

class Car(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

class SUV(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

class Truck(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.__contact_info = contact_info
        self.rental_history = []

    def add_to_rental_history(self, rental_reservation):
        self.rental_history.append(rental_reservation)

    def display_rental_history(self):
        print(f"Rental history for {self.name}:")
        for reservation in self.rental_history:
            reservation.display_reservation_details()

class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = vehicle.calculate_rental_cost(start_date, end_date)

    def confirm_reservation(self):
        if self.vehicle.rent_vehicle():
            self.customer.add_to_rental_history(self)
            print(f"Reservation confirmed for {self.customer.name}.")
        else:
            print(f"Sorry, {self.vehicle.make} {self.vehicle.model} is not available.")

    def display_reservation_details(self):
        print(f"Vehicle: {self.vehicle.make} {self.vehicle.model}, "
              f"Rental Period: {self.start_date} to {self.end_date}, "
              f"Total Cost: ${self.total_cost:.2f}")

def display_info(obj):
    obj.display_details() if isinstance(obj, Vehicle) else obj.display_reservation_details()

car = Car("Toyota", "Camry", 40)
suv = SUV("Ford", "Explorer", 60)
truck = Truck("Chevy", "Silverado", 80)
customer1 = Customer("Alice", "alice@example.com")
start = date(2023, 9, 1)
end = date(2023, 9, 5)
reservation = RentalReservation(customer1, car, start, end)
reservation.confirm_reservation()
display_info(car)
display_info(reservation)
customer1.display_rental_history()
car.return_vehicle()
print("After returning the vehicle:")
display_info(car)
