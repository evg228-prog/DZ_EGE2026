from re import *

with open(r'.\files\24_18239.txt') as file:
    data = file.readline()

num = r'[1-9][1-9]*'
pattern = fr'\-?{num}(\-{num})+'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for match in matches:
    if eval(match) > -20_000:
        ans = max(ans, len(match))
print(ans)