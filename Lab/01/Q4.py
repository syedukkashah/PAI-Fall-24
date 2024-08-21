lst = []
size = int(input("Enter size of list: "))
print("Enter elements: \n")
for i in range(0, size):
    num = int(input())
    lst.append(num)

Sum = 0

for i in range(0, size):
    Sum = Sum + lst[i]

print("Sum: ", Sum)
