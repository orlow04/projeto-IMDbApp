class Pessoa:
    def __init__(self, nome, funcao):
        self.__nome = nome
        self.__funcao = funcao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao

    

class Filme:
    def __init(self, titulo, duracao, ano, classificacaoEtaria, plot, main, sinopse):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__ano = ano
        self.__classificacaoEtaria = classificacaoEtaria
        self.__plot = plot
        self.__main = main
        self.__sinopse = sinopse

    #Encapsular os atributos, de modo que eles não possam ser modificados diretamente
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def classificacaoEtaria(self):
        return self.__classificacaoEtaria

    @classificacaoEtaria.setter
    def classificacaoEtaria(self, classificacaoEtaria):
        self.__classificacaoEtaria = classificacaoEtaria

    @property
    def plot(self):
        return self.__plot

    @plot.setter
    def plot(self, plot):
        self.__plot = plot

    @property
    def main(self):
        return self.__main

    @main.setter
    def main(self, main):
        self.__main = main

    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse):
        self.__sinopse = sinopse

class Cliente(Pessoa):
    def __init__(self, nome, funcao, tipo):
        super().__init__(nome, funcao)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def funcao:
