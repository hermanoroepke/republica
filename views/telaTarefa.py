class TelaTarefa:

    def tela_opcoes(self):
        print("-------- TAREFAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Alterar Status")
        print("4 - Excluir Tarefa")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_tarefa(self):
        print("-------- DADOS TAREFA ----------")
        descricao = input("Descrição: ")
        return {"descricao": descricao}

    def mostra_tarefa(self, dados_tarefa):
        status = "✅ Concluída" if dados_tarefa["concluida"] else "⏳ Pendente"
        print("DESCRIÇÃO: ", dados_tarefa["descricao"])
        print("STATUS: ", status)
        print("\n")

    def seleciona_tarefa(self):
        descricao = input("Descrição da tarefa que deseja selecionar: ")
        return descricao

    def mostra_mensagem(self, msg):
        print(msg)