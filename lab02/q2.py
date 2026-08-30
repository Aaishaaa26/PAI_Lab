products = {}

num = int(input("Number of products: "))

for i in range(num):
    id = input("Product ID: ")
    name = input("Product Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    products[id] = [name, category, price, quantity]

id = input("Enter Product ID to search: ")

if id in products:
    print(products[id])
else:
    print("Product not found")

id = input("Enter Product ID to update price: ")

if id in products:
    price = float(input("New price: "))
    products[id][2] = price

id = input("Enter Product ID to update stock: ")

if id in products:
    quantity = int(input("New quantity: "))
    products[id][3] = quantity

print("Out of stock products:")

for id in products:
    if products[id][3] == 0:
        print(products[id][0])