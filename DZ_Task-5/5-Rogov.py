for N in range(1, 100_000):
    R = f'{N:b}'
    if N % 2 == 0:
        R = R.replace('0', '00')
        R = R.replace('1', '11')
    else:
        R = R.replace('0', '*')
        R = R.replace('1', '0')
        R = R.replace('*', '1')
    R = int(R, 2)
    if R > 60:
        print(N)
        break

# 8