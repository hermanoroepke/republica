class Tarefa:
    def __init__(self, descricao: str):
        self.__descricao = descricao
        self.__concluida = False

    @property
    def descricao(self):
        return self.__descricao

    @property
    def concluida(self):
        return self.__concluida

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    def alterar_status(self):
        self.__concluida = not self.__concluida
        return self.__concluida