def start_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        try_wifi(wlan, 'x', 's')

def invertFlag(flag):
    flag = not flag

def try_wifi(lan, rede, senha):
    from machine import Time
    tim = Time(-1)
    try_flag = True

    print('tentando conexao com:',rede)
    lan.connect(rede, senha)

    tim.init(period=5000, mode=Timer.ONE_SHOT, callback = invertFlag(try_flag))

    while not lan.isconnected() and try_flag:
        if lan.isconnected():
            print('conetado com sucesso a:', rede)
        else:
            pass

