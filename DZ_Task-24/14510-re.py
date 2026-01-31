from re import *
with open(r'.\files\24_14510.txt') as file:
    data = file.readline()

vow = 'AEIOUY'
con = '[]'
pattern = r'(([^AEIOUY][^AEIOUY][AEIOUY]){500})'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)))