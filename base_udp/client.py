import socket
import json
import time
import sys

def menu(tipo):
    if tipo == "int":
        while True:
            valor = input("Digite um número inteiro: ")

            try:
                return int(valor)
            except ValueError:
                print("Digite um número inteiro válido.")

    elif tipo == "char":
        while True:
            valor = input("Digite um caractere: ")

            if len(valor) == 1:
                return valor

            print("Digite apenas UM caractere.")

    elif tipo == "string":
        return input("Digite uma string: ")

porta = int(sys.argv[1]) if len(sys.argv) > 1 else 4444

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\n* Cliente UDP\n Escolha o tipo de mensagem:\n 1- int\n 2- char\n 3- string\n 0- sair")

while True:
    opcao = input("\nDigite uma opção: ").lower()

    if opcao in ("0", "sair"):
        print("Cliente encerrado.")
        break
    if opcao in ("1", "int"):
        tipo = "int"
    elif opcao in ("2", "char"):
        tipo = "char"
    elif opcao in ("3", "string", "str"):
        tipo = "string"

    valor = menu(tipo)
    mensagem = {"tipo": tipo, "val": valor}
    mensagem_json = json.dumps(mensagem)

    print(f"\n- - - - - -\nEnviando: {mensagem_json}")

    inicio = time.perf_counter()

    socket_cliente.sendto(mensagem_json.encode(), ("localhost", porta))
    dados, endereco = socket_cliente.recvfrom(1024)

    fim = time.perf_counter()

    resposta = json.loads(dados.decode())

    print(f"\nResposta do servidor: {resposta}\nValor: {resposta['val']}, RTT: {(fim - inicio) * 1000:.2f} ms\n- - - - - -")

socket_cliente.close()