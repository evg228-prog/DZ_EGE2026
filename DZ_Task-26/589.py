with open(r'.\files\26_589.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
sum_sales = 0
max_sale = 0
for i in range(0, max(prices), 500):
    group = [j for j in prices if i < j <= i + 500]
    sum_sales += sum(group[:len(group) // 2]) / 2
    max_sale = max(max_sale, max(group[:len(group) // 2]))
print(sum_sales, max_sale / 2)

# 11493372 4877
