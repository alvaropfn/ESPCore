'''@author alvaropfn
Objeto usado para gerir as redes (salvar, deletar, recuperar, conectar)
'''
class GestorRedes:
    redes = []
    local = './redes.rds'
    addr = 'addr'
    pasw = 'pasw'

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
    inicia o processo de conexão com a lista de redes salva e conhecidas
     '''
    def conectar_conhecidos(self):
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        gestorRedes = GestorRedes()
        if not wlan.isconnected():
            for each in gestorRedes.obter_redes():
                self.tentarRede(wlan, each[self.addr], each[self.pasw])
    
    '''@author alvaropfn
    metodo privado usado para marcar a passagem de um tempo prederminado de espera

    @param flag flag invertida marcando o fim do tempo de espera de uma tentativa de conexao
     '''
    def inverterFlag(self,flag):
        flag = not flag
    
    '''@author alvaropfn
    inicia o processo de conexão com a lista de redes salva e conhecidas
     '''
    def tentarRede(self, lan, rede, senha):
        from machine import Time
        tim = Time(-1)
        try_flag = True

        print('tentando conexao com:',rede)
        lan.connect(rede, senha)

        tim.init(period=5000, mode=Timer.ONE_SHOT, callback = self.inverterFlag(try_flag))

        while not lan.isconnected() and try_flag:
            if lan.isconnected():
                print('conetado com sucesso a:', rede)
            else:
                pass
    
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
        self.redes.append({self.addr: "apfn", self.pasw: "elevel12"})
        self.redes.append({self.addr: "nmdn", self.pasw: "nmdn.691"})
        self.redes.append({self.addr: "Jaques", self.pasw: "Harien22"})

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
