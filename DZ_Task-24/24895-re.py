from re import *
with open(r'.\files\24_24895.txt') as file:
    data = file.readline()

num = r'[1-9]+'
pattern = fr'{num}([\+\*]{num}){{0,39}}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# Не работает, регулярка не справиться с наложениями