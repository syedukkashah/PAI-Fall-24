size = int(input("How many numbers do you want to enter? "))
list = []
for i in range(size):
    num = int(input("Enter a number: "))
    list.append(num)
max=list[i]
for i in list:
    if i > max:
        max = i
print("Largest number: ", max)
