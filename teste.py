compras = {
    1: [{'sam1001': [['1001', 'Banana', 6.23, 'Banana Nanica', 1],['1002','Goiaba',0.96,'Goiaba da terra',3]]},
        {'sam1002': [['1002','Goiaba',0.96,'Goiaba da terra',3]]}],
    2: [{'mar1001': [['2001','Ovo',22.30,'Ovo tamanho grande',0]]}]
           }



for chave1 in compras:
    for dicionario1 in compras[chave1]:
        for chave2 in dicionario1:
            for lista1 in dicionario1[chave2]:
                for k in lista1:
                    if k == 'Goiabxxx':
                        print(f'Nome: {lista1[1]}')
                        break

#Retorna todos pedidos de acordo com o id informado do cliente
def retornaPedidos(vid):
    pedidos = dict()
    achei = False
    for chave1 in compras:
        for dicionario1 in compras[chave1]:
            for chave2 in dicionario1:
                if chave1 == vid:
                    pedidos[chave2] = dicionario1[chave2]
                    achei = True
        if achei:
            return pedidos
            break

pedidos = retornaPedidos(1)
for chave in pedidos.keys():
    print(f'\nCod: {chave}\nProdutos:',end='')
    for item in pedidos[chave]:
        print(f' | {item[1]} - Un: {item[4]}',end='')
    print()



op = str(input('\nDigite o numero do pedido: '))
achei = False
for chave1 in compras:
    for dicionario1 in compras[chave1]:
        for chave2 in dicionario1:
            if op==chave2:
                listaProdutos = dicionario1[op]
                achei = True
                break
        if achei:
            break
    if achei:
        break
if achei:
    print(listaProdutos)
    for item in listaProdutos:
        print(f'\nProduto: {item[1]}')
        print(f'Quantidade: {item[4]}')
