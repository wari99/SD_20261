def inverte_string(frase: str = ""):
    aux = ""
    for char in range(len(frase)-1, -1, -1):
        aux += frase[char]
    return aux

def fmsg(mensagem):
    tipo = mensagem["tipo"]
    valor = mensagem["val"]

    if tipo == "int":
        resposta = valor + 1
    elif tipo == "char":
        resposta = valor.swapcase()
    elif tipo == "string":
        resposta = inverte_string(valor)
    else:
        resposta = "Tipo inválido"

    print(
        f"Tipo: {tipo}, Mensagem: {valor}, Mensagem formatada: {resposta}"
    )

    return {
        "tipo": tipo,
        "val": resposta
    }