from .Parser import Parser

# DatoPersParser es una clase, hija de Parser
class MateParser(Parser):

    # Es el constructor donde se parsea el html recibido al hacer la petición de la información de una materia
    # recibe ha que es el html de la información de una materia
    def __init__(self, datos_per):
        Parser.__init__(self, datos_per)

    def get_asig_vigente(self):
        return self.html.find_all(class_="zona-dato-caja")[0].find_all('tr')[1].text.split('\\t')[14].split('\\n')[0]

    def get_asig_nombre(self):
        return self.html.find_all(class_="zona-dato-caja")[0].find_all('tr')[2].text.split('\\n')[3]

    def get_asig_creditos(self):
        return self.html.find_all(class_="zona-dato-caja")[0].find_all('tr')[6].text.split('\\n')[3]

