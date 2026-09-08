import socket
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "")
PORT = int(os.getenv("PORT", ""))

socket_teste = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_teste.bind((HOST, PORT)) # Associa o socket ao endereço e porta

print(f"Servidor UDP ouvindo em {HOST}:{PORT}")

dados, endereco = socket_teste.recvfrom(1024)
print(f"Mensagem recebida de {endereco}: {dados.decode()}")
