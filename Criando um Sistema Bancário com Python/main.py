from modulos import *
from os import system


conta = {'saldo': 0, 'extrato': []}
usuarios = {}
registro_contas = []
numero_saque = 0
num_conta = 1
LIMITE_SAQUE = 3
AGENCIA = '0001'

while True:

    system('cls')

    opcao = menu('BANCO DIO', ['Depositar', 'Sacar', 'Extrato',
                 'Criar conta', 'Listar contas', 'Novo usuário', 'Sair'])

    system('cls')

    match opcao:
        case 1:
            conta = depositar(conta)
        case 2:

            if numero_saque != LIMITE_SAQUE:
                conta = sacar(conta)
                numero_saque += 1
            else:
                print(colors('LIMITE DE SAQUE ATINGIDO', 'purple'))
        case 3:
            extrato(conta)
        case 4:
            registro_contas.append(criar_conta(usuarios, AGENCIA, num_conta))
            num_conta += 1
        case 5:
            listar_contas(usuarios, registro_contas)
        case 6:
            usuarios = criar_usuario(usuarios)
        case 7:
            print(colors('\nVOLTE SEMPRE...\n', 'green'))
            break

    system('pause')
