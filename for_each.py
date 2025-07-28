import time
products = ['Banana', 'salt', 'bread', 'cheese']

a_products = []
for product in products:
    # print(products)
    if 'a' in product.lower():
        a_products.append(product)
    # products.append('121'*500)

print(a_products)

a_products_comprehension = [product for product in products if 'a' in product.lower()]
print(a_products_comprehension)
