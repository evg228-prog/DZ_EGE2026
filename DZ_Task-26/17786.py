with open(r'.\files\26_17786.txt') as file:
    N, V = map(int, file.readline().split())
    watermelons = [int(i) for i in file]

watermelons = sorted([i for i in watermelons if 7000 <= i <= 12000], reverse=True)

answer = []

for watermelon in watermelons:
    if sum(answer) + watermelon <= V * 1000:
        answer.append(watermelon)

print(len(answer), answer[-1])

# 75 9196
