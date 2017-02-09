
def connect():
    from redes import GestorRedes
    import network
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    gestorRedes = GestorRedes()
    if not wlan.isconnected():
        for each in gestorRedes.obter_redes():
            tentarRede(wlan, each['addr'], each['pasw'])

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

