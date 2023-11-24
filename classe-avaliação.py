
class Avaliacao:   
    def __init__(self, nota, comentario):
        self._nota = nota
        self._comentario = comentario
        self._filme = None
        self._usuarioApp = None  

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, comentario):
        self._comentario = comentario

    @property
    def filme(self):
        return self._filme

    @filme.setter
    def filme(self, filme):
        self._filme = filme

    @property
    def usuarioApp(self):
        return self._usuarioApp

    @usuarioApp.setter
    def usuarioApp(self, usuarioApp):
        self._usuarioApp = usuarioApp
