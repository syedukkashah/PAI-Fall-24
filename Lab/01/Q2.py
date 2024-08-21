
n1 = float(input("Enter num 1: "))
n2 = float(input("Enter num 2: "))
opt = int(input("Choose calculation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
if opt == 1:
    print(n1 + n2)
elif opt == 2:
        print(n1 - n2)
elif opt == 3:
        print(n1 * n2)
elif opt == 4:
        print(n1 / n2)
else:
        print ("invalid input")
