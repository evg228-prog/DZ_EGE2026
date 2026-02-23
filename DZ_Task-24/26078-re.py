from re import *
with open(r'.\files\24_26078.txt') as file:
    data = file.readline()

pattern = r'[0-9A-Z]*(2025){110}W{90}[0-9A-Z]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))