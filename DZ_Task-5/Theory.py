# Наибольший N при наибольшем R
ans.append([R, N])
print(max(ans))

# Наибольший N при наименьшем R
ans.append([R, N])
ans = sorted(ans, key=lambda x:(x[0], - x[1]))
print(ans[0])

# Наименьший N при наименьшем R
ans.append([R, N])
print(min(ans))

# Наименьший N при наибольшем R
ans.append([R, N])
ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0])
