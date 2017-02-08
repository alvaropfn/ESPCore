import json

preJson = open('./book.txt', 'r').read()

book = json.loads(preJson)

for person in book:
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