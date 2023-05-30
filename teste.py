compras = {
    1:[{'sam1001':[['banana',5],['uva',3]]},{'sam1002':[['Limão',2]]},{'sam1003':[['Lapis',2],['Borracha',1],['Caneta',3],['Caderno',4]]}],
    2:[{'mar1001':[['Goiaba',4],['uva',1],['Laranja',6]]}]
           }


for chave1 in compras:
    for dicionario1 in compras[chave1]:
        for chave2 in dicionario1:
            for lista1 in dicionario1[chave2]:
                for k in lista1:
                    if k == 'Borracha':
                        print(lista1[0])
                        break


op = str(input('Digite o numero do pedido: '))
achei = False
for chave1 in compras:
    for dicionario1 in compras[chave1]:
        for chave2 in dicionario1:
            if op==chave2:
                teste = dicionario1[op]
                achei = True
                break
        if achei:
            break
    if achei:
        break
if achei:
    for item in teste:
        print(f'\nProduto: {item[0]}')
        print(f'Quantidade: {item[1]}')