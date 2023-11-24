class Proprietario(Cliente):
  def __init__(self,nome,email,senha,telefone,idioma,cpf,numeroFranquia):
    super().__init__(nome,email,senha,telefone,idioma)
    self._cpf = cpf
    self._numeroFranquia = numeroFranquia
    self.empresa = None

  def checaFranquia(self):
    if self.empresa.get_franquia():
      print("A empresa é franquia")
    else:
      print("A empresa não é franquia")
      
  @property
  def cpf(self):
    return self._cpf

  @cpf.setter
  def cpf(self,cpf):
    self._cpf = cpf

  @property
  def numeroFranquia(self):
    return self._numeroFranquia

  @numeroFranquia.setter
  def numeroFranquia(self,numeroFranquia):
    self._numeroFranquia = numeroFranquia
