from datetime import date

class Despesa:
    def __init__(self, id: int, descricao: str, valor_total: float, data: date = None):
        self.id = id
        self.descricao = descricao
        self.valorTotal = valor_total
        self.data = data or date.today()
        self.rateada_entre = []

    def registrarDespesa(self) -> None:
        print(f"[Despesa] '{self.descricao}' (R$ {self.valorTotal:.2f}) registrada.")

    def calcularRateio(self, quantidadeMoradores: int) -> float:
        if quantidadeMoradores <= 0:
            raise ValueError("Quantidade de moradores deve ser maior que zero.")
        return self.valorTotal / quantidadeMoradores