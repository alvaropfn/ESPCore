def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(1024)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()


'''################################################################'''

def watchASCII():
    import socket
    host = "towel.blinkenlights.nl"
    addr = socket.getaddrinfo(host, 23)[1][-1]

    print(addr)

    s = socket.socket()
    s.connect(addr)

    while True:
        data = s.recv(1024)
        print(str(data, 'utf8'), end='')

#watchASCII()
#http_get('http://micropython.org/ks/test.html')
