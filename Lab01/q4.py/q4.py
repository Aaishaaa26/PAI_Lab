numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
totalSum = 0
for i in range(0, len(numbers)):
    totalSum += numbers[i]
print("Total sum is: ", totalSum)