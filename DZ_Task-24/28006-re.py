from re import *

with open(r'.\files\24_28006.txt') as file:
    data = file.readline()

chet = r'([2468]|[1-9][0-9]*[02468])'
non_chet = r'([13579]|[1-9][0-9]*[13579])'

pattern = fr'(\({chet}[+-]{non_chet}\))+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 89