# SD_20261

## Trabalho 1 - Sistemas Distribuídos

Este projeto implementa uma comunicação utilizando sockets UDP em Python.

O cliente envia uma mensagem para o servidor, que a processa conforme seu tipo e devolve o resultado ao cliente.

---

### Estrutura do projeto
```
base_udp/

├── client.py      # Cliente UDP  
├── servidor.py    # Servidor UDP  
├── fmsg.py        # Processamento da mensagem
```
---

### Configuração

O arquivo `.env` deve conter:

HOST=localhost  
PORT=5000

---

### Funcionamento

#### Cliente

- Cria um socket UDP;
- Envia uma mensagem para o servidor utilizando `sendto()`;
- Aguarda a resposta do servidor;
- Exibe a resposta recebida.

#### Servidor

- Cria um socket UDP;
- Realiza o `bind()` no endereço e porta definidos;
- Permanece aguardando mensagens dos clientes;
- Processa cada mensagem recebida;
- Envia o resultado de volta ao cliente.

---

### Processamento das mensagens

O processamento é realizado pelo arquivo `fmsg.py`. As regras são:

- **Inteiro:** incrementa o valor em 1.
- **Caractere:** converte para letra maiúscula.
- **String:** retorna a string invertida.

#### Exemplos

| Mensagem recebida | Resposta |
|---|---|
| `3` | `4` |
| `a` | `A` |
| `oiii` | `iiio` |
| `uerj` | `jreu` |

---

### Como executar

- Iniciar primeiro o servidor:

 ```
 python3 servidor.py
 ```

- Em outro terminal, execute o cliente:

``` 
python client.py
```

- Exemplo de saída do servidor:

    Servidor UDP ouvindo em localhost:5000
    
  ``` 
    Mensagem recebida de ('127.0.0.1', 52735): oiii
    Tipo: <class 'str'> / str, Mensagem: oiii, Mensagem formatada: iiio
  ``` 
  ``` 
    Mensagem recebida de ('127.0.0.1', 54700): 3
    Tipo: <class 'int'> / int, Mensagem: 3, Mensagem formatada: 4
  ```
  ``` 
    Mensagem recebida de ('127.0.0.1', 60685): a
    Tipo: <class 'str'> / char, Mensagem: a, Mensagem formatada: A
  ```
Este projeto utiliza o protocolo UDP (User Datagram Protocol), que não estabelece conexão entre cliente e servidor. Cada mensagem é enviada como um datagrama independente, utilizando as funções `sendto()` e `recvfrom()`.