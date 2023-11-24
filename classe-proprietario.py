from classe-cliente import Cliente

class Proprietario(Cliente):
  def __init__(self,nome,email,senha,telefone,idioma,cpf,numeroFranquia):
    super().__init__(nome)
    super().__init__(email)
    super().__init__(senha)
    super().__init__(telefone)
    super().__init__(idioma)
    self._cpf = cpf
    self._numeroFranquia = numeroFranquia

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
