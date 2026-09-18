from views.telaMorador import TelaMorador
from models.morador import Morador
from exceptions.moradorRepetidoException import MoradorRepetidoException


class ControladorMoradores:

    def __init__(self, controlador_sistema):
        self.__moradores = []
        self.__tela_morador = TelaMorador()
        self.__controlador_sistema = controlador_sistema

    def pega_morador_por_cpf(self, cpf: str):
        for morador in self.__moradores:
            if morador.cpf == cpf:
                return morador
        return None

    def incluir_morador(self):
        dados_morador = self.__tela_morador.pega_dados_morador()
        cpf = dados_morador["cpf"]
        morador = self.pega_morador_por_cpf(cpf)
        try:
            if morador is None:
                morador = Morador(dados_morador["nome"],
                                  dados_morador["email"],
                                  dados_morador["cpf"])
                self.__moradores.append(morador)
                self.__tela_morador.mostra_mensagem("Morador cadastrado com sucesso!")
            else:
                raise MoradorRepetidoException(cpf)
        except MoradorRepetidoException as e:
            self.__tela_morador.mostra_mensagem(e)

    def alterar_morador(self):
        self.lista_moradores()
        cpf_morador = self.__tela_morador.seleciona_morador()
        morador = self.pega_morador_por_cpf(cpf_morador)

        if morador is not None:
            novos_dados = self.__tela_morador.pega_dados_morador()
            morador.nome = novos_dados["nome"]
            morador.email = novos_dados["email"]
            morador.cpf = novos_dados["cpf"]
            self.lista_moradores()
        else:
            self.__tela_morador.mostra_mensagem("ATENCAO: Morador não existente")

    def lista_moradores(self):
        if not self.__moradores:
            self.__tela_morador.mostra_mensagem("Nenhum morador cadastrado.")
            return
        for morador in self.__moradores:
            self.__tela_morador.mostra_morador({
                "nome": morador.nome,
                "email": morador.email,
                "cpf": morador.cpf,
                "saldo_devedor": morador.saldo_devedor
            })

    def excluir_morador(self):
        self.lista_moradores()
        cpf_morador = self.__tela_morador.seleciona_morador()
        morador = self.pega_morador_por_cpf(cpf_morador)

        if morador is not None:
            self.__moradores.remove(morador)
            self.lista_moradores()
        else:
            self.__tela_morador.mostra_mensagem("ATENCAO: Morador não existente")

    @property
    def moradores(self):
        return self.__moradores

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_morador,
            2: self.alterar_morador,
            3: self.lista_moradores,
            4: self.excluir_morador,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_morador.tela_opcoes()]()