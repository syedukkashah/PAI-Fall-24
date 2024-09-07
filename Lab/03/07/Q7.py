try:
    with open ("replacement_needed.txt", 'r+') as file:
        content = file.read()
        lst = content.split()
        for i in range(0, len(lst)):
            if lst[i]=="byke":
                lst[i] = "bike"
        file.write("\n")
        file.write(' '.join(lst))
except FileNotFoundError:
    print("File not found")