class Cliente:
    def __init__(self, nome, email, senha, telefone, idiona):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__telefone = telefone
        self.__idioma = idioma

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
   
    @property
    def telefone(self):
        return self.__telefone
   
    @telefone.setter
    def (self, telefone):
        self.__telefone = telefone 
   
    @property
    def idioma(self):
        return self.__idioma
    
    @idioma.setter
    def idioma(self, idioma):
        self.__idioma = idioma


