from layouts import *


def existeVendedor(dadoInserido):
    for vid in vendedores:
        if (dadoInserido == vendedores[vid][0]):
            return vid

def existeDado(dadoInserido,bd):
    for xid in bd:
        if (dadoInserido == bd[xid][0]):
            return xid

def ultimoId(bd):
    ultimo = 0
    for xid in bd.keys():
        if xid > ultimo:
            ultimo = xid
    return ultimo

def cadastroBD(infos,novoId,bd1,bd2,bd3):
    bd1[novoId] = infos
    bd2[novoId] = []
    bd3[novoId] = 0

def attDadosBD(bd,usuario,dado,campo):
    bd[usuario][campo] = dado


vendedores = {1:['a','','Rogerio Brito','rogerio@mail.com'],2:['marcos','123456','Marcos Lira','marcos@mail.com']}

iniProd = {1:5,2:1}

produtos = {1:[['1001','Banana',6.23,'Dúzia banana nanica',15],['1002','Goiaba',0.96,'Goiaba orgânica especial',12],['1003','Laranja',1.06,'Laranja lima da Bahia',23],['1004','Abacaxi',5,'Abacaxi caramelo albino',8],['1005','Manga',1.30,'Manga rosa da aldeia Ibiriuproproene do Sul',22]],2:[['2001','Ovo',22.30,'Dúzia do ovo tamanho grande',3]]}

clientes = {1:['sa','','Samanta Biloba','samanta@mail.com'],2:['marcos','123456','Marcos Lira','marcos@mail.com']}

iniComp = {1:2,2:1}

compras = {
    1: [{'1sa1001': [['1001', 'Banana', 6.23, 'Banana Nanica', 1],['1002','Goiaba',0.96,'Goiaba da terra',3]]},
        {'1sa1002': [['1002','Goiaba',0.96,'Goiaba da terra',3]]}],
    2: [{'2ma2001': [['2001','Ovo',22.30,'Ovo tamanho grande',3]]}]
           }

maisPesquisados = [{'cod':'1001','nome':'Banana','qtd':3},{'cod':'1002','nome':'Goiaba','qtd':5},{'cod':'2001','nome':'Ovo','qtd':2}]

iniCar = [0]

carrinho = dict()
cartemp = dict()


def retornaPedidos(cid):
    pedidos = dict()
    achei = False
    for chave1 in compras:
        for dicionario1 in compras[chave1]:
            for chave2 in dicionario1:
                if chave1 == cid:
                    pedidos[chave2] = dicionario1[chave2]
                    achei = True
        if achei:
            return pedidos
            break

def detalhaPedidos(cod,pedidos):
    achei = False
    for chave in pedidos.keys():
        if (chave == cod):
            achei = True
            total = 0
            print(f'\nTotal de produtos: {len(pedidos[chave])}')
            for item in pedidos[chave]:
                print(f'\n{item[1]}')
                print(f'R$ {item[2]:.2f} | un. {item[4]}')
                print(f'Descrição: {item[3]}')
                parcial = item[2] * item[4]
                total += parcial
            print(f'\nTotal da compra: R$ {total:.2f}')
        if achei:
            break

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

def existeItem(bd, xid):
    if (len(bd[xid]) > 0):
        return True
    else:
        return False

def detalheProduto(vid, cod):
    for prod in produtos[vid]:
        if cod == prod[0]:
            print(f'\nCódigo: {CGRE}{prod[0]}{CEND}')
            print(f'Nome: {prod[1]}')
            print(f'Preço: R$ {prod[2]:.2f}')
            print(f'Descrição: {prod[3]}')
            print(f'Quantidade em estoque: {prod[4]}')
            if (prod[4] > 0):
                return True
            else:
                return False
            break

def manipulaEstoque(vid, cod, qtd, unico, op=''):
    for prod in produtos[vid]:
        if (cod == prod[0]):
            estoque = prod[4]
            if (op == 'retira'):
                resultado = estoque - qtd
                if (resultado >= 0):
                    prod[4] -= qtd
                    if (unico == 'sim'):
                        cartemp[0] = prod.copy()
                        cartemp[0][4] = qtd
                    elif (unico == 'nao'):
                        achei = False
                        for item in carrinho.values():
                            if (item[0] == cod):
                                achei = True
                                break
                        if achei:
                            item[4] += qtd
                        else:
                            iniCar[0] += 1
                            carrinho[iniCar[0]] = prod.copy()
                            carrinho[iniCar[0]][4] = qtd
                    return 'retirado'
                else:
                    return 'insuficiente'
            elif (op == 'devolve'):
                prod[4] += qtd
                return 'devolvido'
            break


def excluiProduto(vid, cod):
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
def novoIdCompra(cid):
    iniComp[cid] += 1
    for chave in clientes.keys():
        if (chave == cid):
            iniciais = ''
            nome = clientes[chave][0]
            for i in range(2):
                iniciais += nome[i]
            break
    idComp = f'{cid}' + f'{iniComp[cid]:03}'
    novoId = str(cid) + iniciais + idComp
    return novoId

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
        cid = existeDado(usuario, clientes)
        if (cid != None) and (clientes[cid][1] == senha):
            return cid
        else:
            erro('Usuario ou senha inválidos.')

def atualizarDados(bd,xid,prompt1,tamanho,campo):
    infoAtual = (f'\n{prompt1} atual eh: {bd[xid][campo]}')
    dado = verInputStr(tamanho,'Digite o novo: ',prompt1,prompt3=infoAtual)
    if (dado != False):
        attDadosBD(bd, xid, dado, campo)
        aviso(f'{prompt1} foi atualizado com sucesso para {bd[xid][campo]}')

def atualizarUsuario(bd,xid,prompt1,tamanho):
    while True:
        infoAtual = (f'\n{prompt1} atual eh: {bd[xid][0]}')
        usuario = verInputStr(tamanho, 'Digite o novo: ', prompt1, prompt3=infoAtual)
        existe = existeVendedor(usuario)
        if (existe != None):
            if (usuario == bd[xid][0]):
                break
            print(f'{CRED}\nErro! esse usuario ja esta em uso.{CEND}')
            if not tentarNovamente():
                return
        else:
            break
    if (usuario != False):
        attDadosBD(bd, xid, usuario, 0)
        aviso(f'Usuario atualizado com sucesso para {usuario}')

def atualizarSenha(bd, xid, prompt1, tamanho):
    senhaantiga = str(input('\nDigite a senha antiga: '))
    if (senhaantiga != bd[xid][1]):
        erro('A senha digitada esta errada!')
    else:
        senha = verInputStr(tamanho, 'Digite a nova: ', prompt1)
        if (senha != False):
            attDadosBD(bd, xid, senha, 1)
            aviso(f'Senha atualizada com sucesso.')