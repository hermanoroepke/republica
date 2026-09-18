from models import Despesa

class ControladorDespesas:
    def __init__(self, controlador_moradores):
        self.despesas = []
        self.controlador_moradores = controlador_moradores
        self._proximo_id = 1

    def adicionarDespesa(self, descricao: str, valor: float, moradores=None) -> None:
        despesa = Despesa(self._proximo_id, descricao, valor)
        despesa.rateada_entre = moradores or self.controlador_moradores.listarMoradores()
        self.despesas.append(despesa)
        self._proximo_id += 1
        despesa.registrarDespesa()

    def gerarRelatorioDeRateio(self) -> dict:
        relatorio = {}
        for despesa in self.despesas:
            qtd = len(despesa.rateada_entre)
            if qtd == 0:
                continue
            valor = despesa.calcularRateio(qtd)
            for m in despesa.rateada_entre:
                m.atualizarSaldo(valor)
                relatorio[m.getNome()] = relatorio.get(m.getNome(), 0.0) + valor
        return relatorio