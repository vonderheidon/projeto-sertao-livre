from layouts import *
from bd import *

def menuCliente(texto):
    while True:
        menu = layMsec(texto)
        if (menu == '1'):
            cadastrarUsuario('cliente')
        elif (menu == '2'):
            vid = entrar('cliente')
            if (vid != None):
                menuPrincipal(vid)
                break
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def menuPrincipal(vid):
    while True:
        texto = ('\n[1] - Meu perfil\n[2] - Minhas Compras\n[3] - Pesquisar produtos\n[0] - Sair da conta')
        menu = layMPrincipal(clientes, vid, texto)
        if (menu == '1'):
            meuPerfil(vid)
        elif (menu == '2'):
            minhasCompras(vid)
        elif (menu == '3'):
            pesquisarProd(vid)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def meuPerfil(vid):
    while True:
        menu = layMmperf(clientes, vid)
        if (menu == '1'):
            atualizarInfoPessoais(vid)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def atualizarInfoPessoais(vid):
    while True:
        menu = layAttinf(clientes, vid)
        if (menu == '1'):
            atualizarDados(clientes, vid, 'O seu nome completo', 3, 2)
        elif (menu == '2'):
            atualizarDados(clientes, vid, 'O seu email', 3, 3)
        elif (menu == '3'):
            atualizarUsuario(clientes, vid, 'O seu usuario', 3)
        elif (menu == '4'):
            atualizarSenha(clientes, vid, 'A sua senha', 6)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

##################################################################################################################################################################################

def minhasCompras(vid):
    if existeItem(compras,vid):
        while True:
            print(45 * '-')
            print(f'{CBLU}Lista de pedidos | {clientes[vid][2]}{CEND}')
            pedidos = retornaPedidos(vid)
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

def pesquisarProd(vid):
    while True:
        print(45 * '-')
        print(f'{CBLU}Tela de pesquisa de produtos | {clientes[vid][2]}{CEND}')
        print(f'\nPelo o que você deseja pesquisar?')
        print('\n[1] - Nome\n[2] - Descrição\n[0] - Voltar ao menu anterior')
        opcao = str(input('\nDigite a opcao desejada: '))
        if (opcao == '1'):
            pesquisaProd(1, 'no nome')
        elif (opcao == '2'):
            pesquisaProd(3, 'na descrição')
        elif (opcao == '0'):
            break
        else:
            erro('Opcao invalida.')

def pesquisaProd(campo, prompt):
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
                        exibirDetalhes(vid,cod)
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

def listarProdutos():
    print(f'\n{produtos}\n')
    for prod in produtos.values():
        for item in prod:
            print(f'\nNome: {item[1]}')
            print(f'Preço: {item[2]}')
            if (item[4] > 0):
                print(f'Quantidade em estoque: {item[4]}')
            else:
                print('Produto esgotado!')

def exibirDetalhes(vid, cod):
    while True:
        print(45 * '-')
        print(f'{CBLU}Tela de detalhes do produto | {clientes[vid][2]}{CEND}')
        if detalheProduto(vid, cod):
            print('\n[1] - Comprar\n[2] - Adicionar ao carrinho\n[0] - Voltar ao menu anterior')
            opcao = str(input('\nDigite a opcao desejada: '))
            if (opcao == '1'):
                input('\nUM')
            elif (opcao == '2'):
                input('\nDOIS')
            elif (opcao == '0'):
                break
            else:
                erro('Opcao invalida.')
        else:
            erro('Esse produto está esgotado.')
            break