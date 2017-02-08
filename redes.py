'''@author alvaropfn
Objeto usado para gerir as redes (salvar, deletar, recuperar)
'''
class GestorRedes:
    redes = []
    local = './redes.rds'

    '''@author alvaropfn
    inicializa o objeto gestor de redes
    caso seja a primeira vez que seja inicializado o inicio bruto e acionado
    '''
    def __init__(self):
        import json
        try:
            saved = open(self.local, 'r').read()
            print('inicio padrao')
            self.redes = json.loads(saved)
        except:
            print('inicio bruto')
            self.inicio_bruto()
            self.salvar_redes()
    
    '''@author alvaropfn
    recebe uma lista de redes e adiciona elas alista self.redes
     e em seguida persiste self.redes em arquivo e printa a quantidade de redes adicionadas
     
     @param redes[n] = {addr": address, "pasw": passsword}
     '''
    def add_redes(self, redes):
        for rede in redes:
            self.redes.append(rede)
        self.salvar_redes()
        print(len(redes), "redes adicionadas")

    '''@author alvaropfn
    lista todas as redes presentes na lista self.redes
    '''
    def listar_redes(self):
        for id in self.redes:
            print(id, self.redes[id])
    
    '''@author alvaropfn
    persiste as self.redes em arquivo

    printa a quantidade de redes atuais
    '''
    def salvar_redes(self):
        import json
        to_save = json.dumps(self.redes)
        with open(self.local, 'w') as f: f.write(to_save)
        print(len(self.redes), "redes persistidas")
        

    '''@author alvaropfn
    TODO
    UNDER_TEST
    '''
    def inicio_bruto(self):
        self.redes.append({"addr": "apfn", "pasw": "elevel12"})
        self.redes.append({"addr": "nmdn", "pasw": "nmdn.691"})
        self.redes.append({"addr": "Jaques", "pasw": "Harien22"})

    '''@author alvaropfn
    remove uma rede da lista de self.redes e em seguida persiste a alteração
    
    caso o index não encontre nem um item na lista printa um erro

    @param index o indice da rede a ser removida
    '''
    def remover_rede(self, index):
        try:
            self.redes.pop(index)
            self.salvar_redes()
        except:
            print("erro ao deletar o elemento:", index)
    
    '''@author alvaropfn
    retor a lista de redes do GestorRedes

    @return a lista de self.redes
    '''
    def obter_redes(self):
        return self.redes
