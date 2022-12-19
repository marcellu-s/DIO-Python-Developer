from time import sleep
from os import system
from datetime import datetime, date
from re import search


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
    print('='*49)
    print('EXTRATO'.center(49))
    print('='*49)
    for valor in conta['extrato']:
        for tipo, extrato in valor.items():
            print(f'{tipo} \t\t{colors(f"R$ {extrato[1]}", "red")} em {extrato[0]}' if tipo == 'SAQUE' else f'{tipo} \t{colors(f"R$ {extrato[1]}", "green")} em {extrato[0]}')


def filtrar_usuario(usuarios, cpf):
    
    if usuarios.get(cpf) == None:
        return False
    else:
        return True


def criar_usuario(usuarios):
    
    print('='*40)
    print('CRIAR USUÁRIO'.center(40))
    print('='*40)
    
    while True:
        
        cpf = input('Digite seu CPF: ')
        # apenas valida o tamanho
        if search('^[0-9]{11}$', cpf):
            if not filtrar_usuario(usuarios, cpf):
                break
            else:
                print(colors('\nUsuário já cadastrado.\n', 'yellow'))
                continue
        else:
            print(colors('\nERRO: CPF inválido.\n', 'red'))
            continue

    while True:

        name = input('Nome: ').strip()
        if search('[0-9]', name):
            print(colors('\nERRO: Nome inválido.\n', 'red'))
            continue 
        else:
            break

    while True:
        
        data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
        # OBS: está validando somente o formato.
        if search('^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/[12][0-9]{3}$', data_nascimento):
            idade = date.today().year - int(data_nascimento[6:])
            break 
        else: 
            print(colors('\nERRO: Data inválida.\n', 'red'))
            continue

    print('\nOBS: logradouro, nº - bairro - cidade/sigla do estado\n')
    endereco = input('Informe seu endereço: ')

    print('\nCriando...')
    sleep(1.5)
    print(colors('Usuário criado com sucesso... Bem-vindo(a)', 'green'))

    usuarios.setdefault(cpf, {'Nome': name, 'Idade': idade, 'Endereço': endereco})

    return usuarios


def criar_conta(usuarios, agencia, num_conta):
    while True:
        
        cpf = input('Digite seu CPF: ')
        # apenas valida o tamanho
        if search('^[0-9]{11}$', cpf):
            if filtrar_usuario(usuarios, cpf):
                print(colors("\n=== Conta criada com sucesso! ===", 'green'))
                print(f'Agência \t{agencia}')
                print(f'Núm. conta \t{num_conta}')
                print(f'Titular \t{usuarios[cpf]["Nome"]}')
                return {'Agência': agencia, 'Núm. conta': num_conta, 'Titular': usuarios[cpf]['Nome']}
            else:
                print(colors('\nUsuário não encontrado.\n', 'yellow'))
                break
        else:
            print(colors('\nERRO: CPF inválido.\n', 'red'))
            continue
    

def listar_contas(usuarios, contas):
    if len(contas) > 0:
        print('='*40)
        print('CONTAS REGISTRADAS'.center(40))
        for conta in contas:
            print('='*40)
            for key, value in conta.items():
                print(f'{key} \t{value}')
    else:
        print(colors('Nenhuma conta foi encontrada.', 'yellow'))

