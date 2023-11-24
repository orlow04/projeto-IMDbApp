class Empresa:
  def __init__(self,Proprietario):
    self._Proprietario = None

  def __init__(self,cnpj,franquia,CEP,numero,complemento):
    self._cnpj = cnpj
    self._franquia = franquia
    self._CEP = CEP
    self._numero = numero
    self._complemento = complemento

  @property
  def Proprietario(self):
    return self._Proprietario

  @Proprietario.setter
  def Propietario(self,Propietario):
    self._Propietario = Propietario

  @property
  def cnpj(self):
    return self._cnpj

  @cnpj.setter
  def cnpj(self,cnpj):
    self._cnpj = cnpj

  @property
  def CEP(self):
    return self._CEP
    
  @CEP.setter
  def CEP(self,CEP):
    self._CEP = CEP

  @property
  def numero(self):
    return self._numero

  @numero.setter
  def numero(self,numero):
    self._numero = numero

  @property
  def complemento(self):
    return self._complemento

  @complemento.setter
  def complemento(self,complemento):
    self._complemento = complemento
