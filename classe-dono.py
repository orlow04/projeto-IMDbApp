class Cinema:
  def __init__(self,donoCinema):
    self.__donoCinema = None

  def __init__(self,empresa,endereco,idIngresso,vendas):
    self.__empresa = empresa
    self.__endereco = endereco
    self.__idIngresso = idIngresso
    self.__vendas = vendas

  @propery
  def donoCinema(self):
    return self.__donoCinema

  @donoCinema.setter
  def donoCinema(self,donoCinema):
    self.__donoCinema = donoCinema

  @propery
  def empresa(self):
    return self.__empresa

  @empresa.setter
  def empresa(self,empresa):
    self.__empresa = empresa

  @propery
  def endereco(self):
    return self.__endereco
    
  @endereco.setter
  def endereco(self,endereco):
    self.__endereco = endereco

  @propery
  def idIngresso(self):
    return self.__idIngresso

  @idIngresso.setter
  def idIngresso(self,idIngresso):
    self.__idIngresso = idIngresso

  @propery
  def vendas(self):
    return self.__vendas

  @vendas.setter
  def vendas(self,vendas):
    self.__vendas = vendas

# métodos da classe
def comprarIngresso(self, valor):

def getVendas(self):
  return self.__vendas
