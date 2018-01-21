def maior(colecao):
    maior_item = colecao[0]
    for i in colecao:
        if i > maior_item:
            maior_item = i
    return maior_item
print(maior([1,2,3,4,5,6,7,8,255]))


def menor(colecao):
    menor_item = colecao[0]
    for y in colecao:
        if y < menor_item:
            menor_item = y
    return menor_item
print(menor([2,-65535,455,21,4,5]))
