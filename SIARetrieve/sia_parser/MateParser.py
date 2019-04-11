from .Parser import Parser


# DatoPersParser es una clase, hija de Parser
class MateParser(Parser):

    # Es el constructor donde se parsea el html recibido al hacer la petición de la información de una materia
    # recibe ha que es el html de la información de una materia
    def __init__(self, datos_per):
        Parser.__init__(self, datos_per)

