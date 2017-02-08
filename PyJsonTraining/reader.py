import json

preJson = open('./book.txt', 'r').read()

book = json.loads(preJson)

for person in book:
<<<<<<< HEAD
    print(person, book[person])
=======
    print(person, book[person])

    
'''
redes[0] = {'addr': 'rede0', 'pasw': 'senha0'}
redes[1] = {'addr': 'rede1', 'pasw': 'senha1'}

to_save = json.dumps(redes)
with open('./redes.txt', 'w') as f: f.write(to_save)
####################################################
pre_json = open('./redes.txt', 'r').read()

redes = json.loads(pre_json)

for id in redes:
    print(id, redes[id])
'''
>>>>>>> bf5650e83842e6e63377c665cb8e5780d2abe1ed
