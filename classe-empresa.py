class Empresa:
  def __init__(self,nome,cnpj,franquia=False,cep,numero,complemento):
    self._nome = nome
    self._cnpj = cnpj
    self._franquia = franquia
    self.cep = cep
    self._numero = numero
    self._complemento = complemento
    self._proprietario = None

  def associarProprietario(self,proprietario):
    self._proprietario = proprietario

  @property
  def nome(self):
    return self._nome

  @nome.setter(self,nome):
    self.nome = nome
  
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

  def get_franquia(self):
    return self.franquia

  def set_franquia(self,franquia):
    self.franquia = franquia
