import socket
import json
from fmsg import fmsg

socket_teste = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_teste.bind(("localhost", 500))

print("Servidor UDP ouvindo em localhost:500")

try:
    while True:
        dados, endereco = socket_teste.recvfrom(1024)
        mensagem = json.loads(dados.decode())

        print(f"Mensagem recebida de {endereco}: {mensagem}")

        resposta = fmsg(mensagem)
        resposta_json = json.dumps(resposta)

        socket_teste.sendto(
            resposta_json.encode(),
            endereco
        )

except KeyboardInterrupt:
    print("\nServidor encerrado.")

finally:
    socket_teste.close()