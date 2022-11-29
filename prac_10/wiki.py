"""
CP1404 - Practical 10
Wikipedia API & Python Library
"""
import wikipedia

query = input("Enter page title or query phrase in quotation marks: ")
while query != "":
    search = wikipedia.page(query)
    print(search.title)
    print(search.url)
    try:
        print(wikipedia.summary(str(query)))
        query = input("Enter page title or query phrase: ")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        query = input("Enter page title or query phrase: ")
