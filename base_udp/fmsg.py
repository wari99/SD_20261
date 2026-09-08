#mensagem = "98"
#mensagem = "m"
mensagem = "uerj"

def inverte_string(frase: str = ""):
    aux = ""
    for char in range(len(frase)-1, -1, -1):
        aux += frase[char]
    return aux

if mensagem.isdigit():
    mensagem = int(mensagem)
    devolucao = mensagem + 1
    tipo = "int"
elif len(mensagem)==1:
    devolucao = mensagem.upper()
    tipo = "char"
else:
    devolucao = inverte_string(mensagem)
    tipo = "str"

print(f"Tipo: {type(mensagem)} / {tipo}, Mensagem: {mensagem},  Mensagem formatada: {devolucao}")