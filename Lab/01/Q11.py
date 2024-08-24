dict = {}
dict["Math"] = int(input("Enter Math marks (out of 50): "))
dict["Chemistry"] = int(input("Enter Chem marks (out of 50): "))
dict["Physics"] = int(input("Enter Physics marks (out of 50): "))
sum = 0
print("Math %: ", (dict["Math"]/50) * 100 )
print("Chemistry %: ", (dict["Chemistry"]/50) * 100 )
print("Physics %: ", (dict["Physics"]/50) * 100 )
for i in dict:
    sum+=dict[i]
print("Average marks: ", sum/3)
