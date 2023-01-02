class Cliente:
    def __init__(self, cpf, nome, idade):
        self.cpf = cpf 
        self.nome = nome 
        self.idade = idade



class Conta:
    def __init__(self, usuario, num_conta, cpf):
        self._qnta_limite_saque = 3
        self._limite_saque = 500
        self._saldo = 0
        self._agencia = '0001'
        self._extrato = []
        self._usuario = usuario
        self._num_conta = num_conta
        self._cpf = cpf

    
    @classmethod
    def criar_conta(cls, usuario, num_conta, cpf):
        return cls(usuario, num_conta, cpf)

    
    @property
    def limite_saque(self):
        return self._limite_saque
    

    @property
    def saldo(self):
        return self._saldo 

    
    @property
    def agencia(self):
        return self._agencia 


    @property
    def usuario(self):
        return self._usuario

    
    @property
    def num_conta(self):
        return self._num_conta

    
    @property
    def cpf(self):
        return self._cpf

    
    @property
    def extrato(self):
        return self._extrato

    
    @property
    def qnta_limite_saque(self):
        return self._qnta_limite_saque


    @classmethod
    def len_extrato(self, conta):
        if len(conta._extrato) > 0:
            return True 
        else:
            return False

    
    def sacar(self, conta, valor):
        conta._saldo -= valor 
        return True


    def depositar(self, conta, valor):
        conta._saldo += valor
        return True

    
    def transacao(self, conta, tipo, valor, horario):
        conta._extrato.append({'Tipo': tipo, 'Valor': valor, 'Horario': horario})
        return True

    
    def qnta_limite_de_saque(self, conta, sacar):
        if conta._qnta_limite_saque > 0:
            if sacar:
                conta._qnta_limite_saque -= 1
                return True
            else:
                return True
        else:
            return False
