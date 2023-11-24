#Classe Ator:
class Ator:
    def __init__(self, nome, idade, personagem, outroTrabalhos, biografia, premio):
        self.__nome = nome
        self.__idade = idade
        self.__personagem = personagem
        self.__outroTrabalhos = outroTrabalhos
        self.__biografia = biografia
        self.__premio = premio

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def personagem(self):
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem):
        self.__personagem = personagem

    @property
    def outroTrabalhos(self):
        return self.__outroTrabalhos

    @outroTrabalhos.setter
    def outroTrabalhos(self, outroTrabalhos):
        self.__outroTrabalhos = outroTrabalhos

    @property
    def biografia(self):
        return self.__biografia

    @biografia.setter
    def biografia(self, biografia):
        self.__biografia = biografia

    @property
    def premio(self):
        return self.__premio

    @premio.setter
    def premio(self, premio):
        self.__premio = premio
