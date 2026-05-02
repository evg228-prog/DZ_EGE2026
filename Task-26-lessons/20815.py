with open(r'.\files\26_20815.txt') as file:
    N, S = map(int, file.readline().split())
    astronauts = []
    for i in file:
        id, e1, e2, e3, s = map(int, i.split())
        astronauts.append([e1 + e2 + e3 + s, s, id])

astronauts = sorted(astronauts, key=lambda x: (-x[0], -x[1], x[2]))

passed = astronauts[:S]
rejected = astronauts[S:]

half_score = passed[-1][0]
last_astronaut = [i[2] for i in passed[::-1] if i[0] != half_score][0]

cnt_half_astronaut = [i for i in astronauts if i[0] == half_score]
print(last_astronaut, len(cnt_half_astronaut))

# 45539 127