from datetime import date
from views.telaDespesa import TelaDespesa
from models.despesa import Despesa


class ControladorDespesas:

    def __init__(self, controlador_sistema):
        self.__despesas = []
        self.__tela_despesa = TelaDespesa()
        self.__controlador_sistema = controlador_sistema

    def pega_despesa_por_descricao(self, descricao: str):
        for despesa in self.__despesas:
            if despesa.descricao == descricao:
                return despesa
        return None

    def incluir_despesa(self):
        dados = self.__tela_despesa.pega_dados_despesa()

        try:
            ano, mes, dia = map(int, dados["data"].split("-"))
            data_formatada = date(ano, mes, dia)
        except ValueError:
            self.__tela_despesa.mostra_mensagem("Data inválida! Use o formato AAAA-MM-DD.")
            return

        despesa = Despesa(dados["descricao"], dados["valor_total"], data_formatada)
        self.__despesas.append(despesa)

        # Rateia automaticamente entre os moradores
        moradores = self.__controlador_sistema.controlador_moradores.moradores
        if moradores:
            rateio = despesa.calcular_rateio(len(moradores))
            for morador in moradores:
                morador.atualizar_saldo(rateio)
            self.__tela_despesa.mostra_mensagem(
                f"Despesa registrada! Cada morador deve R$ {rateio:.2f}"
            )
        else:
            self.__tela_despesa.mostra_mensagem(
                "Despesa registrada, mas não há moradores para ratear."
            )

    def lista_despesas(self):
        if not self.__despesas:
            self.__tela_despesa.mostra_mensagem("Nenhuma despesa registrada.")
            return

        moradores = self.__controlador_sistema.controlador_moradores.moradores
        qtd = len(moradores) if moradores else 1

        for despesa in self.__despesas:
            self.__tela_despesa.mostra_despesa({
                "descricao": despesa.descricao,
                "valor_total": despesa.valor_total,
                "data": despesa.data,
                "rateio": despesa.calcular_rateio(qtd)
            })

    def excluir_despesa(self):
        self.lista_despesas()
        descricao = self.__tela_despesa.seleciona_despesa()
        despesa = self.pega_despesa_por_descricao(descricao)

        if despesa is not None:
            self.__despesas.remove(despesa)
            self.lista_despesas()
        else:
            self.__tela_despesa.mostra_mensagem("ATENCAO: Despesa não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_despesa,
            2: self.lista_despesas,
            3: self.excluir_despesa,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_despesa.tela_opcoes()]()