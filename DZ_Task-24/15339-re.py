from re import *

with open(r'.\files\24_15339.txt') as file:
    data = file.readline()

pattern = r'([A-Z][0-9])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 22