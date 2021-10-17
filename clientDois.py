#clienteDois.py
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    mensagem_envio = input('Deseja solicitar a totalização de votos? -Sim ou -Nao: ').strip().lower()[0]
    if mensagem_envio == 's':
        mensagem_envio = 'total'
        client.sendto(mensagem_envio.encode(), ('172.18.0.1', 12000)) # aqui deve pegar o ip do Servidor, dando o comando -> ip a <- no terminal
        mensagem_bytes, enderec_ip_server = client.recvfrom(2048)
        lista = eval(mensagem_bytes.decode())
        for key, value in lista.items():
            print(f'{key} com {value} voto(s).')
        if lista['Bolsonaro'] > lista['Lula'] and lista['Bolsonaro'] > lista['Marcel'] and lista['Bolsonaro'] > lista['Xavier']:
            print('Bolsonaro venceu!')
        elif lista['Lula'] > lista['Bolsonaro'] and lista['Lula'] > lista['Marcel'] and lista['Lula'] > lista['Xavier']:
            print('Lula venceu!')
        elif lista['Marcel'] > lista['Lula'] and lista['Marcel'] > lista['Bolsonaro'] and lista['Marcel'] > lista['Xavier']:
            print('Marcel venceu!')
        elif lista['Xavier'] > lista['Lula'] and lista['Xavier'] > lista['Marcel'] and lista['Xavier'] > lista['Bolsonaro']:
            print('Xavier venceu!')
        else:
            print('Ainda não houve um ganhador.') 
    else:
        break
