R = 4**36 + 3 * 4**20 + 4**15 + 2 * 4**7 + 49
new_R = f'{R:x}'

x = dict()
for letter in new_R:
    x[letter] = new_R.count(letter, 0)
print(x)

############################################

from collections import Counter
new_R = Counter(new_R)
print(new_R)

# 5
