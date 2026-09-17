import socket
import json
from fmsg import fmsg

BUFFER_SIZE = 2048

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_servidor.bind(("127.0.0.1", 4444))

print("Servidor UDP ouvindo em 127.0.0.1:500")

try:
    while True:
        dados, endereco = socket_servidor.recvfrom(2048)
        mensagem = json.loads(dados.decode())

        print(f"Mensagem recebida de {endereco}: {mensagem}")

        resposta = fmsg(mensagem)
        resposta_json = json.dumps(resposta)

        socket_servidor.sendto(
            resposta_json.encode(),
            endereco
        )

except KeyboardInterrupt:
    print("\nServidor encerrado.")

finally:
    socket_servidor.close()