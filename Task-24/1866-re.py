from re import *

with open(r'files/24_1866.txt') as file:
    data = file.readline()

pattern = r'(?<=(ad|da)).+?(?=(ad|da))'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) + 2)

# 2252