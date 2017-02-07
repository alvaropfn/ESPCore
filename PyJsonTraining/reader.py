import json

preJson = open('./book.txt', 'r').read()

book = json.loads(preJson)

for person in book:
    print(person, book[person])