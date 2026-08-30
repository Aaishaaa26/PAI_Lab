cart ={}
num = int(input("Enter number of items: "))
for i in range(num):
    idz = int(input("Enter item id: "))
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    if idz not in cart:
        cart[idz] = [price, quantity]
    else:
        cart[idz][1] += quantity

print(cart)
idz = int(input("\nEnter item id to add: "))
if idz not in cart:
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    cart[idz] = [price, quantity]
else:
    quantity = int(input("Enter quantity: "))
    cart[idz][1] += quantity

idz = int(input("\nEnter item id to remove: "))
if idz not in cart:
    print("Item not found in cart")
else:
    del cart[idz]
idz = int(input("\nEnter item id to update quantity: "))
if idz in cart:
    quantity = int(input("Enter quantity: "))
    cart[idz][1] += quantity
total = 0
for idz in cart:
    total = total + cart[idz][0] * cart[idz][1]
print("\nTotal Price: ", total)