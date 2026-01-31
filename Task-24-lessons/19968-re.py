from re import *
with open(r'.\files\24_19968.txt') as file:
    data = file.readline()

num = r'(0|[1-5][0-5]*)'
pattern = fr'{num}([\+\*][1-5][0-5]*)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 26