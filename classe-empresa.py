class Empresa:
  def __init__(self,Proprietario):
    self.__Proprietario = None

  def __init__(self,cnpj,franquia,CEP,numero,complemento):
    self.__cnpj = cnpj
    self.__franquia = franquia
    self.__CEP = CEP
    self.__numero = numero
    self.__complemento = complemento

  @property
  def Proprietario(self):
    return self.__Proprietario

  @Proprietario.setter
  def Propietario(self,Propietario):
    self.__Propietario = Propietario

  @property
  def cnpj(self):
    return self.__cnpj

  @cnpj.setter
  def cnpj(self,cnpj):
    self.__cnpj = cnpj

  @property
  def CEP(self):
    return self.__CEP
    
  @CEP.setter
  def CEP(self,CEP):
    self.__CEP = CEP

  @property
  def numero(self):
    return self.__numero

  @numero.setter
  def numero(self,numero):
    self.__numero = numero

  @property
  def complemento(self):
    return self.__complemento

  @complemento.setter
  def complemento(self,complemento):
    self.__complemento = complemento


