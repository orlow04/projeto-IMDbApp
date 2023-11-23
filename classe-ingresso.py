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
    def usuarioApp(self):
        return self.__usuarioApp

    @usuarioApp.setter
    def usuarioApp(self, usuarioApp):
        self.__usuarioApp = usuarioApp

  @property
  def venda(self):
    return self.__venda

  @venda.setter
  def venda(self,venda):
    self.__venda = venda

  @property
  def horario(self):
    return self.__horario

  @horario.setter
  def horario(self,horario):
    self.__horario = horario

  @property
  def poltrona(self):
    return self.__poltrona

  @poltrona.setter
  def poltrona(self,poltrona):
    self.__poltrona = poltrona

  @property
  def sala(self):
    return self.__sala

  @sala.setter
  def sala(self,sala):
    self.__sala = sala


    
