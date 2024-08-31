dict = {
    "John":['A', 'B', 'C'],
    "Bob" : ['B', 'B', 'B'],
    "Alice": ['D', 'A', 'C']
}
grade_to_marks = {
    'A' : 90,
    'B' : 80, 
    'C' : 70, 
    'D' : 60
}
print(dict)
dict["John"].append('A') 
print("grade added to John's list")
print(dict["John"])
sum = 0
for i in dict["John"]:
    sum+=grade_to_marks[i]
print("John's average Marks: ", sum/4)
dict['Adam'] = []
print("Adam added with empty list")
dict.pop("Bob") 
print("Bob removed")
print(dict)
