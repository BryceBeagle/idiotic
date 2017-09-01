import re
import socket

host = ''
port = 8008

id = "xxxx"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

while True:

    csock, caddr = sock.accept()
    print("Connection from {}".format(caddr))

    request = csock.recv(1024).decode()
    print(request)
    print()

    match = re.match('GET /alarm\?id={}&status=(\w+)'.format(id), request)

    if match:

        with open('state', 'w+') as fi:
            fi.write(match.group(1))

    csock.close()