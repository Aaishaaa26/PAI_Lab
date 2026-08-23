
numList = [int(x) for x in input("Enter Numbers separated by spaces: ").split()]
evenNums = 0
for i in range(0, len(numList)):
    if numList[i] % 2 == 0:
        evenNums += 1
print("Even Numbers Counted: ", evenNums)