numbers = [int(x) for x in input("Enter Numbers separated by spaces: ").split()]
element = int(input("Enter Element to delete values less than that: "))
length = len(numbers) - 1
for i in range(length, -1, -1):
    if numbers[i] < element:
        del numbers[i]
print(numbers)