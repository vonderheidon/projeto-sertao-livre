from layouts import *
from bd import *

def menuCliente(texto):
    while True:
        menu = layMsec(texto)
        if (menu == '1'):
            cadastrarUsuario('cliente')
        elif (menu == '2'):
            cid = entrar('cliente')
            if (cid != None):
                menuPrincipal(cid)
                break
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def menuPrincipal(cid):
    while True:
        texto = ('\n[1] - Meu perfil\n[2] - Minhas Compras\n[3] - Pesquisar produtos\n[4] - Ver Carrinho\n[0] - Sair da conta')
        menu = layMPrincipal(clientes, cid, texto)
        if (menu == '1'):
            meuPerfil(cid)
        elif (menu == '2'):
            minhasCompras(cid)
        elif (menu == '3'):
            pesquisarProd(cid)
        elif (menu == '4'):
            pesquisarProd(cid)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def meuPerfil(cid):
    while True:
        menu = layMmperf(clientes, cid)
        if (menu == '1'):
            atualizarInfoPessoais(cid)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def atualizarInfoPessoais(cid):
    while True:
        menu = layAttinf(clientes, cid)
        if (menu == '1'):
            atualizarDados(clientes, cid, 'O seu nome completo', 3, 2)
        elif (menu == '2'):
            atualizarDados(clientes, cid, 'O seu email', 3, 3)
        elif (menu == '3'):
            atualizarUsuario(clientes, cid, 'O seu usuario', 3)
        elif (menu == '4'):
            atualizarSenha(clientes, cid, 'A sua senha', 6)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

##################################################################################################################################################################################

def minhasCompras(cid):
    if existeItem(compras, cid):
        while True:
            print(45 * '-')
            print(f'{CBLU}Lista de pedidos | {clientes[cid][2]}{CEND}')
            pedidos = retornaPedidos(cid)
            for chave in pedidos.keys():
                print(f'\nCod: {CGRE}{chave}{CEND}\nProdutos:', end='')
                for item in pedidos[chave]:
                    print(f' | {item[1]} - Un: {item[4]}', end='')
                print()
            print('\n[1] - Exibir detalhes\n[0] - Voltar ao menu anterior')
            opcao = str(input('\nDigite a opcao desejada: '))
            if (opcao == '1'):
                cod = str(input('Digite o código do pedido: '))
                if cod in pedidos.keys():
                    detalhaPedidos(cod,pedidos)
                    input('\nPressione ENTER para voltar o menu anterior.')
                else:
                    erro('Pedido não encontrado.')
            elif (opcao == '0'):
                break
            else:
                erro('Opção inválida.')
    else:
        erro('Você ainda não fez nenhuma compra.')
        return

def pesquisarProd(cid):
    while True:
        print(45 * '-')
        print(f'{CBLU}Tela de pesquisa de produtos | {clientes[cid][2]}{CEND}')
        print(f'\nPelo o que você deseja pesquisar?')
        print('\n[1] - Nome\n[2] - Descrição\n[0] - Voltar ao menu anterior')
        opcao = str(input('\nDigite a opcao desejada: '))
        if (opcao == '1'):
            resultPesquisaProd(1, 'no nome', cid)
        elif (opcao == '2'):
            resultPesquisaProd(3, 'na descrição', cid)
        elif (opcao == '0'):
            break
        else:
            erro('Opcao invalida.')

def resultPesquisaProd(campo, prompt, cid):
    codigos = list()
    busca = str(input(f'\nPesquisando {prompt}: ').lower())
    if (busca != ''):
        while True:
            achei = False
            for prod in produtos.values():
                for item in prod:
                    lowprod = item[campo].lower()
                    if (lowprod.find(busca) >= 0):
                        codigos.append(item[0])
                        if not achei:
                            print(f'\n{CYEL}O que encontramos com o termo "{busca}" {prompt}:{CEND}')
                            print(f'\nCódigo - Produto - Descrição')
                        print(f'{CGRE}{item[0]}{CEND} - {item[1]} - {item[3]}')
                        achei = True
            if achei:
                print('\n[1] - Exibir detalhes\n[0] - Voltar ao menu anterior')
                opcao = str(input('\nDigite a opcao desejada: '))
                if (opcao == '1'):
                    cod = str(input('Digite o código do produto: '))
                    if cod in codigos:
                        vid = selecionaID(cod)
                        exibirDetalhes(cid, cod, vid)
                    else:
                        erro('Produto não encontrado.')
                elif (opcao == '0'):
                    break
                else:
                    erro('Opção inválida.')
            else:
                erro(f'Nao tem nenhum produto com o termo "{busca}" {prompt}.')
                return
    else:
        erro(f'O campo de pesquisa não deve ficar em branco.')

def exibirDetalhes(cid, cod, vid):
    while True:
        print(45 * '-')
        print(f'{CBLU}Tela de detalhes do produto | {clientes[cid][2]}{CEND}')
        if detalheProduto(vid, cod):
            print('\n[1] - Comprar\n[2] - Adicionar ao carrinho\n[0] - Voltar ao menu anterior')
            opcao = str(input('\nDigite a opcao desejada: '))
            if (opcao == '1'):
                if comprarProduto(cid, cod, vid):
                    return
            elif (opcao == '2'):
                input('\nDOIS')
            elif (opcao == '0'):
                break
            else:
                erro('Opcao invalida.')
        else:
            erro('Esse produto está esgotado.')
            break

def comprarProduto(cid, cod, vid):
    while True:
        qtd = verInputNum('Digite a quantidade desejada: ',tipo='int')
        if (qtd != 'erro'):
            acao = manipulaEstoque(vid, cod, qtd, op='retira')
            if (acao == 'retirado'):
                finalizaPedido(cid)
                return True
            elif (acao == 'insuficiente'):
                erro('A quantidade em estoque é insuficiente para a quantidade informada.')
                break
        else:
            break

def finalizaPedido(cid):
    nid = novoIdCompra(cid)
    for chave1 in compras:
        if (chave1 == cid):
            compras[chave1].append({nid: []})
            for dicicionario1 in compras[chave1]:
                for chave2 in dicicionario1:
                    if (chave2 == nid):
                        for pedido in carrinho.values():
                            dicicionario1[chave2].append(pedido)
                        carrinho.clear()
                        break
            break
    aviso(f'Pedido código {nid} finalizado com com sucesso.')