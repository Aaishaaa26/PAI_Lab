transactions = []
num = int(input("Enter number of ids: "))
for i in range(num):
    id = input("Enter id: ")
    transactions.append(id)
unique = set()
duplicate = set()

for id in transactions:
    if id not in unique:
        unique.add(id)
    else:
        duplicate.add(id)

print("\nUnique idz: ", unique)