dict = {}
dict["Math"] = int(input("Enter Math marks: "))
dict["Chemistry"] = int(input("Enter Chem marks: "))
dict["Physics"] = int(input("Enter Physics marks: "))
sum = 0
max = dict["Math"]
max_sub = "Math"
for i in dict.keys():
    sum+=dict[i]
    if dict[i] > max:
        max_sub = i

print("Average marks: ", sum/3)
print("\nBest subject by Marks: ", max_sub)

