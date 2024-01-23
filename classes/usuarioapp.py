#Classe Usuário App: Pendente
from filme import Filme
from cliente import Cliente
from genero import Genero
from ator import Ator
from diretor import Diretor
from produtora import Produtora
from empresa import Empresa

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
              lista.append(objeto.titulo)
              lista.append(objeto.duracao)
              lista.append(objeto.ano)
              lista.append(objeto.classificacaoEtaria)
              lista.append(objeto.sinopse)
              lista.append(objeto.notaIMDB)
              lista.append(objeto.premio)
              print(f"{objeto.titulo} foi adicionado na lista de favoritos")
          elif objeto in lista and acao == "desinscrever":
              lista.remove(objeto.titulo)
              lista.remove(objeto.duracao)
              lista.remove(objeto.ano)
              lista.remove(objeto.classificacaoEtaria)
              lista.remove(objeto.sinopse)
              lista.remove(objeto.notaIMDB)
              lista.remove(objeto.premio)
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
            lista.append(objeto.tipo)
            print(f"{objeto.tipo} foi adicionado na lista de favoritos")
        elif objeto in lista and acao == "desinscrever":
            lista.remove(objeto.tipo)
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
            lista.append(objeto.nome)
            lista.append(objeto.idade)
            lista.append(objeto.personagem)
            lista.append(objeto.outroTrabalhos)
            lista.append(objeto.biografia)
            lista.append(objeto.premio)
            print(f"{objeto.nome} foi adicionado na lista de favoritos")
        elif objeto in lista and acao == "desinscrever":
            lista.remove(objeto.nome)
            lista.remove(objeto.idade)
            lista.remove(objeto.personagem)
            lista.remove(objeto.outroTrabalhos)
            lista.remove(objeto.biografia)
            lista.remove(objeto.premio)
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
              lista.append(objeto.nome)
              lista.append(objeto.idade)
              lista.append(objeto.outrosTrabalhos)
              lista.append(objeto.biografia)
              lista.append(objeto.premio)
              print(f"{objeto.nome} foi adicionado na lista de favoritos")
          elif objeto in lista and acao == "desinscrever":
              lista.remove(objeto.nome)
              lista.remove(objeto.idade)
              lista.remove(objeto.outrosTrabalhos)
              lista.remove(objeto.biografia)
              lista.remove(objeto.premio)
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
              lista.append(objeto.nome)
              lista.append(objeto.sede)
              lista.append(objeto.dono)
              lista.append(objeto.endereco)
              print(f"{objeto.nome} foi adicionado na lista de favoritos")
          elif objeto in lista and acao == "desinscrever":
              lista.remove(objeto.nome)
              lista.remove(objeto.sede)
              lista.remove(objeto.dono)
              lista.remove(objeto.endereco)
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
            lista.append(objeto.nome)
            lista.append(objeto.cnpj)
            lista.append(objeto.cep)
            lista.append(objeto.numero)
            lista.append(objeto.complemento)
            print(f"{objeto.nome} foi adicionado na lista de favoritos")
        elif objeto in lista and acao == "desinscrever":
            lista.remove(objeto.nome)
            lista.remove(objeto.cnpj)
            lista.remove(objeto.cep)
            lista.remove(objeto.numero)
            lista.remove(objeto.complemento)
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
  
user = usuarioApp("João","joao@gmail.com","123456","(11) 99999-9999","Português",18,"São Paulo")
filme = Filme("Vingadores: Ultimato",2019,"Ação","3h 2m","12 anos","https://www.youtube.com/watch?v=6ZfuNTqbHE8","https://www.themoviedb.org/t/p/w600_and_h900_bestv2/q6725aR8Zs4IwGMXzZT8aC8lh41.jpg")
genero = Genero("Ação")
ator = Ator("Robert Downey Jr.", 55,"Tony Stark / Homem de Ferro","https://www.themoviedb.org/t/p/w600_and_h900_bestv2/5qHNjhtjMD4YWH3UP0rm4tKwxCL.jpg","https://www.themoviedb.org/person/3223-robert-downey-jr","sem oscars")
diretor = Diretor("Anthony Russo", 50,"https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8CuuNIKMzMUL1NKOPv9AqEwM7og.jpg","https://www.themoviedb.org/person/19271-anthony-russo","sem oscars")
produtora = Produtora("Marvel Studios","USA","https://www.themoviedb.org/t/p/w600_and_h900_bestv2/86B8qZpAKyw0jZMHCV1qUEcxl9r.jpg","https://www.themoviedb.org/company/420")
empresa = Empresa("Cinemark","00.000.000/0000-00","Av. Paulista" ,1234,"São Paulo")
user.inscreverFilme(filme)
user.inscreverGenero(genero)
user.inscreverAtor(ator)
user.inscreverDiretor(diretor)
user.inscreverProdutora(produtora)
user.inscreverCinema(empresa)
print(user)