import json
dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23, 'Syed': 46}
with open("dict.json", 'w') as file:
    json.dump(dictionary, file)

with open ("dict.json", 'r') as file:
    content = json.load(file)


print(content)
Max = content['Ali']
same = {}
name = " "
for i in content.keys():
    if Max<content[i]:
        Max = content[i]
        name = i

for i in content.keys():
    if Max == content[i] and name!= i :
        same[i] = content[i]

print("Max Age: ", Max , " Name: ", name)
print(same) #duplicate printed




