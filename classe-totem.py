class Totem:
  def __init__(self):
    self.__cinema = None

  def __init__(self,filmes,catalogo):
    self.__filmes = filmes
    self.__catalogo = catalogo

  @property
  def cinema(self):
    return self.__cinema

  @cinema.setter
  def cinema(self,cinema):
    self.__cinema = cinema

  @property
  def filmes(self):
    return self.__filmes

  @filmes.setter
  def filmes(self,filmes):
    self.__filmes = filmes

  @property
  def catalogo(self):
    return self.__catalogo

  @catalogo.setter
  def cinema(self,catalogo):
    self.__catalogo = catalogo

  #metódos da classe

  def getCatalogo(self,catalogo):
    return self.__catalogo
  
  def __str__(self):
    return f'[{self.catalogo}]'

    
