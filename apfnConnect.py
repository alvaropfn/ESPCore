def connectar():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not lan.isconnected():
        tentarRede(rede, senha)



def tentarRede(lan, rede, senha):
    from machine import Timer
    tim = Timer(-1)

    tryFlag = True

    print('tentando conectar a rede:', rede)
    lan.connect(rede, senha)

    tim.init(period = 5000, mode=Timer.ONE_SHOT, callback = lambda: tryFlag = False)

    while not lan.isconnected() and tryFlag:
        pass
    

'''
classe usada como estrutura para guardar a lista de redes
'''
class Redes:
    import json
    redes = {}
    size = 0

    def __init__(self):
        self.redes[0] = {'wifi': 'apfn', 'pasw': 'elevel12'}
        self.redes[1] = {'wifi': 'nmdn', 'pasw': 'nmdn.691'}
        self.redes[2] = {'wifi': 'Jaques', 'pasw': 'Harien22'}
        #self.redes[3] = {'wifi': 'x', 'pasw': 'y'}
    
    def salvarRedes():
        with open('./redes.txt', 'w') as f: f.write(data)
        
