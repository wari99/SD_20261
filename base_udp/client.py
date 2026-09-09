import socket
import os
from dotenv import load_dotenv
import time

load_dotenv()

HOST = os.getenv("HOST", "")
PORT = int(os.getenv("PORT", ""))

socket_teste = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = "a"

inicio = time.perf_counter()

socket_teste.sendto(mensagem.encode(), (HOST, PORT))

dados, endereco = socket_teste.recvfrom(1024)

fim = time.perf_counter()

print("Resposta do servidor:", dados.decode())
print(f"RTT: {(fim - inicio) * 1000:.2f} ms")

socket_teste.close()
