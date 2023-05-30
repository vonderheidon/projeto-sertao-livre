CRED = '\33[91m'
CYEL = '\33[93m'
CEND = '\33[0m'
CBLU = '\33[34m'
CGRE = '\33[92m'


def layMini():
    print(f'\n{CYEL}{25 * "*"}')
    print('Bem vindo ao Sertao Livre')
    print(f'{25 * "*"}{CEND}')
    print('\n- Menu Inicial')
    print('\n[1] - Vendedor\n[2] - Cliente\n[0] - Sair')
    opcao = str(input('\nDigite a opcao desejada: '))
    return opcao

def layMsec(texto):
    print(f'\n{CBLU}{texto}{CEND}')
    print('\n[1] - Cadastrar-se\n[2] - Entrar\n[0] - Voltar ao menu inicial')
    opcao = str(input('\nDigite a opcao desejada: '))
    return opcao

def layMPrincipal(bd,vid,texto):
    print(f'{CGRE}\nSeja Bem vindo, {bd[vid][2]}.{CEND}')
    print(texto)
    opcao = str(input('\nDigite a opcao desejada: '))
    return opcao

def layMmperf(bd,vid):
    print(45 * '-')
    print(f'{CBLU}Tela de perfil | {bd[vid][2]}{CEND}')
    print(f'\nNome completo: {bd[vid][2]}')
    print(f'E-mail: {bd[vid][3]}')
    print(f'Usuario: {bd[vid][0]}')
    print('\n[1] - Atualizar informacoes pessoais\n[0] - Para voltar ao menu anterior')
    opcao = str(input('\nDigite a opcao desejada: '))
    return opcao

def layAttinf(bd,vid):
    print(60 * '-')
    print(f'{CBLU}Tela de atualizacao de informacoes pessoais | {bd[vid][2]}{CEND}')
    print('\n[1] - Nome completo\n[2] - E-mail\n[3] - Usuario\n[4] - Senha\n[0] - Para voltar ao menu anterior')
    opcao = str(input('\nDigite a opcao desejada: '))
    return opcao

def layMmprod(vendedores,vid):
    print(45 * '-')
    print(f'{CBLU}Tela de produtos | {vendedores[vid][2]}{CEND}')
    print('\n[1] - Listar todos cadastrados\n[2] - Cadastrar um novo\n[3] - Buscar\n[0] - Para voltar ao menu anterior')
    opcao = str(input('\nDigite a opcao desejada: '))
    return opcao

def erro(texto):
    print(f'\n{CRED}{texto}{CEND}')
    input('\nAperte ENTER para continuar...')

def aviso(texto):
    print(f'\n{CYEL}{texto}{CEND}')
    input('\nAperte ENTER para continuar...')

def tentarNovamente():
    while True:
        opcao = str(input('\nDeseja tentar novamente? [S/N]: ')).upper()
        if (opcao == 'S'):
            return True
        elif (opcao == 'N'):
            return False
        else:
            print(f'\n{CRED}Opcao invalida.{CEND}')

def verInputStr(tamanho,prompt1,prompt2,prompt3=''):
    while True:
        if (prompt3 != ''):
            print(prompt3)
        dados = str(input(prompt1))
        if (len(dados.strip()) >= tamanho):
            return dados
        else:
            print(f'{CRED}\nErro! {prompt2} deve ter pelo menos {tamanho} caracteres.{CEND}')
            if not tentarNovamente():
                return False

def verInputNum(prompt1,tipo=''):
    while True:
        try:
            if (tipo == 'int'):
                numero = int(input(prompt1))
            elif (tipo == 'float'):
                numero = float(input(prompt1))
            return numero
        except:
            print(f'{CRED}\nErro! O valor digitado é inválido.{CEND}')
            if not tentarNovamente():
                return 'erro'