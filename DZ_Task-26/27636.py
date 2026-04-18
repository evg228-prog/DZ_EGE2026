with open(r'.\files\26_27636.txt') as file:
    S, N = map(int, file.readline().split())
    containers = [int(i) for i in file]

containers = sorted(containers)

ans = []
current = 0

for container in containers:
    if current + container <= S:
        ans.append(container)
        current += container
    else:
        break
print(N - len(ans), sum(containers[len(ans):]))

# 7347 472188