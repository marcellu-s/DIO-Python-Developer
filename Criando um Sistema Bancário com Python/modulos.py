from time import sleep
from os import system
from datetime import datetime


def colors(text, cor):  # FUNÇÃO PARA ATRIBUIR COR EM TEXTOS
    match cor:
        case 'red':
            return (f'\033[1;31m{text}\033[m')
        case 'green':
            return (f'\033[1;32m{text}\033[m')
        case 'yellow':
            return (f'\033[1;33m{text}\033[m')
        case 'blue':
            return (f'\033[1;34m{text}\033[m')
        case 'purple':
            return (f'\033[1;35m{text}\033[m')
        case 'gray':
            return (f'\033[1;37m{text}\033[m')


def leiafloat(msg):  # FUNÇÃO PARA LER UM VALOR FLOAT
    while True:
        try:
            valor = float(input(msg))
        except:
            print('\n\033[1;31mERRO: Digite um valor válido.\033[m\n')
            continue
        return valor


def leiaint(msg):  # FUNÇÃO PARA LER UM VALOR INTEIRO
    while True:
        try:
            valor = int(input(msg))
        except:
            print('\n\033[1;31mERRO: Digite um valor válido.\033[m\n')
            continue
        return valor


def menu(title, lista):

    print('='*50)
    print(f'{title:^50}')
    print('='*50)

    for pos, c in enumerate(lista):
        print(f'{pos+1} - {c}')
    print('='*50)

    while True:
        try:
            op = int(input('\033[1;35mSua opção: \033[m'))
        except:
            print('\033[1;31mERRO: valor inválido!\033[m')
            continue

        if 1 <= op <= 4:
            return op
        else:
            print('\033[1;31mERRO: seleção inválida!\033[m')


def depositar(conta):
    print(f'SALDO ATUAL: R$ {conta["saldo"]}\n')

    while True:
        valor_deposito = leiafloat('Informe o valor a ser depositado: R$ ')

        if valor_deposito <= 0:
            print(colors('ERRO: Informe um valor válido', 'red'))
            continue
        else:
            print(f'Realizando depósito, aguarde...')
            sleep(1.5)
            system('cls')
            print(f'SALDO ANTIGO: R$ {conta["saldo"]}\n')
            conta['saldo'] += valor_deposito
            conta['extrato'].append({'DEPÓSITO':(datetime.now().strftime('%d-%m-%Y as %H:%M:%S'), valor_deposito)})
            print(colors(f'Depósito de R$ {valor_deposito} realizado com sucesso', 'green'))
            print(f'\nNOVO SALDO: R$ {conta["saldo"]}')
            return conta
        

def sacar(conta):


    while True:

        print(f'SALDO ATUAL: R${conta["saldo"]}\n')

        valor_saque = leiafloat('Informe o valor de saque: R$ ')

        if 1 <= valor_saque <= 500:
            pass
        elif valor_saque > 500:
            print(colors('\nValor limite de R$ 500 excedido.', 'yellow'))
            sleep(1.5)
            system('cls')
            continue
        else:
            print(colors('ERRO: valor inválido.', 'red'))
            continue

        if valor_saque > conta['saldo']:
            print(
                colors(f'ERRO: Não foi possível realizar o saque de R$ {valor_saque}, pois o seu saldo é de R$ {conta["saldo"]}', 'red'))
            resp = input('Deseja finalizar a operação? [S/N]: ').upper()
            if resp == 'S':
                return conta
            elif resp == 'N':
                system('cls')
                continue
            else:
                print(colors('ERRO: Tente novamente.', 'red'))
        else:
            print('Realizando a operação, aguarde...')
            sleep(1.5)
            system('cls')
            print(f'SALDO ANTIGO: R${conta["saldo"]}\n')
            conta['saldo'] -= valor_saque
            print(colors(f'Saque de R$ {valor_saque} realizado com sucesso.', 'green'))
            print(f'\nNOVO SALDO: R$ {conta["saldo"]}')
            conta['extrato'].append({'SAQUE': (datetime.now().strftime('%d-%m-%Y as %H:%M:%S'), valor_saque)})
            return conta


def extrato(conta):

    print(f'SALDO ATUAL: R$ {conta["saldo"]}\n')
    print('='*45)
    print('EXTRATO'.center(45))
    print('='*45)
    for valor in conta['extrato']:
        for tipo, extrato in valor.items():
            print(f'{tipo} - {colors(f"R$ {extrato[1]}", "red")} em {extrato[0]}' if tipo == 'SAQUE' else f'{tipo} - {colors(f"R$ {extrato[1]}", "green")} em {extrato[0]}')
