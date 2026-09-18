from datetime import date

from controllers import (
    ControladorMoradores,
    ControladorDespesas,
    ControladorTarefas,
)
from views import TelaMorador, TelaDespesa, TelaTarefa


def main():
    # Controllers
    ctrl_moradores = ControladorMoradores()
    ctrl_despesas = ControladorDespesas(ctrl_moradores)
    ctrl_tarefas = ControladorTarefas(ctrl_moradores)

    # Views
    tela_morador = TelaMorador()
    tela_despesa = TelaDespesa()
    tela_tarefa = TelaTarefa()

    # Cadastro inicial (simulado)
    ctrl_moradores.cadastrarMorador({"nome": "Hermano", "email": "hermano@email.com"})
    ctrl_moradores.cadastrarMorador({"nome": "Cecilia", "email": "cecilia@email.com"})
    ctrl_moradores.cadastrarMorador({"nome": "Jean", "email": "jean@email.com"})
    ctrl_moradores.cadastrarMorador({"nome": "Vinicius", "email": "vinicius@email.com"})

    # Despesas
    ctrl_despesas.adicionarDespesa("Hamburgada", 100.0)
    ctrl_despesas.adicionarDespesa("Luz", 300.0)
    ctrl_despesas.adicionarDespesa("Internet", 100.0)

    tela_despesa.mostrarRateio(ctrl_despesas.gerarRelatorioDeRateio())

    # Tarefas
    t1 = ctrl_tarefas.criarTarefa("Lavar a louça")
    ctrl_tarefas.atribuirTarefa(idMorador=1, idTarefa=t1.id, dataRealizacao=date.today())
    ctrl_tarefas.marcarComoConcluida(t1.id)


if __name__ == "__main__":
    main()