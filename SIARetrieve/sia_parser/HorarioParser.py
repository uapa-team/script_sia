from .Parser import Parser


class HorarioParser(Parser):
    # Es el constructor donde se parsea el html recibido al hacer la petición de los datos académicos
    # recibe ha que es el html de la historia academica
    def __init__(self, datos_per):
        Parser.__init__(self, datos_per)
        # En el arreglo datos se guardan todas las etiquetas cuya clase se llame titulo-2
        # en este arreglo se quiere guardar todos los titulos de los datos personales de la persona
        # ej: Ciudad o municipio, País, Telefono
        self.titulos = [i.text for i in self.html.find_all(class_="titulo-2")]
        # En el arreglo datos se guardan todas las etiquetas cuya clase se llame cuerpo
        # en este arreglo se quiere guardar todos los valores de los datos personales de la persona
        # ej: Bogota d.c, Colombia, 1234567
        self.data = [i.text for i in self.html.find_all(class_="cuerpo")]

    def get_codigo(self):
        return self.data[0].split('\\')[0]

    def get_grupo(self):
        return self.data[0].split('\\')[0]

    def get_nombre_asignatura(self):
        return self.data[0].split('\\')[0]

    def get_horario(self):
        return self.data[0].split('\\')[0]

    def get_edif_salon(self):
        return self.data[0].split('\\')[0]

    def get_docente(self):
        return self.data[0].split('\\')[0]

    def get_creditos(self):
        return self.data[0].split('\\')[0]
