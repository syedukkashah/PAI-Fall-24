list = [1,2,3]
list2 = ["key1", "key2", "key3"]
dict = {}
index = 0
for i in list2:
    dict[i] = list[index]
    index+=1
try:
    with open("task3.txt", 'r+') as file:
        file.write(str(dict))
        file.seek(0)
        content = file.readlines()
        print(content)
except FileNotFoundError:
    print("File not found")


