'''
classe usada como estrutura para guardar a lista de redes
'''
class Redes:
    
    import json
    redes = {}
    size = 0
    arquivo = './redes.txt'

    def __init__(self):
        self.inicioForcado()
        preJson = open(self.arquivo, 'r').read()
    
    def salvarRedes(self):
        with open(self.arquivo, 'w') as f: f.write(self.redes)

    def addRede(self, rede, senha):
        #TODO
        pass
    
    def listarRedes(self):
        for index in self.redes:
            print(index, self.redes[index])
    
    def CorrigirRede(self):
        #TODO
        pass

    def inicioForcado(self):
        self.redes[0] = {'wifi': 'apfn', 'pasw': 'elevel12'}
        self.redes[1] = {'wifi': 'nmdn', 'pasw': 'nmdn.691'}
        self.redes[2] = {'wifi': 'Jaques', 'pasw': 'Harien22'}
        #self.redes[3] = {'wifi': 'x', 'pasw': 'y'}