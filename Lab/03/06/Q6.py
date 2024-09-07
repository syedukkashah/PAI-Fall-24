def is_ques(fname):
    try:
        with open(fname, 'r') as file:
            content = file.read()
            return content[len(content)-1] == '?'
    except FileNotFoundError:
        print("File not found")
try:
    with open('questions.txt', 'w') as file:
        file.write("What is your name?")
except FileNotFoundError:
    print("File not found")
if is_ques('questions.txt'):
    print("it is a question")
else:
    print("Not a question")