
class Cliente(Pessoa):
    def __init__(self, nome, funcao, tipo):
        super().__init__(nome, funcao)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
