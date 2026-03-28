with open(r'.\files\26_4660.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods)
sale_products = N // 4

one_check = sum(prods) - sum(prods[:sale_products]) // 2
many_chek = sum(prods) - sum(prods[::-1][3::4]) // 2

print(many_chek, one_check)

# 44101521 48825239