def majority_element(nums):
    length = len(nums)
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    length = length/2
    majority = []
    for num in frequency:
        if frequency[num] > length:
            majority.append(num)
    return majority

nums = [3,7,9,7,7,9,7]
print("Majority element: ", majority_element(nums))