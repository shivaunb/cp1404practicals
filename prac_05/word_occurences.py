"""
CP1404 Practical
Word Occurences - Count the Occurences of words in a string

Estimate: 25 minutes
Actual:
"""

word_to_amount = {}
text = input("Text: ")
words = text.split()  # convert text to list of words
print(words)  # test split worked
for word in words:
    try:
        word_to_amount[word] += 1
    except KeyError:
        word_to_amount[word] = 1

print(word_to_amount)  # test dict
