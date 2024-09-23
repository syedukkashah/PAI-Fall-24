f = open("newFile.txt", "x") #x used to create a new file
f.close()
f = open("newFile.txt", "w")
f.write("PAI file handling sample")
print(f.tell()) #locates file ptr
f.close()
f = open("newFile.txt", "r") #r for reading, r+ for reading first then writing , w+ for writing first then reading
data = f.read()
print(data)
f.close()
f = open("newFile.txt", "a") #append, a+ for append, write, read
f.write("append text")
f.close()
f = open("newFile.txt", "r")
data = f.read()
print(data)
f.close()
