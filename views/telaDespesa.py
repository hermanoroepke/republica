class TelaDespesa:

    def tela_opcoes(self):
        print("-------- DESPESAS ----------")
        print("Escolha a opcao")
        print("1 - Registrar Despesa")
        print("2 - Listar Despesas")
        print("3 - Excluir Despesa")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_despesa(self):
        print("-------- DADOS DESPESA ----------")
        descricao = input("Descrição: ")
        valor_total = float(input("Valor total: "))
        data = input("Data (AAAA-MM-DD): ")
        return {"descricao": descricao, "valor_total": valor_total, "data": data}

    def mostra_despesa(self, dados_despesa):
        print("DESCRIÇÃO: ", dados_despesa["descricao"])
        print("VALOR TOTAL: R$ {:.2f}".format(dados_despesa["valor_total"]))
        print("DATA: ", dados_despesa["data"])
        print("RATEIO POR MORADOR: R$ {:.2f}".format(dados_despesa["rateio"]))
        print("\n")

    def seleciona_despesa(self):
        descricao = input("Descrição da despesa que deseja selecionar: ")
        return descricao

    def mostra_mensagem(self, msg):
        print(msg)