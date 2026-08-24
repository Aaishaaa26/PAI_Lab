x = [int(x) for x in input("Enter Numbers seperated by spaces").split()]
max = x[0]
for i in range(1, len(x)):
    if max < x[i]:
        max = x[i]
print(max)
