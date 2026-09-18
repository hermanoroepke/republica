class Tarefa:
    def __init__(self, id: int, descricao: str, concluida: bool = False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida
        self.responsavel = None

    def registrarTarefa(self) -> None:
        print(f"[Tarefa] '{self.descricao}' registrada.")

    def alterarStatus(self) -> None:
        self.concluida = not self.concluida
        status = "concluída" if self.concluida else "pendente"
        print(f"[Tarefa] '{self.descricao}' agora está {status}.")