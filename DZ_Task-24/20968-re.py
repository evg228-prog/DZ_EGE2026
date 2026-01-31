from re import *
with open(r'.\files\24_20968.txt') as file:
    data = file.readline()

num = r'(0|[1-9][0-9]*[02468])'
pattern = fr'{num}([\+\*]{num})*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 130