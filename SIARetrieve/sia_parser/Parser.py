from bs4 import BeautifulSoup


# Es la super clase que parsea los html recibidos en las peticiones hechas
class Parser:

    # Es el constructor que utiliza la librería BeautifulSoup para parsear el html
    # recibe raw, que es el html
    # lxml es el lenguaje con el que se está parseando las respuestas del sia
    def __init__(self, raw):
        self.html = BeautifulSoup(raw, features="lxml")
        self.raw = raw
