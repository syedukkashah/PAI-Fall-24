lst = []
size = int(input("Enter size of list: "))
print("Enter elements: \n")
for i in range(size):
    num = int(input())
    lst.append(num)
print("List before deleting element: \n")
print(lst)
num = int(input("Enter num (All elements in list less than num will be deleted): "))
filtered_lst = []
for element in lst:
    if element >= num:
        filtered_lst.append(element)
lst = filtered_lst
print("List after deleting element: ")
print(lst)
