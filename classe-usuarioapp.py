class usuarioApp(Cliente):
  def __init__(self,tipoCliente,idUsuario,perfil,historico,favorito):
    super().__init__(tipoCliente)
    self.__idUsuario = idUsuario
    self.__perfil = perfil
    self.__historico = historico
    self.__favorito = favorito

@property
  def idUsuario(self):
    return self.__idUsuario

  @cpf.setter
  def idUsuario(self,idUsuario):
    self.__idUsuario = idUsuario

  @property
  def perfil(self):
    return self.__perfil

  @empresa.setter
  def perfil(self,perfil):
    self.__perfil = perfil

  @property
  def historico(self):
    return self.__historico

  @endereco.setter
  def historico(self,historico):
    self.__historico = historico

  @property
  def favorito(self):
    return self.__favorito

  @valor.setter
  def favorito(self,favorito):
    self.__favorito = favorito
    
  #métodos da classe

  def criarPerfil(self, perfil):
    self.__perfil = perfil

  def criarFav(self, favorito):
    self.__favorito = favorito
