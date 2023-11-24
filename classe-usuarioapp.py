class usuarioApp(Cliente):
  def __init__(self,nome,email,senha,telefone,idioma,idade,localizacao):
    super().__init__(nome,email,senha,telefone,idioma)
    self._idade = idade
    self._localizacao = localizacao
    self.filme = None
    self.genero = None
    self.ator = None
    self.diretor = None
    self.produtora = None
    self.empresa = None
    self.filmesFavorito = []
    self.generosFavorito = []
    self.atoresFavorito = []
    self.diretoresFavorito = []
    self.produtorasFavorito = []
    self.cinemasFavorito = []

  def inscreverFilme(self, filme):
      if isinstance(filme, Filme): 
          self.filmesFavorito.append(filme)
          print(f"{filme.titulo} foi adicionado na lista de favoritos")
      else:
          print("Objeto inválido")

  def desinscreverFilme(self, filme):
      if isinstance(filme, Filme):  
          if filme in self.filmesFavorito:
              self.filmesFavorito.remove(filme)
              print(f"{filme.titulo} foi retirado na lista de favoritos")
          else:
              print(f"{filme.titulo} não está na lista de favoritos")
      else:
          print("Objeto inválido")
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
