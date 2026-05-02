with open(r'.\files\26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = []
    for i in file:
        id, e1, e2, e3, s = map(int, i.split())
        sailors.append([e1 + e2 + e3, s, id])

sailors = sorted(sailors, key=lambda x: (-x[0], -x[1], x[2]))

passed = sailors[:S]
rejected = sailors[S:]

half_score = passed[-1][0]
last_sailor = [sailor[2] for sailor in passed[::-1] if sailor[0] != half_score][0]

cnt_half_sailor = [i for i in sailors[::-1] if i[0] == half_score]
print(last_sailor, len(cnt_half_sailor))

# 7600410 14