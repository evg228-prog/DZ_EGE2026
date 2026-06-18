from re import *

with open(r'.\files\24_22356.txt') as file:
    data = file.readline()

pattern = r'[1-9AB][0-9AB]*[13579B]'
matches = [match for match in finditer(pattern, data)]

num = max(matches, key=lambda x: (len(x.group()), x.group()))

print(num.start())

# 8499457