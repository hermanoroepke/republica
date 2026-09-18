from views.telaTarefa import TelaTarefa
from models.tarefa import Tarefa


class ControladorTarefas:

    def __init__(self, controlador_sistema):
        self.__tarefas = []
        self.__tela_tarefa = TelaTarefa()
        self.__controlador_sistema = controlador_sistema

    def pega_tarefa_por_descricao(self, descricao: str):
        for tarefa in self.__tarefas:
            if tarefa.descricao == descricao:
                return tarefa
        return None

    def incluir_tarefa(self):
        dados = self.__tela_tarefa.pega_dados_tarefa()
        tarefa = Tarefa(dados["descricao"])
        self.__tarefas.append(tarefa)
        self.__tela_tarefa.mostra_mensagem("Tarefa registrada!")

    def lista_tarefas(self):
        if not self.__tarefas:
            self.__tela_tarefa.mostra_mensagem("Nenhuma tarefa registrada.")
            return
        for tarefa in self.__tarefas:
            self.__tela_tarefa.mostra_tarefa({
                "descricao": tarefa.descricao,
                "concluida": tarefa.concluida
            })

    def alterar_status_tarefa(self):
        self.lista_tarefas()
        descricao = self.__tela_tarefa.seleciona_tarefa()
        tarefa = self.pega_tarefa_por_descricao(descricao)

        if tarefa is not None:
            tarefa.alterar_status()
            self.lista_tarefas()
        else:
            self.__tela_tarefa.mostra_mensagem("ATENCAO: Tarefa não existente")

    def excluir_tarefa(self):
        self.lista_tarefas()
        descricao = self.__tela_tarefa.seleciona_tarefa()
        tarefa = self.pega_tarefa_por_descricao(descricao)

        if tarefa is not None:
            self.__tarefas.remove(tarefa)
            self.lista_tarefas()
        else:
            self.__tela_tarefa.mostra_mensagem("ATENCAO: Tarefa não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_tarefa,
            2: self.lista_tarefas,
            3: self.alterar_status_tarefa,
            4: self.excluir_tarefa,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_tarefa.tela_opcoes()]()