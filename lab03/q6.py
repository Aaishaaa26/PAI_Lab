def top_k_frequent(nums, k):
    frequency = {}
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    ranked = sorted(frequency.items(), key = lambda x:x[1], reverse = True)
    result = []
    for i in range(k):
        result.append(ranked[i][0])
    return result

nums = [1,1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k))