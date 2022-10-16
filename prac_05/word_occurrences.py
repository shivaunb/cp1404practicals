"""
CP1404 Practical
Word Occurrences - Count the Occurences of words in a string

Estimate: 25 minutes
Actual: 43 minutes
"""

word_to_amount = {}
text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_to_amount[word] += 1
    except KeyError:
        word_to_amount[word] = 1

words = set(list(word_to_amount.keys()))
words = sorted(words)

longest_word = 0
for word in words:
    if len(word) > longest_word:
        longest_word = len(word)

for word in words:
    print(f"{word:{longest_word}} : {word_to_amount[word]}")
