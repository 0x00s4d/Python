pessoas = raw_input('Digite a quantidade de pessoas: ')
i = 1
lista_de_convidados = []
while i <= int(pessoas):
    nome_convidados = raw_input('Digite o nome da pessoa'+str(i)+': ')
    lista_de_convidados.append(nome_convidados)
    i+=1
print('\nLista de Convidados:')
for nome in lista_de_convidados:
    print(nome)