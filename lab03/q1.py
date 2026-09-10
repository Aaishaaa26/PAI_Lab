text = """
machine learning is powerful
machine learning helps analyze data
data science uses machine learning
"""
text = text.lower()
words = text.split()

frequency = {}
for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1
print("Frequency of words: ", frequency)
most_frequent = ""
highest_frequency = 0
for word in frequency:
    if frequency[word] > highest_frequency:
        highest_frequency = frequency[word]
        most_frequent = word
print("Most frequent word:", most_frequent)
unique_Words = set(words)
print("Unique Words: ", unique_Words)

repeated_words = []
for word in frequency:
    if frequency[word] > 1:
        repeated_words.append(word)
print("Repeated Words: ", repeated_words)