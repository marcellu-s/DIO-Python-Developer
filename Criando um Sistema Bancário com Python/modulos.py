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
            sleep(3)
            system('cls')
            print(f'SALDO ANTIGO: R$ {conta["saldo"]}\n')
            conta['saldo'] += valor_deposito
            conta['valor_depositado'].append([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), valor_deposito])
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
            print(colors('Seu limite de saque é de até 500.', 'yellow'))
            continue
        else:
            print(colors('ERRO: valor inválido.', 'red'))
            continue

        if valor_saque > conta['saldo']:
            print(
                colors(f'ERRO: Não foi possível realizar o saque, seu saldo é de R$ {conta["saldo"]}', 'red'))
            resp = input('Deseja finalizar a operação? [S/N]: ').upper()
            if resp == 'S':
                return conta
            elif resp == 'N':
                continue
            else:
                print(colors('ERRO: Tente novamente.', 'red'))
        else:
            print('Realizando a operação, aguarde...')
            sleep(3)
            system('cls')
            print(f'SALDO ANTIGO: R${conta["saldo"]}\n')
            conta['saldo'] -= valor_saque
            print(colors(f'Saque de R$ {valor_saque} realizado com sucesso.', 'green'))
            print(f'\nNOVO SALDO: R$ {conta["saldo"]}')
            conta['valor_sacado'].append([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), valor_saque])
            return conta


def extrato(conta):
    while True:

        system('cls')
        print(f'SALDO ATUAL: R$ {conta["saldo"]}\n')
        opcao = menu('EXTRATO', ['Histórico de Depósito', 'Histórico de Saque', 'Sair'])
        print()
        match opcao:
            case 1:

                if len(conta['valor_depositado']) == 0:
                    print('SEM REGISTRO')
                else:
                    for valor in (conta['valor_depositado']):   
                        print(f'[{valor[0]}] - R$ {colors(valor[1], "green")}')
                system('pause')
            case 2:
                if len(conta['valor_sacado']) == 0:
                    print('SEM REGISTRO')
                else:
                    for valor in (conta['valor_sacado']):
                        
                        print(f'[{valor[0]}]- R$ {colors(valor[1], "green")}')
                system('pause')
            case 3:
                break
            case 4:
                break
