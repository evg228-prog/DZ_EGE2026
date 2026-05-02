with open(r'.\files\9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    a, b, c, d = line
    if max(line) < sum(line) - max(line):
        if a + b != c + d and a + c != b + d and a + d != c + b:
            ans += 1
print(ans)

print(f'{1023:b}'.count('1'))
# 10000000000
# 2354