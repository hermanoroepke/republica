class TelaTarefa:
    def exibirTelaTarefas(self) -> str:
        return input("Descrição da tarefa: ")

    def capturarNovaTarefa(self) -> dict:
        return {
            "id_morador": int(input("ID do morador responsável: ")),
            "id_tarefa": int(input("ID da tarefa: ")),
        }