def employee(name, salary = 1000):
    salary *= 0.98
    print("Name: ", name, "\nSalary after tax: ", salary)


employee("Bob")
employee("Ned", 5000)