from re import *
with open(r'.\files\24_1428.txt') as file:
    data = file.readline()

pattern = r'(^|(?<=(XY|XZ))).+?($|(?=(XY|XZ)))'
ans = 0
for match in finditer(pattern, data):
    cnt_XY_XZ = match.groups().count('XY') + match.groups().count('XZ')
    ans = max(ans, len(match.group()) + 2 if cnt_XY_XZ else 1)
print(ans)
# 25