from datetime import date


class Despesa:
    def __init__(self, descricao: str, valor_total: float, data: date):
        self.__descricao = descricao
        self.__valor_total = valor_total
        self.__data = data

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def data(self):
        return self.__data

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @valor_total.setter
    def valor_total(self, valor: float):
        self.__valor_total = valor

    @data.setter
    def data(self, data: date):
        self.__data = data

    def calcular_rateio(self, quantidade_moradores: int) -> float:
        if quantidade_moradores == 0:
            return 0.0
        return self.__valor_total / quantidade_moradores