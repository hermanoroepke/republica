class TelaDespesa:
    def exibirTelaDespesas(self) -> tuple[str, float]:
        descricao = input("Descrição da despesa: ")
        valor = float(input("Valor total (R$): "))
        return descricao, valor

    def mostrarRateio(self, dadosRateio: dict) -> None:
        print("\n--- Relatório de Rateio ---")
        for nome, valor in dadosRateio.items():
            print(f"{nome}: R$ {valor:.2f}")