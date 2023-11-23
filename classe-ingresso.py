class Ingresso:
  def __init__(self,avaliacao,usuarioApp):
    self.__avaliacao = None
    self.__usuarioApp = None

  def __init__(self,venda,horario,poltrona,sala):
    self.__venda = venda
    self.__horario = horario
    self.__poltrona = poltrona
    self.__sala = sala

  @property
  def avaliacao(self):
    return self.__avaliacao

  @avaliacao.setter
  def avaliacao(self,avaliacao):
    self.__avaliacao = avaliacao

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

    
