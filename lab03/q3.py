def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return False
    return True

nums = [3,7,9,7]
if contains_duplicate(nums):
    print("Doesnt Contain duplicate")
else:
    print("Contains duplicate")