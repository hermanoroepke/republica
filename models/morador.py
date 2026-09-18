class Morador:
    def __init__(self, id: int, nome: str, email: str, saldo_devedor: float = 0.0):
        self.id = id
        self.nome = nome
        self.email = email
        self.saldoDevedor = saldo_devedor

    def registrarMorador(self) -> None:
        print(f"[Morador] {self.nome} registrado com sucesso.")

    def getNome(self) -> str:
        return self.nome

    def atualizarSaldo(self, valor: float) -> None:
        self.saldoDevedor += valor

    def __repr__(self):
        return f"Morador(id={self.id}, nome='{self.nome}', saldo={self.saldoDevedor:.2f})"