with open(r'.\files\26_4629.txt') as file:
    N = int(file.readline())
    products = [int(i) for i in file]

products = sorted(products)
sale_products = N // 4

customer = sum(products) - sum(products[-sale_products:]) // 2
store = sum(products) - sum(products[:sale_products]) // 2

print(customer, store)

# 39434611 48825239