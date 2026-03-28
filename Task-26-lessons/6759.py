with open(r'.\files\26_6759.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods)
sale_prods = N // 3

start = sum(prods) - sum(prods[-sale_prods:])
end = sum(prods) - sum(prods[::-1][2::3])

print(start, end)

# 22262050 33246829