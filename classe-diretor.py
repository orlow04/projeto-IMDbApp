class Diretor:   
  def __init__(self, nome, outros_trabalhos, main, biografia):
    self.nome = nome
    self.outros_trabalhos = outros_trabalhos
    self.main = main
    self.biografia = biografia

@property
def nome(self):
  return self.__nome

@nome.setter
def nome(self, nome):
  self.__nome = nome

@outros_trabalhos.setter
def outros_trabalhos(self, outros_trabalhos):
  self.__outros_trabalhos = outros_trabalhos

@property
def main(self):
  return self.__main

@main.setter
def main(self, main):
  self.__main = main

@property
def biografia(self):
  return self.__biografia

@biografia.setter
def biografia(self, biografia):
  self.__biografia = biografia

def __str__(self):
  return f'Nome: {self.nome}\nOutros Trabalhos: {self.outros_trabalhos}\nMain: {self.main}\nBiografia: {self.biografia}'
