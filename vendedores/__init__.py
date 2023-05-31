from layouts import *
from bd import *

def menuVendedor(texto):
    while True:
        menu = layMsec(texto)
        if (menu == '1'):
            cadastrarUsuario('vendedor')
        elif (menu == '2'):
            vid = entrar('vendedor')
            if (vid != None):
                menuPrincipal(vid)
                break
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def menuPrincipal(vid):
    while True:
        texto = ('\n[1] - Meu perfil\n[2] - Meus produtos\n[0] - Sair da conta')
        menu = layMPrincipal(vendedores, vid, texto)
        if (menu == '1'):
            meuPerfil(vid)
        elif (menu == '2'):
            meusProdutos(vid)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def meuPerfil(vid):
    while True:
        menu = layMmperf(vendedores, vid)
        if (menu == '1'):
            atualizarInfoPessoais(vid)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def atualizarInfoPessoais(vid):
    while True:
        menu = layAttinf(vendedores, vid)
        if (menu == '1'):
            atualizarDados(vendedores, vid, 'O seu nome completo', 3, 2)
        elif (menu == '2'):
            atualizarDados(vendedores, vid, 'O seu email', 3, 3)
        elif (menu == '3'):
            atualizarUsuario(vendedores, vid, 'O seu usuario', 3)
        elif (menu == '4'):
            atualizarSenha(vendedores, vid, 'A sua senha', 6)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

##################################################################################################################################################################################

def meusProdutos(vid):
    while True:
        menu = layMmprod(vendedores,vid)
        if (menu == '1'):
            listarProdutos(vid)
        elif (menu == '2'):
            manipulaProduto(vid,opcao='cadastrar')
        elif (menu == '3'):
            pesquisarProduto(vid)
        elif (menu == '0'):
            break
        else:
            erro('Opcao invalida.')

def listarProdutos(vid):
    while True:
        if existeItem(produtos, vid):
            codigos = list()
            print(45 * '-')
            print(f'{CBLU}Tela produtos cadastrados | {vendedores[vid][2]}{CEND}')
            print(f'\nCódigo - Produto')
            for item in produtos[vid]:
                codigos.append(item[0])
                print(f'{CGRE}{ item[0]}{CEND} - {item[1]}')
            print('\n[1] - Exibir detalhes\n[0] - Voltar ao menu anterior')
            opcao = str(input('\nDigite a opcao desejada: '))
            if (opcao == '1'):
                cod = str(input('Digite o código do produto: '))
                if cod in codigos:
                    exibirDetalhes(vid, cod)
                    if not existeItem(produtos, vid):
                        break
                else:
                    erro('Produto não encontrado.')
            elif (opcao == '0'):
                break
            else:
                erro('Opção inválida.')
        else:
            erro('Você ainda não tem nenhum produto cadastrado.')
            return

def manipulaProduto(vid,cod='',opcao=''):
    if (opcao == 'cadastrar'):
        print(45 * '-')
        print(f'{CBLU}Tela de cadastro de produto | {vendedores[vid][2]}{CEND}')
    elif (opcao == 'atualizar'):
        print(f'\n{CBLU}Digite os novos valores para o produto selecionado.{CEND}')
    nome = verInputStr(3, '\nNome: ', 'O nome do produto')
    if (nome != False):
        preco = verInputNum('Preço: R$ ',tipo='float')
        if (preco != 'erro'):
            descricao = verInputStr(3, 'Descrição: ', 'O campo descrição')
            if (descricao != 'erro'):
                quantidade = verInputNum('Quantidade: ',tipo='int')
                if (quantidade != 'erro'):
                    if (opcao == 'cadastrar'):
                        iniProd[vid] += 1
                        idProd = f'{vid}' + f'{iniProd[vid]:03}'
                        produtos[vid].append([idProd, nome, preco, descricao, quantidade])
                        aviso('Produto cadastrado com sucesso.')
                    elif (opcao == 'atualizar'):
                        dados = [nome,preco,descricao,quantidade]
                        attProduto(vid,cod,dados)
                        aviso('Produto atualizado com sucesso.')

def exibirDetalhes(vid, cod):
    while True:
        print(45 * '-')
        print(f'{CBLU}Tela de detalhes do produto | {vendedores[vid][2]}{CEND}')
        detalheProduto(vid, cod)
        print('\n[1] - Editar\n[2] - Excluir\n[0] - Voltar ao menu anterior')
        opcao = str(input('\nDigite a opcao desejada: '))
        if (opcao == '1'):
            manipulaProduto(vid, cod=cod, opcao='atualizar')
        elif (opcao == '2'):
            if excluirProduto(vid,cod):
                break
        elif (opcao == '0'):
            break
        else:
            erro('Opcao invalida.')

def excluirProduto(vid, cod):
    confirma = input('\nVoce realmente deseja excluir o produto selecionado? [S/N]: ').upper()
    if (confirma == 'S'):
        excluiProduto(vid, cod)
        aviso('Produto excluido com sucesso.')
        return True
    elif (confirma == 'N'):
        return False
    else:
        erro('Opção inválida.')

def pesquisarProduto(vid):
    while True:
        if existeItem(produtos, vid):
            print(45 * '-')
            print(f'{CBLU}Tela de pesquisa de produtos | {vendedores[vid][2]}{CEND}')
            print(f'\nPelo o que você deseja pesquisar?')
            print('\n[1] - Nome\n[2] - Descrição\n[0] - Voltar ao menu anterior')
            opcao = str(input('\nDigite a opcao desejada: '))
            if (opcao == '1'):
                pesquisaProd(vid, 1, 'no nome')
                if not existeItem(produtos, vid):
                    break
            elif (opcao == '2'):
                pesquisaProd(vid, 3, 'na descrição')
                if not existeItem(produtos, vid):
                    break
            elif (opcao == '0'):
                break
            else:
                erro('Opcao invalida.')
        else:
            erro('Você não tem nenhum produto cadastrado ainda.')
            return

def pesquisaProd(vid, campo, prompt):
    codigos = list()
    busca = str(input(f'\nPesquisando {prompt}: ').lower())
    if (busca != ''):
        while True:
            achei = False
            for item in produtos[vid]:
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
                        exibirDetalhes(vid, cod)
                        if not existeItem(produtos, vid):
                            return
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