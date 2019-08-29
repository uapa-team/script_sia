from .Parser import Parser
import re


class SubjectSchedule:
    def __init__(self, code, group, name, schedule, class_room, professor, credits):
        self.code = code
        self.group = group
        self.name = name
        self.schedule = schedule
        self.class_room = class_room
        self.professor = professor
        self.credits = credits


class ScheduleParser(Parser):
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
        self.data = [i.text for i in self.html.find_all(valign="top")]

    def get_subjects(self):
        #match = re.search("([0-9]+[.B]* - [0-9]*)", str(self.data))
        # return match.group()
        cod_assig = []
        for i in self.data:
            match = re.search("([0-9]+(\W\w)?\s\W\s[0-9]+)", str(i))
            try:
                cod_assig.append(match.group())
            except:
                pass
        return cod_assig
