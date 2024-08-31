list1 = ["key 1", "key 2", " key 3"]
list2 = [1, 2, 3]
dict = {}
index = 0
for i in list1:
    dict[i] = {list2[index]}
    index+=1
print(dict)