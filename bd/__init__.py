from layouts import *


def existeVendedor(dadoInserido):
    for vid in vendedores:
        if (dadoInserido == vendedores[vid][0]):
            return vid

def existeDado(dadoInserido,bd):
    for vid in bd:
        if (dadoInserido == bd[vid][0]):
            return vid

def ultimoId(bd):
    ultimo = 0
    for vid in bd.keys():
        if vid > ultimo:
            ultimo = vid
    return ultimo

def cadastroBD(infos,novoId,bd1,bd2,bd3):
    bd1[novoId] = infos
    bd2[novoId] = []
    bd3[novoId] = 0

def attDadosBD(bd,usuario,dado,campo):
    bd[usuario][campo] = dado


vendedores = {1:['a','','Rogerio Brito','rogerio@mail.com'],2:['marcos','123456','Marcos Lira','marcos@mail.com']}

iniProd = {1:2,2:1}

produtos = {1:[['1001','Banana',0.48,'Banana Nanica',5],['1002','Goiaba',0.96,'Goiaba da terra',12]],2:[['2001','Ovo',22.30,'Ovo tamanho grande',0]]}

clientes = {1:['s','','Samanta Biloba','samanta@mail.com'],2:['marcos','123456','Marcos Lira','marcos@mail.com']}

iniComp = {1:3,2:1}

compras = {
    1:[{'sam1001':[['banana',5],['uva',3]]},{'sam1002':[['Limão',2]]},{'sam1003':[['Lapis',2],['Borracha',1],['Caneta',3],['Caderno',4]]}],
    2:[{'mar1001':[['Goiaba',4],['uva',1],['Laranja',6]]}]
           }


def selecionaID(cod):
    achei = False
    for prod in produtos:
        for item in produtos[prod]:
            if (item[0] == cod):
                achei = True
                break
        if achei:
            break
    return prod

def existeItem(bd, vid):
    if (len(bd[vid]) > 0):
        return True
    else:
        return False

def detalheProduto(vid,cod):
    for prod in produtos[vid]:
        if cod == prod[0]:
            print(f'\nCódigo: {prod[0]}')
            print(f'Nome: {prod[1]}')
            print(f'Preço: R$ {prod[2]:.2f}')
            print(f'Descrição: {prod[3]}')
            print(f'Quantidade em estoque: {prod[4]}')
            if (prod[4] > 0):
                return True
            else:
                return False

def excluiProduto(vid,cod):
    for prod in produtos[vid]:
        if cod == prod[0]:
            produtos[vid].remove(prod)
            break

def attProduto(vid,cod,dados):
    for prod in produtos[vid]:
        if cod == prod[0]:
            prod[1:4] = dados
            break

def cadastrarUsuario(op):
    print(51 * '-')
    print(f'{CBLU}Complete os dados para criar sua conta de {op}!{CEND}')
    while True:
        usuario = verInputStr(3, '\nUsuario: ', 'O seu usuario')
        if (op == 'vendedor'):
            existe = existeDado(usuario,vendedores)
        elif (op == 'cliente'):
            existe = existeDado(usuario,clientes)
        if (existe != None):
            print(f'{CRED}\nErro! esse usuario ja esta em uso.{CEND}')
            if not tentarNovamente():
                return
        else:
            break
    if (usuario != False):
        senha = verInputStr(6, 'Senha: ', 'A sua senha')
        if (senha != False):
            nome = verInputStr(3, 'Nome completo: ', 'O seu nome')
            if (nome != False):
                email = verInputStr(3, 'E-mail: ', 'O seu email')
                if (email != False):
                    infos = [usuario, senha, nome, email]
                    if (op == 'vendedor'):
                        novoId = ultimoId(vendedores) + 1
                        cadastroBD(infos, novoId, vendedores, produtos, iniProd)
                    elif (op == 'cliente'):
                        novoId = ultimoId(clientes) + 1
                        cadastroBD(infos, novoId, clientes, compras, iniComp)
                    aviso(f'Cadastro de {op} efetuado com sucesso!')

def entrar(op):
    print(39 * '-')
    print(f'{CBLU}Tela de login - {op} | Sertao Livre\n{CEND}')
    usuario = str(input('Nome de usuario: '))
    senha = str(input('Senha: '))
    if (op == 'vendedor'):
        vid = existeDado(usuario, vendedores)
        if (vid != None) and (vendedores[vid][1] == senha):
            return vid
        else:
            erro('Usuario ou senha inválidos.')
    elif (op == 'cliente'):
        vid = existeDado(usuario, clientes)
        if (vid != None) and (clientes[vid][1] == senha):
            return vid
        else:
            erro('Usuario ou senha inválidos.')

def atualizarDados(bd,vid,prompt1,tamanho,campo):
    infoAtual = (f'\n{prompt1} atual eh: {bd[vid][campo]}')
    dado = verInputStr(tamanho,'Digite o novo: ',prompt1,prompt3=infoAtual)
    if (dado != False):
        attDadosBD(bd, vid, dado, campo)
        aviso(f'{prompt1} foi atualizado com sucesso para {bd[vid][campo]}')

def atualizarUsuario(bd,vid,prompt1,tamanho):
    while True:
        infoAtual = (f'\n{prompt1} atual eh: {bd[vid][0]}')
        usuario = verInputStr(tamanho, 'Digite o novo: ', prompt1, prompt3=infoAtual)
        existe = existeVendedor(usuario)
        if (existe != None):
            if (usuario == bd[vid][0]):
                break
            print(f'{CRED}\nErro! esse usuario ja esta em uso.{CEND}')
            if not tentarNovamente():
                return
        else:
            break
    if (usuario != False):
        attDadosBD(bd,vid,usuario,0)
        aviso(f'Usuario atualizado com sucesso para {usuario}')

def atualizarSenha(bd, vid, prompt1, tamanho):
    senhaantiga = str(input('\nDigite a senha antiga: '))
    if (senhaantiga != bd[vid][1]):
        erro('A senha digitada esta errada!')
    else:
        senha = verInputStr(tamanho, 'Digite a nova: ', prompt1)
        if (senha != False):
            attDadosBD(bd, vid, senha, 1)
            aviso(f'Senha atualizada com sucesso.')