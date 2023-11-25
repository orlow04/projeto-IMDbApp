#Classe Diretor: Ok
class Diretor:
    def __init__(self, nome, idade, outrosTrabalhos, biografia, premio):
        self.__nome = nome
        self.__idade = idade
        self.__outrosTrabalhos = outrosTrabalhos
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
    def outrosTrabalhos(self):
        return self.__outrosTrabalhos

    @outrosTrabalhos.setter
    def outrosTrabalhos(self, outrosTrabalhos):
      self.__outrosTrabalhos = outrosTrabalhos

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

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nOutros trabalhos: {self.outrosTrabalhos}\nBiografia: {self.biografia}\nPrêmio: {self.premio}'

# teste:
diretor = Diretor('Murilo Alvares', 19, 'O menino que descobriu o vento', 'Nacsido em Goiânia...',
                  'Oscar de Melhor Diretor')
print(diretor.nome)
print(diretor.idade)
print(diretor.outrosTrabalhos)
print(diretor.biografia)
print(diretor.premio)
print()
print(diretor)
