class Animal:
    def __init__(self, name, age, habitat, availability = True):
        self._name = name
        self._age = age
        self._habitat = habitat
        self._availability = availability

    def is_available(self, available):
        self._availability = available

    def details(self):
        print("Age: ", self._age)
        print("Name: ", self._age)
        print("Habitat: ", self._habitat)
        availability_status = "Currently available for viewing" if self._availability else "Quarantined"
        print("Availability Status: ", availability_status)

class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type):
        super().__init__(name, age, habitat)
        self._fur_length = fur_length
        self._diet_type = diet_type

    def details(self):
        super().details()
        print("Fur length: ", self._fur_length)
        print("Diet Type: ", self._diet_type)
        print("\n")


class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_attitude):
        super().__init__(name, age, habitat)
        self._wingspan = wingspan
        self._flight_attitude = flight_attitude

    def details(self):
        super().details()
        print("Flight altitude: ", self._flight_attitude)
        print("Wing span: ", self._wingspan)
        print("\n")

class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_pattern, venomous_status):
        super().__init__(name, age, habitat)
        self._scale_pattern = scale_pattern
        self._venomous_status = venomous_status

    def details(self):
        super().details()
        venom_status = "Venomous" if self._venomous_status else "Non-Venomous"
        print("Venomous status: ", venom_status)
        print("Scale pattern: ", self._scale_pattern)
        print("\n")

lion = Mammal("Lion", 5, "Savannah", "Short", "Carnivore")
eagle = Bird("Eagle", 3, "Mountains", "2.5 m", "3000 m")
snake1 = Reptile("Python", 4, "Rainforest", "Diamond", False)
snake2 = Reptile("Cobra", 4, "Desert", "Diamond", True)
# Displaying information about the animals
lion.details()
eagle.details()
snake1.details()
snake2.details()
# Marking one animal as in quarantine
lion.is_available(False)
print("\nAfter marking Lion as unavailable:")
lion.details()