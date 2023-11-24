class usuarioApp(Cliente):
  def __init__(self,nome,email,senha,telefone,idioma,idade,localizacao):
    super().__init__(nome)
    super().__init__(email)
    super().__init__(senha)
    super().__init__(telefone)
    super().__init__(idioma)
    self._idade = idade
    self._localizacao = localizacao



  @property
  def idade(self):
    return self._idade

  @idade.setter
  def idade(self,idade):
    self._idade = idade

  @property
  def localizacao(self):
    return self._localizacao

  @localizacao.setter
  def localizacao(self,localizacao):
    self._localizacao = localizacao
    
