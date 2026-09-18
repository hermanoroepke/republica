from views.telaSistema import TelaSistema
from controllers.controladorMoradores import ControladorMoradores
from controllers.controladorDespesas import ControladorDespesas
from controllers.controladorTarefas import ControladorTarefas


class ControladorSistema:

    def __init__(self):
        self.__controlador_moradores = ControladorMoradores(self)
        self.__controlador_despesas = ControladorDespesas(self)
        self.__controlador_tarefas = ControladorTarefas(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_moradores(self):
        return self.__controlador_moradores

    @property
    def controlador_despesas(self):
        return self.__controlador_despesas

    @property
    def controlador_tarefas(self):
        return self.__controlador_tarefas

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_moradores(self):
        self.__controlador_moradores.abre_tela()

    def cadastra_despesas(self):
        self.__controlador_despesas.abre_tela()

    def cadastra_tarefas(self):
        self.__controlador_tarefas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_moradores,
            2: self.cadastra_despesas,
            3: self.cadastra_tarefas,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()