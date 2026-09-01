import socket 


socket_teste = socket.socket() 

socket_teste.bind(("localhost", 5000)) # disponível em localhost na porta 5000 

socket_teste.listen() # aguardando conexao
    
conn, address = socket_teste.accept() 

msg = conn.recv(1024) # mensagem pode ser de até 1024 bytes

print(msg)

