class Employee:
    def __init__(self):
        self.name = ""
        self.monthly_salary = 0
        self.tax_percentage = 2  
    def get_data(self):
        self.name = input("Enter employee name: ")
        self.monthly_salary = float(input("Enter monthly salary: "))
    def Salary_after_tax(self):
        tax_amount = (self.tax_percentage / 100) * self.monthly_salary
        return self.monthly_salary - tax_amount
    def update_tax(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage
emp = Employee()
emp.get_data()
print(f"Salary after tax: {emp.Salary_after_tax():.2f}")
emp.update_tax(3) 
print(f"Salary after tax (with updated tax percentage): {emp.Salary_after_tax():.2f}")
