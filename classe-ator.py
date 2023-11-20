class Ator:
  def __init__(self,nome,papel,outrosPapeis,main,biografia):
    self.__nome = nome
    self.__papel = papel
    self.__outrosPapeis = outrosPapeis
    self.__main = main
    self.__biografia = biografia
    
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,nome):
    self.__nome = nome

  @property
  def papel(self):
    return self.__papel

  @papel.setter
  def papel(self,papel):
    self.__papel = papel

  @property
  def outrosPapeis(self):
    return self.__outrosPapeis

  @outrosPapeis.setter
  def outrosPapeis(self,outrosPapeis):
    self.__outrosPapeis = outrosPapeis

  @property
  def main(self):
    return self.__main

  @main.setter
  def main(self,main):
    self.__main = main

  @property
  def biografia(self):
    return self.__biografia

  @biografia.setter
  def biografia(self,biografia):
    self.__biografia = biografia
  
