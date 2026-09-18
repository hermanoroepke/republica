class Morador:
    def __init__(self, nome: str, email: str, cpf: str):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__saldo_devedor = 0.0

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def saldo_devedor(self):
        return self.__saldo_devedor

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @email.setter
    def email(self, email: str):
        self.__email = email

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    def atualizar_saldo(self, valor: float):
        self.__saldo_devedor += valor
        return self.__saldo_devedor