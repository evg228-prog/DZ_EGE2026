from re import *
with open(r'.\files\24_9075.txt') as file:
    data = file.readline()

pattern = r'(([^02468][13579])|([^13579][02468]))+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))