
class GestorRedes:
    redes = {}

    def __init__(self):
        import json
        try:
            pre_json = open('./redes.txt', 'r').read()
            print('inicio padrao')
            self.redes = json.loads(pre_json)
        except:
            print('inicio bruto')
            self.inicio_bruto()
            self.salvar_redes()
        
    def listar_redes(self):
        for id in self.redes:
            print(id, self.redes[id])
    
    def salvar_redes(self):
        import json
        to_save = json.dumps(self.redes)
        with open('./redes.txt', 'w') as f: f.write(to_save)

    def inicio_bruto(self):
        self.redes[0] = {"addr": "apfn", "pasw": "elevel12"}
        self.redes[1] = {"addr": "nmdn", "pasw": "nmdn.691"}
        self.redes[2] = {"addr": "Jaques", "pasw": "Harien22"}

    def remover_rede(self, index):
        for id in self.redes:
            if int(id) >= index:
                try:
                    #self.redes[id] = self.redes[id+1]
                    print(self.redes[int(id)+1])
                except:
                    print(int(id)+1)
                finally:
                    self.salvar_redes()
                

r = GestorRedes()
r.listar_redes()
r.remover_rede(1)
print('#######################################')
r.listar_redes()



