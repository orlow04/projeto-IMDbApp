class donoCinema(Cliente):
  def __init__(self,tipoCliente,cpf,empresa,endereco,valor):
    super().__init__(tipoCliente)
    self.__cpf = cpf
    self.__empresa = empresa
    self.__endereco = endereco
    self.__valor = valor

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self,cpf):
    self.__cpf = cpf

  @property
  def empresa(self):
    return self.__empresa

  @empresa.setter
  def empresa(self,empresa):
    self.__empresa = empresa

  @property
  def endereco(self):
    return self.__endereco

  @endereco.setter
  def endereco(self,endereco):
    self.__endereco = endereco

  @property
  def valor(self):
    return self.__valor

  @valor.setter
  def valor(self,valor):
    self.__valor = valor

# métodos da classe
def setValor(self, valor):
  self.__valor = valor

def setCinema(self, empresa):
  self.__empresa = empresa

