class Empresa:
  def __init__(self,Proprietario):
    self._Proprietario = None

  def __init__(self,cnpj,franquia,cep,numero,complemento):
    self._cnpj = cnpj
    self._franquia = franquia
    self.cep = cep
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
  def cep(self):
    return self._cep
    
  @cep.setter
  def cep(self,cep):
    self._cep = cep

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
