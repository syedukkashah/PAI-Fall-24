try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(num1 / num2)
except ZeroDivisionError:
    print("Math Error")
except ValueError:
    print("Invalid input")