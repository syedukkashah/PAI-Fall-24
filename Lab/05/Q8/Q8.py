import re
with open("text.txt", "r+") as file:
    data = file.read()
reg = r"\b\d{2}/\d{2}/\d{4}\b"
reg += r"|"
reg += r"\b\d{4}-\d{2}-\d{2}\b"
reg += r"|"
reg += r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}\b"
dates = re.findall(reg, data)
print(dates)
