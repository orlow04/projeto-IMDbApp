class Proprietario(Cliente):
  def __init__(self,nome,email,senha,telefone,idioma,cpf,numeroFranquia):
    super().__init__(nome)
    super().__init__(email)
    super().__init__(senha)
    super().__init__(telefone)
    super().__init__(idioma)
    self.__cpf = cpf
    self.__numeroFranquia = numeroFranquia

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self,cpf):
    self.__cpf = cpf

  @property
  def numeroFranquia(self):
    return self.__numeroFranquia

  @numeroFranquia.setter
  def numeroFranquia(self,numeroFranquia):
    self.__numeroFranquia = numeroFranquia
