class Vehicle:
    def __init__(self, c):
        self.capacity = c

    def get_fare(self):
       return self.capacity*100

class Bus(Vehicle):
    def __init__(self, c):
        super().__init__(c)

    def get_fare(self):
        return 1.1*super().get_fare()

b = Bus(20)
print(b.get_fare())