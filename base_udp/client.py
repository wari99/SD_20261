import socket
import json
import time
import sys

BUFFER_SIZE = 2048

def menu(tipo):
    if tipo == "int":
        valor = input("* Digite um número inteiro: ")

        try:
            return int(valor)
        except ValueError:
            print("Digite um número inteiro válido.")

    elif tipo == "char":
        valor = input("* Digite um caractere: ")

        if len(valor) == 1:
            return valor
        print("Digite apenas UM caractere.")

    elif tipo == "string":
        return input("Digite uma string: ")

porta = int(sys.argv[1]) if len(sys.argv) > 1 else 4444

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\n* Cliente UDP\n * Escolha o tipo de mensagem:\n 1- int\n 2- char\n 3- string\n 0- sair")

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

    t_inicio = time.perf_counter() 
    socket_cliente.sendto(mensagem_json.encode(), ("127.0.0.1", porta))
    t_apos_sendto = time.perf_counter()

    dados, endereco = socket_cliente.recvfrom(BUFFER_SIZE)
    t_fim = time.perf_counter()

    tempo_sendto = (t_apos_sendto - t_inicio) * 1000 # Tempo do sendto()
    tempo_resposta = (t_fim - t_apos_sendto) * 1000 # Tempo após sendto() até o recvfrom()

    resposta = json.loads(dados.decode())

    print(
        f"\nResposta do servidor: {resposta}\n"
        f"\nValor retornado: {resposta['val']}\n"
        f"Tempo do sendto: {tempo_sendto:.4f} ms\n"
        f"RTT: {tempo_resposta:.4f} ms\n- - - - - -\n\n"
    )

socket_cliente.close()