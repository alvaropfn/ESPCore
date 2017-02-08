def connectar():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
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
    

