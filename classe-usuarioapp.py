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

  def _inscrever_desinscrever(self, lista, objeto, acao):
      if isinstance(objeto, Filme):
          if objeto not in lista and acao == "inscrever":
              lista.append(objeto)
              print(f"{objeto.titulo} foi adicionado na lista de favoritos")
          elif objeto in lista and acao == "desinscrever":
              lista.remove(objeto)
              print(f"{objeto.titulo} foi retirado na lista de favoritos")
          elif acao == "inscrever":
              print(f"{objeto.titulo} já está adicionado na lista de favoritos")
          elif acao == "desinscrever":
              print(f"{objeto.titulo} não está na lista de favoritos")
      else:
          print("Objeto inválido")

  def inscreverFilme(self, filme):
      self._inscrever_desinscrever(self.filmesFavorito, filme, "inscrever")

  def desinscreverFilme(self, filme):
      self._inscrever_desinscrever(self.filmesFavorito, filme, "desinscrever")

  def inscreverGenero(self,genero):
    self._inscrever_desinscrever(self.generosFavorito, genero, "inscrever")
    
  def desinscreverGenero(self,genero):
    self._inscrever_desinscrever(self.generosFavorito, genero, "desinscrever")

  def inscreverAtor(self,ator):
    self._inscrever_desinscrever(self.atoresFavorito, ator, "inscrever")
    
  def desinscreverAtor(self,ator):
    self._inscrever_desinscrever(self.atoresFavorito, ator, "desinscrever")
    
  def inscreverDiretor(self,diretor):
    self._inscrever_desinscrever(self.diretoresFavorito, diretor, "inscrever")
    
  def desinscreverDiretor(self,diretor):
    self._inscrever_desinscrever(self.diretoresFavorito, diretor, "desinscrever")
    
  def inscreverProdutora(self,produtora):
    self._inscrever_desinscrever(self.produtorasFavorito, produtora, "inscrever")
    
  def desinscreverProdutora(self,produtora):
    self._inscrever_desinscrever(self.produtorasFavorito, produtora, "desinscrever")
    
  def inscreverCinema(self,empresa):
    self._inscrever_desinscrever(self.cinemasFavorito, empresa, "inscrever")
    
  def desinscreverCinema(self,empresa):
    self._inscrever_desinscrever(self.cinemasFavorito, empresa, "desinscrever")
  
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
