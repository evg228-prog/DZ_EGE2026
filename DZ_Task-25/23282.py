def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num  ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}
    if len(d) > 1:
        return max(d) + min(d)
    return 0

cnt = 0
for N in range(5_400_001, 10**20):
    M = f(N)
    if M > 60000 and str(M) == str(M)[::-1]:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 5400042 900009
# 5400420 90009
# 5400866 158851
# 5406116 1351531
# 5406420 90109

