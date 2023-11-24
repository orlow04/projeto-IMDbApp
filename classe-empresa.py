class Empresa:
  def __init__(self,cnpj,franquia=False,cep,numero,complemento):
    self._cnpj = cnpj
    self._franquia = franquia
    self.cep = cep
    self._numero = numero
    self._complemento = complemento
    self._proprietario = None

  def associarProprietario(self,proprietario):
    self._proprietario = proprietario

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
