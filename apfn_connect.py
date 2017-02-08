
def connect():
    from redes import GestorRedes
    import network
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    gestor = GestorRedes()
    if not wlan.isconnected():
        tentarRede(wlan, 'x', 's')

def inverterFlag(flag):
    flag = not flag

def tentarRede(lan, rede, senha):
    from machine import Time
    tim = Time(-1)
    try_flag = True

    print('tentando conexao com:',rede)
    lan.connect(rede, senha)

    tim.init(period=5000, mode=Timer.ONE_SHOT, callback = inverterFlag(try_flag))

    while not lan.isconnected() and try_flag:
        if lan.isconnected():
            print('conetado com sucesso a:', rede)
        else:
            pass

