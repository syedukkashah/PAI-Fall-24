a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]
ab = [i + j for i, j in zip(a, b)]
print(ab)  
print([x + y for x, y in zip(["He", "th", "i", "sal"], ["llo", "is", "s", "man"])]) #written in one line
