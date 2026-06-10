with open(r'.\files\26_8581.txt') as file:
    N = int(file.readline())
    K = int(file.readline())
    M = int(file.readline())
    weights = [int(i) for i in file]

weights = sorted(weights)
refrigerators = [0] * K
last_free = 0
last_camera = 0

for i in range(K):
    while weights:
        free = M - refrigerators[i]
        if weights[-1] <= free:
            refrigerators[i] += weights.pop()
            last_camera = i + 1
            last_free = M - refrigerators[i]
        elif weights[0] <= free:
            refrigerators[i] += weights.pop(0)
            last_camera = i + 1
            last_free = M - refrigerators[i]
        else:
            break

print(last_camera, last_free)

# 426 5783
