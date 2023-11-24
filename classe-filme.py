#Classe Filme:
class Filme:
    def __init__(self, titulo, duracao, ano, classificacaoEtaria, sinopse, notaIMDB, premio):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__ano = ano
        self.__classificacaoEtaria = classificacaoEtaria
        self.__sinopse = sinopse
        self.__notaIMDB = notaIMDB
        self.__premio = premio
        
        self.__genero = None
        
        self.__produtora = None
        self.__atores = []
        self.__diretor = None

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
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse):
        self.__sinopse = sinopse

    @property
    def notaIMDB(self):
        return self.__notaIMDB

    @notaIMDB.setter
    def notaIMDB(self, notaIMDB):
        self.__notaIMDB = notaIMDB

    @property
    def premio(self):
        return self.__premio

    @premio.setter
    def premio(self, premio):
        self.__premio = premio

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero.tipo

    @property
    def produtora(self):
        return self.__produtora

    @produtora.setter
    def produtora(self, produtora):
        self.__produtora = produtora.nome

    @property
    def atores(self):
        return self.__atores

    def adicionar_ator(self, ator):
        self.__atores.append(ator.nome)

    @property
    def diretor(self):
        return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor.nome

    def __str__(self):
      return f'Título: {self.__titulo}\nDuração: {self.__duracao}\nAno: {self.__ano}\nClassificação Etária: {self.__classificacaoEtaria}\nSinopse: {self.__sinopse}\nNota IMDB: {self.__notaIMDB}\nPrêmio: {self.__premio}\nGênero: {self.__genero}\nProdutora: {self.__produtora}\nAtores: {self.__atores}\nDiretor: {self.__diretor}'
