#Classe Produtora: Ok
class Produtora:
    def __init__(self, nome, sede, dono, endereco):
        self.__nome = nome
        self.__sede = sede
        self.__dono = dono
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sede(self):
        return self.__sede
    @sede.setter
    def sede(self, sede):
        self.__sede = sede

    @property
    def dono(self):
        return self.__dono
    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    def __str__(self):
        return f'Nome: {self.__nome}\nSede: {self.__sede}\nDono: {self.__dono}\nEndereço: {self.__endereco}'
