
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
