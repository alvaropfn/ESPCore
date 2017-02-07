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

with open('./book.txt', 'w') as f: f.write(data)

