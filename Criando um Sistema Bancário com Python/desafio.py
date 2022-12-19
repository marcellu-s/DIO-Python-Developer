from modulos import *
from os import system


conta = {'saldo': 0, 'extrato': []}
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    system('cls')

    opcao = menu('BANCO DIO', ['Depositar', 'Sacar', 'Extrato', 'Sair'])
    
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
            print(colors('\nVOLTE SEMPRE...\n', 'green'))
            break

    system('pause')
