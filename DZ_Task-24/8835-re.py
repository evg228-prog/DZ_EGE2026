from re import *

with open(r'files/24_8835.txt') as file:
    data = file.readline()

pattern = r'([ A-LN-Z]*M){112}[ A-LN-Z]*\.'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 4594