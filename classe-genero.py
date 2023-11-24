#Classe Gênero:
class Genero:
    def __init__(self, tipo):
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f'Gênero: {self._tipo}'
