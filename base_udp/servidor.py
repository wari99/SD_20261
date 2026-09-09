import socket
import os
from dotenv import load_dotenv
from fmsg import fmsg

load_dotenv()

HOST = os.getenv("HOST", "")
PORT = int(os.getenv("PORT", ""))

socket_teste = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_teste.bind((HOST, PORT))

print(f"Servidor UDP ouvindo em {HOST}:{PORT}")

try:
    while True:
        dados, endereco = socket_teste.recvfrom(1024)
        mensagem = dados.decode()
        
        print(f"Mensagem recebida de {endereco}: {mensagem}")

        resposta = fmsg(mensagem)
        socket_teste.sendto(str(resposta).encode(), endereco)

except KeyboardInterrupt:
    print("\nServidor encerrado.")

finally:
    socket_teste.close()
