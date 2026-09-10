def is_anagram(s, t):
    s = s.lower()
    t = t.lower()

    if len(s) != len(t):
        return False
    frequency1 = {}
    frequency2 = {}
    for char in s:
        if char not in frequency1:
            frequency1[char] = 1
        else:
            frequency1[char] += 1
    for char in t:
        if char not in frequency2:
            frequency2[char] = 1
        else:
            frequency2[char] += 1

    if frequency1 == frequency2:
        return True
    else:
        return False


s = input("Enter string 1: ")
t = input("Enter string 2: ")
if is_anagram(s, t):
    print("Anagrams")
else:
    print("Not Anagrams")
