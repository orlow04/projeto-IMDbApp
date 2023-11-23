class usuarioApp(Cliente):
  def __init__(self,nome,email,senha,telefone,idioma,idade,localizacao):
    super().__init__(nome)
    super().__init__(email)
    super().__init__(senha)
    super().__init__(telefone)
    super().__init__(idioma)
    self.__idade = idade
    self.__localizacao = localizacao



  @property
  def idade(self):
    return self.__idade

  @idade.setter
  def idade(self,idade):
    self.__idade = idade

  @property
  def localizacao(self):
    return self.__localizacao

  @localizacao.setter
  def localizacao(self,localizacao):
    self.__localizacao = localizacao
    
