try:
    with open("sample.txt", 'r+') as fileObj:
        lines = fileObj.read()
        fileObj.write("\nModified content: \n")
        fileObj.write(lines.replace("blue", "pink"))
except FileNotFoundError:
        print(f"Error: The file 'sample.txt' was not found.")
except PermissionError:
        print("Error: You do not have permission to write to the file sample.txt")
except Exception as e:
        print(f"An unexpected error occurred: {e}")