
class Avaliacao:
    def __init__(self,filme,usuarioApp):
        self.__filme = None
        self.__usuarioApp = None    
    
    def __init__(self, nota, comentario):
        self.__nota = nota
        self.__comentario = comentario

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def comentario(self):
        return self.__comentario

    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario


    @property
    def filme(self):
        return self.__filme

    @filme.setter
    def filme(self, filme):
        self.__filme = filme


    @property
    def usuarioApp(self):
        return self.__usuarioApp

    @usuarioApp.setter
    def usuarioApp(self, usuarioApp):
        self.__usuarioApp = usuarioApp

