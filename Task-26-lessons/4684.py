with open(r'.\files\26_4684.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods)
sale_prods = N // 6

one_check = sum(prods) - sum(prods[:sale_prods]) // 2
many_check = sum(prods) - sum(prods[::-1][5::6]) // 2

print(many_check, one_check)

# 46201709 49699604