import json

book = {}

book['tom'] = {
    'addr': 'red street, RN',
    'phone': 123456789
}

book['ana'] = {
    'addr': 'blue street, RN',
    'phone': 987654321
}

data = json.dumps(book)

<<<<<<< HEAD
with open('./book.txt', 'w') as f: f.write(data)

=======
with open('./book.txt', 'w') as f: f.write(data)
>>>>>>> bf5650e83842e6e63377c665cb8e5780d2abe1ed
