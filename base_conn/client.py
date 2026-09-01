import socket

socket_teste = socket.socket()

socket_teste.connect(("localhost", 5000))

socket_teste.send("oiii".encode())
print("Message sent to server!")