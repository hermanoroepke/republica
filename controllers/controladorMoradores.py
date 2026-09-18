from models import Morador

class ControladorMoradores:
    def __init__(self):
        self.moradores = []
        self._proximo_id = 1

    def cadastrarMorador(self, dados: dict) -> None:
        morador = Morador(self._proximo_id, dados["nome"], dados["email"])
        self.moradores.append(morador)
        self._proximo_id += 1
        morador.registrarMorador()

    def listarMoradores(self):
        return self.moradores

    def buscarPorId(self, id_morador: int):
        return next((m for m in self.moradores if m.id == id_morador), None)