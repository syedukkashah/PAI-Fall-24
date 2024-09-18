class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        total = super().fare()
        maintenance = total * 0.10
        return total + maintenance


bus = Bus(capacity=50)
print(f"Total fare for the bus: {bus.fare()}")
