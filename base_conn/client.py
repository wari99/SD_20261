import socket
import os
from dotenv import load_dotenv

load_dotenv()

HOST=os.getenv("HOST", "")
PORT=int(os.getenv("PORT", ""))

socket_teste = socket.socket()

socket_teste.connect((HOST, PORT))

socket_teste.send("oiii".encode())
print("Message sent to server!")