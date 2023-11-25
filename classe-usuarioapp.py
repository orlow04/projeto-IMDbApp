#Classe Usuário App: Pendente
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

  def _inscrever_desinscreverF(self, lista, objeto, acao):
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
  
  def _inscrever_desinscreverG(self, lista, objeto, acao):
      if isinstance(objeto, Genero):
        if objeto not in lista and acao == "inscrever":
            lista.append(objeto)
            print(f"{objeto.tipo} foi adicionado na lista de favoritos")
        elif objeto in lista and acao == "desinscrever":
            lista.remove(objeto)
            print(f"{objeto.tipo} foi retirado na lista de favoritos")
        elif acao == "inscrever":
            print(f"{objeto.tipo} já está adicionado na lista de favoritos")
        elif acao == "desinscrever":
            print(f"{objeto.tipo} não está na lista de favoritos")
      else:
          print("Objeto inválido")
 
  def _inscrever_desinscreverA(self, lista, objeto, acao):
      if isinstance(objeto, Ator):
        if objeto not in lista and acao == "inscrever":
            lista.append(objeto)
            print(f"{objeto.nome} foi adicionado na lista de favoritos")
        elif objeto in lista and acao == "desinscrever":
            lista.remove(objeto)
            print(f"{objeto.nome} foi retirado na lista de favoritos")
        elif acao == "inscrever":
            print(f"{objeto.nome} já está adicionado na lista de favoritos")
        elif acao == "desinscrever":
            print(f"{objeto.nome} não está na lista de favoritos")
      else:
          print("Objeto inválido")
 
  def _inscrever_desinscreverD(self, lista, objeto, acao):
      if isinstance(objeto, Diretor):
          if objeto not in lista and acao == "inscrever":
              lista.append(objeto)
              print(f"{objeto.nome} foi adicionado na lista de favoritos")
          elif objeto in lista and acao == "desinscrever":
              lista.remove(objeto)
              print(f"{objeto.nome} foi retirado na lista de favoritos")
          elif acao == "inscrever":
              print(f"{objeto.nome} já está adicionado na lista de favoritos")
          elif acao == "desinscrever":
              print(f"{objeto.nome} não está na lista de favoritos")
      else:
          print("Objeto inválido")
 
  
  def _inscrever_desinscreverP(self, lista, objeto, acao):
      if isinstance(objeto, Produtora):
          if objeto not in lista and acao == "inscrever":
              lista.append(objeto)
              print(f"{objeto.nome} foi adicionado na lista de favoritos")
          elif objeto in lista and acao == "desinscrever":
              lista.remove(objeto)
              print(f"{objeto.nome} foi retirado na lista de favoritos")
          elif acao == "inscrever":
              print(f"{objeto.nome} já está adicionado na lista de favoritos")
          elif acao == "desinscrever":
              print(f"{objeto.nome} não está na lista de favoritos")
      else:
          print("Objeto inválido")
   
  def _inscrever_desinscreverC(self, lista, objeto, acao):
    if isinstance(objeto, Empresa):
        if objeto not in lista and acao == "inscrever":
            lista.append(objeto)
            print(f"{objeto.nome} foi adicionado na lista de favoritos")
        elif objeto in lista and acao == "desinscrever":
            lista.remove(objeto)
            print(f"{objeto.nome} foi retirado na lista de favoritos")
        elif acao == "inscrever":
            print(f"{objeto.nome} já está adicionado na lista de favoritos")
        elif acao == "desinscrever":
            print(f"{objeto.nome} não está na lista de favoritos")
    else:
        print("Objeto inválido")
  
  def inscreverFilme(self, filme):
      self._inscrever_desinscreverF(self.filmesFavorito, filme, "inscrever")

  def desinscreverFilme(self, filme):
      self._inscrever_desinscreverF(self.filmesFavorito, filme, "desinscrever")

  def inscreverGenero(self,genero):
    self._inscrever_desinscreverG(self.generosFavorito, genero, "inscrever")
    
  def desinscreverGenero(self,genero):
    self._inscrever_desinscreverG(self.generosFavorito, genero, "desinscrever")

  def inscreverAtor(self,ator):
    self._inscrever_desinscreverA(self.atoresFavorito, ator, "inscrever")
    
  def desinscreverAtor(self,ator):
    self._inscrever_desinscreverA(self.atoresFavorito, ator, "desinscrever")
    
  def inscreverDiretor(self,diretor):
    self._inscrever_desinscreverD(self.diretoresFavorito, diretor, "inscrever")
    
  def desinscreverDiretor(self,diretor):
    self._inscrever_desinscreverD(self.diretoresFavorito, diretor, "desinscrever")
    
  def inscreverProdutora(self,produtora):
    self._inscrever_desinscreverP(self.produtorasFavorito, produtora, "inscrever")
    
  def desinscreverProdutora(self,produtora):
    self._inscrever_desinscreverP(self.produtorasFavorito, produtora, "desinscrever")
    
  def inscreverCinema(self,empresa):
    self._inscrever_desinscreverC(self.cinemasFavorito, empresa, "inscrever")
    
  def desinscreverCinema(self,empresa):
    self._inscrever_desinscreverC(self.cinemasFavorito, empresa, "desinscrever")
  
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

  def __str__(self):  
      return f"Nome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}\nIdioma: {self.idioma}\nIdade: {self.idade}\nLocalização: {self.localizacao}\nLista de filmes favoritos: {self.filmesFavorito}\nLista de gêneros favoritos: {self.generosFavorito}\nLista de atores favoritos: {self.atoresFavorito}\nLista de diretores favoritos: {self.diretoresFavorito}\nLista de produtoras favoritas: {self.produtorasFavorito}\nLista de cinemas favoritos: {self.cinemasFavorito}"
