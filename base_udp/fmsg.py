def inverte_string(frase: str = ""):
    aux = ""
    for char in range(len(frase)-1, -1, -1):
        aux += frase[char]
    return aux

def fmsg(mensagem):

    if mensagem.isdigit():
        mensagem = int(mensagem)
        resposta = mensagem + 1
        tipo = "int"
    elif len(mensagem)==1:
        resposta = mensagem.upper()
        tipo = "char"
    else:
        resposta = inverte_string(mensagem)
        tipo = "str"

    print(f"Tipo: {type(mensagem)} / {tipo}, Mensagem: {mensagem}, Mensagem formatada: {resposta}")

    return resposta