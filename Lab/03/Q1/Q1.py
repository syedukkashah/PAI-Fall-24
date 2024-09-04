try:
    with open(r'text file.txt') as fileObj:
        content = fileObj.read()
    print("file content: ", content)
    print("Total characters: ", len(content))
    print("Word count: ", len(content.split()))
except FileNotFoundError:
    print("File not found")
