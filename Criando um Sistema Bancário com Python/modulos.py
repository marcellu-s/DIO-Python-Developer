from classes import *
from re import search
from datetime import date, datetime
from time import sleep
from os import system


def colors(text, cor):
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
        case _:
            return (f'{text}')


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except:
            print('\n\033[1;31mERRO: Digite um valor válido.\033[m\n')
            continue
        return valor


def leiaint(msg):
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

        if 1 <= op <= 7:
            return op
        else:
            print('\033[1;31mERRO: seleção inválida!\033[m')


def filtrar_usuario(registros, cpf):
    if registros.get(cpf) == None:
        return False
    else:
        return True



def criar_usuario(registros):
    while True:
        cpf = str(input(('Informe seu CPF: ')))
        if search('^[0-9]{11}$', cpf):
            if filtrar_usuario(registros, cpf):
                print(colors('\nUsuário já cadastrado.\n', 'yellow'))
                return False
            else:
                break
        else:
            print(colors('CPF inválido, digite novamente.', 'red'))
            continue 
    print()
    while True:
        nome = str(input('Informe seu nome e sobrenome: ')).strip()
        if search('[0-9]', nome):
            print(colors('Nome inválido.', 'red'))
            continue
        else:
            break
    print()
    while True:
        idade = str(input('Informe sua data de nascimento [DD/MM/AAAA]: ')).strip()
        if search('^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/[12][0-9]{3}$', idade):
            idade = date.today().year - int(idade[6:])
            break
        else:
            print(colors('Data inválida.', 'red'))
            continue
    print('\nCriando...\n')
    sleep(1.5)
    new_client = Cliente(cpf, nome, idade)
    registros.setdefault(cpf, new_client)
    print(colors('Usuário criado com sucesso.', 'green'))
    return registros


def create_new_account(registros_user, registros_account):
    while True:
        cpf = input('Digite seu CPF: ')
        if search('^[0-9]{11}$', cpf):
            if filtrar_usuario(registros_user, cpf):
                qnta_registros = 1 if len(registros_account) == 0 else len(registros_account) + 1
                new_account = Conta.criar_conta(registros_user.get(cpf).nome, qnta_registros, registros_user.get(cpf).cpf)
                registros_account.setdefault(qnta_registros, new_account)
                print(colors("\n=== Conta criada com sucesso! ===", 'green'))
                print(f"""Titular: \t{registros_user.get(cpf).nome}\nAgência: \t0001\nNúm. Conta: \t{qnta_registros}""")
                return registros_account
            else:
                print(colors('\nUsuário não encontrado.\n', 'yellow'))
                return False
        else:
            print(colors('\nERRO: CPF inválido.\n', 'red'))
            continue


def listar_contas(registros):
    if len(registros) > 0:
        print('='*40)
        print('CONTAS REGISTRADAS'.center(40))
        for conta in registros.values():
            print('='*40)
            print(f'Titular: \t{conta.usuario}\nAgência: \t{conta.agencia}\nNúm. Conta: \t{conta.num_conta}')
    else:
        print(colors('Nenhuma conta foi encontrada.\n', 'yellow'))


def filtrar_contas(registros_contas, num_conta):
    if registros_contas.get(num_conta) == None:
        return False 
    else:
        return True


def check(registros_users, registros_contas):
    num_conta = leiaint('Informe o número da conta: ')
    while True:
        cpf = str(input('Informe seu CPF: ')).strip()
        if search('^[0-9]{11}$', cpf):
            if filtrar_usuario(registros_users, cpf):
                if not filtrar_contas(registros_contas, num_conta):
                    print(colors('\nConta não encontrada.\n', 'yellow'))
                    return False
                else:
                    conta = registros_contas[num_conta]
                    if conta.cpf == cpf:
                        system('cls')
                        return conta
                    else:
                        print(colors('\nNúmero da conta ou CPF incorreto.\n', 'yellow'))
                        return False
            else:
                print(colors('\nUsuário não encontrado.\n', 'yellow'))
                return False
        else:
            print(colors('\nERRO: CPF inválido.\n', 'red'))
            continue


def deposito(registros_users, registros_contas):
    conta = check(registros_users, registros_contas)
    if not conta:
        return False
    else:
        print(f'SALDO ATUAL: R$ {conta.saldo}\n')
        print(colors('Digite "0" para finalizar a operação.\n', 'yellow'))
        while True:
            valor_deposito = leiafloat('Informe o valor a ser depositado: R$ ')
            if valor_deposito < 0:
                print(colors('ERRO: Informe um valor válido', 'red'))
                continue
            elif valor_deposito == 0:
                return False
            else:
                print(f'Realizando depósito, aguarde...')
                sleep(1)
                conta.depositar(conta, valor_deposito)
                system('cls')
                print(colors(f'Depósito de R$ {valor_deposito}, realizado com sucesso.', 'green'))
                conta.transacao(conta, 'DEPÓSITO', valor_deposito, datetime.now().strftime('%d-%m-%Y as %H:%M:%S'))
                print(f'\nSALDO ATUAL: R$ {conta.saldo}')
                return True


def extrato(registros_users, registros_contas):
    conta = check(registros_users, registros_contas)
    if not conta:
        return False
    else:
        print(f'SALDO ATUAL: R$ {conta.saldo}\n')
        if conta.len_extrato(conta):
            print('='*54)
            print('EXTRATO'.center(54))
            print('='*54)
            for transacao in conta.extrato:
                print(f'{transacao["Tipo"]} \t+ R$ {transacao["Valor"]} \t{transacao["Horario"]}\n' 
                    if transacao["Tipo"] == 'DEPÓSITO' else f'{transacao["Tipo"]} \t\t- R$ {transacao["Valor"]} \t{transacao["Horario"]}\n')
            return True
        else:
            print(colors('Sem registro de movimentação na conta.\n', 'yellow'))
            return False


def saque_check(conta, sacar=False):
    if conta.qnta_limite_de_saque(conta, sacar):
        return True 
    else:
        return False


def saque(registros_users, registros_contas):
    conta = check(registros_users, registros_contas)
    if not conta:
        return False 
    else:
        if saque_check(conta):
            print(f'SALDO ATUAL: R$ {conta.saldo}\n')
            print(colors('Digite "0" para finalizar a operação.\n', 'yellow'))
            while True:
                valor_saque = leiafloat('Informe o valor a ser sacado: R$ ')
                if valor_saque < 0:
                    print(colors('ERRO: Informe um valor válido', 'red'))
                    continue
                elif valor_saque == 0:
                    return False
                elif valor_saque > conta.limite_saque:
                    print(colors('\nSua conta não permite saques acima de R$ 500.\n', 'yellow'))
                    continue
                elif valor_saque > conta.saldo:
                    print(colors('SALDO INSUFICIENTE', 'yellow'))
                else:
                    print(f'Realizando saque, aguarde...')
                    sleep(1)
                    conta.sacar(conta, valor_saque)
                    saque_check(conta, True)
                    system('cls')
                    print(colors(f'Saque de R$ {valor_saque}, realizado com sucesso.', 'green'))
                    conta.transacao(conta, 'SAQUE', valor_saque, datetime.now().strftime('%d-%m-%Y as %H:%M:%S'))
                    print(f'\nSALDO ATUAL: R$ {conta.saldo}')
                    return True
        else:
            print(colors(f'VOCÊ ATINGIU O LIMITE DE 3 SAQUES DA SUA CONTA', 'yellow'))
            return False
