from modulos import *
from os import system


conta = {'saldo': 0, 'valor_sacado': [], 'valor_depositado': []}
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    system('cls')

    opcao = menu('BANCO DIO', ['Depositar', 'Sacar', 'Extrato', 'Sair'])

    match opcao:
        case 1:
            system('cls')
            conta = depositar(conta)
            system('pause')
        case 2:
            system('cls')
            if numero_saque != LIMITE_SAQUE:
                conta = sacar(conta)
                numero_saque += 1
            else:
                print(colors('LIMITE DE SAQUE ATINGIDO', 'purple'))
            system('pause')
        case 3:
            extrato(conta)
        case 4:
            print(colors('\nVOLTE SEMPRE...\n', 'green'))
            break
