from models import Tarefa

class ControladorTarefas:
    def __init__(self, controlador_moradores):
        self.tarefas = []
        self.controlador_moradores = controlador_moradores
        self._proximo_id = 1

    def criarTarefa(self, descricao: str) -> Tarefa:
        tarefa = Tarefa(self._proximo_id, descricao)
        self.tarefas.append(tarefa)
        self._proximo_id += 1
        tarefa.registrarTarefa()
        return tarefa

    def atribuirTarefa(self, idMorador: int, idTarefa: int, dataRealizacao) -> None:
        morador = self.controlador_moradores.buscarPorId(idMorador)
        tarefa = self._buscarTarefa(idTarefa)
        if not morador or not tarefa:
            print("[Erro] Morador ou tarefa não encontrado.")
            return
        tarefa.responsavel = morador
        print(f"[Tarefa] '{tarefa.descricao}' atribuída a {morador.getNome()} para {dataRealizacao}.")

    def marcarComoConcluida(self, idTarefa: int) -> None:
        tarefa = self._buscarTarefa(idTarefa)
        if tarefa:
            tarefa.alterarStatus()

    def _buscarTarefa(self, idTarefa: int):
        return next((t for t in self.tarefas if t.id == idTarefa), None)