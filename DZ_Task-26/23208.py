with open(r'.\files\26_23208.txt') as file:
    N = int(file.readline())
    details = []
    for pos, data in enumerate(file, start=1):
        time1, time2 = map(int, data.split())
        if time1 < time2:
            details.append([time1, 's', pos])
        else:
            details.append([time2, 'o', pos])
details = sorted(details)

last_detail = details[-1]
cnt = sum(1 for detail in details[:-1] if detail[1] == 's')

print(last_detail[2], cnt)

# 503 478