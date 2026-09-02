import socket 
import os
from dotenv import load_dotenv

load_dotenv()

HOST=os.getenv("HOST", "")
PORT=int(os.getenv("PORT", ""))

socket_teste = socket.socket() 

socket_teste.bind((HOST, PORT)) # disponível em localhost na porta 5000 

socket_teste.listen() # aguardando conexao
print("Listening...")

conn, address = socket_teste.accept() 
print("Client connected!")

msg = conn.recv(1024).decode()
print("Message received: ", msg)

conn.close()
socket_teste.close()

print("Server is closed.")
