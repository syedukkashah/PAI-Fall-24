import re
pattern = "phone"
text = "The agent’s phone number is 408-555-1234. Call soon!"
search_pattern = re.search(pattern, text)
print(search_pattern.span())
print(search_pattern.string)
print(search_pattern.start())
print(search_pattern.end())
sample = "ok dmskkdmk ok dnjsdn ok ok njdsj"
matches = re.findall('ok', sample)
print(matches)
print(len(matches))
phone = "405-555-1234"
phone_search = re.search(r'\d{3}-\d{3}-\d{4}', phone)
print(phone_search)
print(phone_search.group())
print(re.search(r'cat|dog', 'the dog is here'))
print(re.search(r'cat', 'the dog is here'))
