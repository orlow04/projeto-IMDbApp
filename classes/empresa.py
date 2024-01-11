#Classe Empres: +/- Ok
class Empresa:
    def __init__(self, nome, cnpj, cep, numero, complemento, franquia=False):
        self._nome = nome
        self._cnpj = cnpj
        self._franquia = franquia
        self._cep = cep
        self._numero = numero
        self._complemento = complemento
        
        self._proprietario = None
        self._ingresso = None

    def associarProprietario(self, proprietario):
        self._proprietario = proprietario.nome
    
    def verificarIngressoVendido(self):
        if self._ingresso is not None:
            return self._ingresso.get_vendido()
        else:
            return False

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, complemento):
        self._complemento = complemento

    @property
    def franquia(self):
        return self._franquia

    @franquia.setter
    def franquia(self, franquia):
        self._franquia = franquia
    
    def __str__(self):
        return f"Nome: {self._nome}\nCNPJ: {self._cnpj}\nCEP: {self._cep}\nNúmero: {self._numero}\nComplemento: {self._complemento}\nFranquia: {self._franquia}\nProprietário: {self._proprietario}\nIngresso: {self._ingresso}"
