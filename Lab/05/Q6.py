class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Subclasses must implement this method")

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

    def hire(self):
        print(f"{self.name} is hiring someone.")

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10

    def write_code(self):
        print(f"{self.name} is writing code.")

class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.30


if __name__ == "__main__":
    manager = Manager("Alice", 80000)
    developer = Developer("Bob", 60000)
    senior_manager = SeniorManager("Charlie", 100000)
    print(f"{manager.name}'s Bonus: ${manager.calculate_bonus():.2f}")
    print(f"{developer.name}'s Bonus: ${developer.calculate_bonus():.2f}")
    print(f"{senior_manager.name}'s Bonus: ${senior_manager.calculate_bonus():.2f}")
    manager.hire()
    developer.write_code()
