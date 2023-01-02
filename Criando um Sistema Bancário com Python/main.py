from modulos import *
from os import system


registros_usuario = {}
registros_contas = {}

while True:

    system('cls')

    opcao = menu('BANCO DIO', ['Depositar', 'Sacar', 'Extrato',
                 'Criar conta', 'Listar contas', 'Novo usuário', 'Sair'])

    system('cls')

    retorno = False

    match opcao:
        case 1:
            deposito(registros_usuario, registros_contas)
        case 2:
            saque(registros_usuario, registros_contas)
        case 3:
            extrato(registros_usuario, registros_contas) 
        case 4:
            retorno = create_new_account(registros_usuario, registros_contas)
            if retorno:
                registros_contas = retorno
            else:
                pass
        case 5:
            listar_contas(registros_contas) 
        case 6:
            retorno = criar_usuario(registros_usuario)
            if retorno:
                registros_usuario = retorno
            else:
                pass
        case 7:
            break

    system('pause')
