with open(r'text file.txt') as fileObj:
    content = fileObj.read()
cnt = 0
for i in content:
    cnt += 1
print("file content: ", content)
print("Total characters: ", cnt)
