string = str(input("Enter a string: "))
reverse = ""
for char in string:
    reverse = char + reverse

print(reverse)