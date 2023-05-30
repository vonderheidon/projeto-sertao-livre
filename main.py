from layouts import *
from vendedores import *
from clientes import *

while True:
    menu = layMini()
    if (menu == '1'):
        menuVendedor('## Menu vendedor ##')
    elif (menu == '2'):
        menuCliente('## Menu Cliente ##')
    elif (menu == '0'):
        break
    else:
        erro('Opcao invalida.')