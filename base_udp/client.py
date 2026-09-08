import socket
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "")
PORT = int(os.getenv("PORT", ""))

socket_teste = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket UDP

mensagem = "oiii"

socket_teste.sendto(mensagem.encode(), (HOST, PORT)) # Envia a mensagem para o servidor

print("Mensagem enviada ao servidor!")

socket_teste.close()
