import socket
import signal
import sys

ClientSocket = socket.socket()
host = '192.168.56.102'
port = 8828                     #port connected

print('Waiting for connection from server')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input = input('Enter any input: ')

    if Input == 'exit':
        break
    else:
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()
