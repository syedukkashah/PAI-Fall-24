lst = []
size = int(input("Enter size of list: "))
print("Enter elements: \n")
for i in range(0, size):
    num = int(input())
    lst.append(num)

count = 0
for i in range(0, size):
    if lst[i] % 2 == 0:
        count = count+1

print("Even nums in list: ", count)
