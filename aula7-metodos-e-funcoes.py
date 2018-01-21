def soma(n1, n2):
    resp = n1+n2
    return resp

retorno = soma(100, 200)
print(retorno)
print('--------------------------------------------------')

retorno2 = soma(10.2, 100.2)
print(retorno2)
print('--------------------------------------------------')

def imprimir_oi():
    print('Oi')
imprimir_oi()
print('--------------------------------------------------')

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
print(tem_sete_itens(str(raw_input('Digite uma palavra: '))))
print('--------------------------------------------------')