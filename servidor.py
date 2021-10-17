#servidor.py
import socket # importação do socket
candidatos = { 'Lula':0, 'Bolsonaro':0, 'Marcel':0, 'Xavier':0 } # estrutura de dados (dicionário, tabela hash, etc) com os valores necessários
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ipv4 , Protocolo UDP
servidor.bind(('', 12000)) # localhost , porta 12000
while True: # loop infinito de escuta
    envia = str(candidatos)
    inex = 'Voto Confirmado'
    mensagem_bytes, endereco_ip_client = servidor.recvfrom(2048)
    mensagem_resposta = mensagem_bytes.decode().lower()
    if mensagem_resposta == 'candidatos':
        servidor.sendto(envia.encode(), endereco_ip_client)
        voto, endereco_ip_client = servidor.recvfrom(2048)
        voto = voto.decode()
        if voto == '1':
            candidatos['Lula']+= 1
        elif voto == '2':
            candidatos['Bolsonaro']+= 1
        elif voto == '3':
            candidatos['Marcel']+= 1
        elif voto == '4':
            candidatos['Xavier']+= 1
        else:
            inex = 'Candidato Inexistente'
        servidor.sendto(inex.encode(), endereco_ip_client)
        print(f'Solicitou os {mensagem_resposta}.')
    elif mensagem_resposta == 'total':
        servidor.sendto(envia.encode(), endereco_ip_client)
        print(f'Solicitou o {mensagem_resposta} de votos.')
