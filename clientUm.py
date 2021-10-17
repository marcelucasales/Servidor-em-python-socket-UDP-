#clienteUm.py
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    num = 1
    mensagem_envio = input('Deseja solicitar a lista de Candidatos? -Sim ou -Nao: ').strip().lower()[0]
    if mensagem_envio == 's':
        mensagem_envio = 'candidatos'
        client.sendto(mensagem_envio.encode(), ('172.18.0.1', 12000)) # aqui deve pegar o ip do Servidor, dando o comando -> ip a <- no terminal
        mensagem_bytes, enderec_ip_server = client.recvfrom(2048)
        lista = eval(mensagem_bytes.decode())
        for key in lista:
            print(f'- Digite {num} para votar em {key}')
            num += 1
        voto = input()
        client.sendto(voto.encode(), ('172.18.0.1', 12000))
        confirmacao, enderec_ip_server = client.recvfrom(2048)
        print(confirmacao.decode())
    else:
        break
