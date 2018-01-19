import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Criar estrutura do socket
client.connect((target_host,target_port))                   #conexao
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")   #envio de dados
response = client.recv(4096)                                #retornar dados

print response