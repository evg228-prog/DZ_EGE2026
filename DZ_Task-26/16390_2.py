with open(r'.\files\26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    weights = [int(i) for i in file]

weights = sorted(weights)
truck = [weights[0]]

for weight in weights[1:]:
    if weight + sum(truck) <= S:
        truck.append(weight)

truck.pop()
for weight in weights[::-1]:
    if weight + sum(truck) <= S:
        truck.append(weight)
print(len(truck), truck[-1])

# 2216 56