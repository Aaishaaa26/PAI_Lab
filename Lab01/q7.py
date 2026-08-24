word = input("Enter a word: ")
length = len(word)
word = list(word)
temp = ''
for i in range(int(len(word)/2)):
    temp = word[i]
    word[i] = word[length - i - 1]
    word[length - i - 1] = temp
print("Reversed word: " + ''.join(word))