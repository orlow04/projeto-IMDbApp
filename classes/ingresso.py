#Classe Ingresso: Ok
class Ingresso:
    def __init__(self, horario, poltrona, sala, identificador, vendido=True):
        self._vendido = vendido
        self._horario = horario
        self._poltrona = poltrona
        self._sala = sala
        self._identificador = identificador
        self._avaliacao = None
        self._usuarioApp = None

    @property
    def avaliacao(self):
        return self._avaliacao

    @avaliacao.setter
    def avaliacao(self, avaliacao):
        self._avaliacao = avaliacao

    @property
    def usuarioApp(self):
        return self._usuarioApp

    @usuarioApp.setter
    def usuarioApp(self, usuarioApp):
        self._usuarioApp = usuarioApp

    @property
    def vendido(self):
        return self._vendido
    
    @vendido.setter
    def vendido(self, vendido):
        self._vendido = vendido

    @property
    def horario(self):
        return self._horario

    @horario.setter
    def horario(self, horario):
        self._horario = horario

    @property
    def poltrona(self):
        return self._poltrona

    @poltrona.setter
    def poltrona(self, poltrona):
        self._poltrona = poltrona

    @property
    def sala(self):
        return self._sala

    @sala.setter
    def sala(self, sala):
        self._sala = sala

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, identificador):
        self._identificador = identificador

    def __str__(self):
        return f"Horário: {self.horario}\nPoltrona: {self.poltrona}\nSala: {self.sala}\nIdentificador: {self.identificador}\nVendido: {self._vendido}\nAvaliação: {self._avaliacao}\nUsuário: {self._usuarioApp}"

