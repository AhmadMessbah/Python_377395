import re
txt = input("Enter a sentence: ")
print(re.findall(r"\d", txt))
print(re.findall(r"\w", txt))