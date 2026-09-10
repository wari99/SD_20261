import socket
import os
import json
import time
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "")
PORT = int(os.getenv("PORT", ""))

socket_teste = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(
    "\n* Cliente UDP\n"
    "Escolha o tipo de mensagem:\n"
    "1 - int\n"
    "2 - char\n"
    "3 - string\n"
    "0 - sair"
)

while True:
    opcao = input("\nDigite uma opção: ")

    if opcao == "0":
        print("Cliente encerrado.")
        break

    if opcao == "1":
        tipo = "int"

        while True:
            valor = input("Digite um número inteiro: ")

            try:
                valor = int(valor)
                break
            except ValueError:
                print("Digite um número inteiro válido.")

    elif opcao == "2":
        tipo = "char"

        while True:
            valor = input("Digite um caractere: ")

            if len(valor) == 1:
                break

            print("Digite apenas UM caractere.")

    elif opcao == "3":
        tipo = "string"
        valor = input("Digite uma string: ")

    else:
        print("Opção inválida.")
        continue

    mensagem = {
        "tipo": tipo,
        "val": valor
    }

    mensagem_json = json.dumps(mensagem)

    print(f"\nEnviando: {mensagem_json}")

    inicio = time.perf_counter()

    socket_teste.sendto(
        mensagem_json.encode(),
        (HOST, PORT)
    )

    dados, endereco = socket_teste.recvfrom(1024)

    fim = time.perf_counter()
    resposta = json.loads(dados.decode())

    print(
        f"\n- - -\nResposta do servidor: {resposta}"
        f"\nValor: {resposta['val']}, RTT: {(fim - inicio) * 1000:.2f} ms\n"
    )

socket_teste.close()