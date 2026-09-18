class TelaMorador:
    def capturarDadosMorador(self) -> dict:
        return {
            "nome": input("Nome do morador: "),
            "email": input("Email do morador: "),
        }

    def mostrarMensagem(self, msg: str) -> None:
        print(msg)