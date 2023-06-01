clientes = {1:['sam','','Samanta Biloba','samanta@mail.com'],2:['marcos','123456','Marcos Lira','marcos@mail.com']}

iniComp = {1:2,2:1}

compras = {
    1: [{'1sa1001': [['1001', 'Banana', 6.23, 'Banana Nanica', 1],['1002','Goiaba',0.96,'Goiaba da terra',3]]},
        {'1sa1002': [['1002','Goiaba',0.96,'Goiaba da terra',3]]}],
    2: [{'2ma2001': [['2001','Ovo',22.30,'Ovo tamanho grande',0]]}]
           }

carrinho = {2: ['1001', 'Banana', 6.23, 'Banana Nanica', 90]}




'''
for chave1 in compras:
    for dicionario1 in compras[chave1]:
        for chave2 in dicionario1:
            for lista1 in dicionario1[chave2]:
                for k in lista1:
                    if k == 'Goiaba' and chave2=='1sa1002':
                        if lista1[4] > 0:
                            print(f'QTD: {lista1[4] - 1}')
                            break
                        else:
                            print('Quantidade em estoque insuficiente.')

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
achei = False
for chave in pedidos.keys():
    if (chave == 'sam1001'):
        achei = True
        total = 0
        print(f'Codigo do pedido: {chave}')
        print(f'Total de produtos: {len(pedidos[chave])}')
        for item in pedidos[chave]:
            print(f'\n{item[1]}')
            print(f'R$ {item[2]} | un. {item[4]}')
            print(f'Descrição: {item[3]}')
            parcial = item[2] * item[4]
            total += parcial
        print(f'\nTotal da compra: R$ {total}')
    if achei:
        break

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
'''