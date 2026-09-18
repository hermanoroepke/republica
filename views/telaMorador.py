class TelaMorador:

    def tela_opcoes(self):
        print("-------- MORADORES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Morador")
        print("2 - Alterar Morador")
        print("3 - Listar Moradores")
        print("4 - Excluir Morador")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_morador(self):
        print("-------- DADOS MORADOR ----------")
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")
        return {"nome": nome, "email": email, "cpf": cpf}

    def mostra_morador(self, dados_morador):
        print("NOME DO MORADOR: ", dados_morador["nome"])
        print("EMAIL DO MORADOR: ", dados_morador["email"])
        print("CPF DO MORADOR: ", dados_morador["cpf"])
        print("SALDO DEVEDOR: R$ {:.2f}".format(dados_morador["saldo_devedor"]))
        print("\n")

    def seleciona_morador(self):
        cpf = input("CPF do morador que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)