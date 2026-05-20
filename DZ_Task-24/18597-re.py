from re import *

with open(r'.\files\24_18597.txt') as file:
    data = file.readline()

num = r'[1-9][0-9]{3}\.[0-9]+'
pattern = fr'{num}(&{num})+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 45
