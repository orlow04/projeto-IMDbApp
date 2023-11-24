class Cliente:
    def __init__(self, nome, email, senha, telefone, idiona):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._telefone = telefone
        self._idioma = idioma

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
   
    @property
    def telefone(self):
        return self._telefone
   
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone 
   
    @property
    def idioma(self):
        return self._idioma
    
    @idioma.setter
    def idioma(self, idioma):
        self._idioma = idioma
