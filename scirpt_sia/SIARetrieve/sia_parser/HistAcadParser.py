import re
from .Parser import Parser


# HistAcadParser es una clase, hija de Parser
# noinspection PyMethodMayBeStatic
class HistAcadParser(Parser):
    
    # Es el constructor donde se parsea el html recibido al hacer la petición de la historia académica
    # recibe ha que es el html de la historia academica
    def __init__(self, ha):
        Parser.__init__(self, ha)

    # Esta función devuelve el plan de la persona
    # utiliza la funcion search de la librería re, se le manda lo que se quiere buscar
    # y la cadena en la que se va a buscar, que es self.raw
    # retorna el plan
    def get_programa(self):
        match = re.search('plan=[0-9A-Z]*', self.raw)
        return match.group()[5:]

    # Esta función devuelve el expediente de la persona
    # utiliza la funcion search de la librería re, se le manda lo que se quiere buscar
    # y la cadena en la que se va a buscar, que es self.raw
    # retorna el expediente
    def get_expediente(self):
        match = re.search('expediente=[0-9A-Z]*', self.raw)
        return match.group()[11:]

    # Esta función devuelve las historias académicas de la persona
    # utiliza la funcion finditer de la librería re, devuelve un arreglo con las historias. Se le manda lo que
    # se quiere buscar y la cadena en la que se va a buscar, que es self.raw
    # retorna un arreglo de historias
    def get_historias(self):
        historias = []
        omit = False
        match = re.finditer('doSubmitSelectorPlanes...([0-9A-Z]*).....([0-9A-Z]*)', self.raw)
        
        # Si match es None, convertimos mtach en una lista vacía
        # esto puede pasar cuando una persona solo tiene una historia académica
        if match is None:
            match = []
        # Por cada elemento es match se hace una iteración
        for ma in match:
            # omit se cambia de valor, ya que por cada plan sale dos veces la cadena doSubmitSelectorPlanes...
            # ([0-9A-Z]*).....([0-9A-Z]*), y solo nos interesa una de ellas
            omit = not omit
            if omit:
                continue
            plan = ma.group(1)
            expediente = ma.group(2)
            historias.append([plan, expediente])
        return historias

    # Esta función nos genera un diccionario con toda la información de las materias de los periodos académicos
    def get_info(self):
        periodoJSON = {}

        # Se usa la función find_all de la librería BeautifulSoup para que nos encuentre todas aquellas etiquetas que
        # tienen de nombre de clase "periodo_academico"
        # se genera un arreglo llamado periodos con todas las etiquetas encontradas
        periodos = self.html.find_all(class_="periodo-academico")
        # Se usa la función find_all de la librería BeautifulSoup para que nos encuentre todas aquellas etiquetas que
        # tienen id "calificaciones"
        # se genera un arreglo llamado notas con todas las etiquetas encontradas
        # nos interesa estas etiquetas ya que dentro de ese div está toda la informacion de las materias
        notas = self.html.find_all(id="calificaciones")

        # Por cada elemento en periodos se hace una iteración
        for i in range(len(periodos)):
            periodoJSON[periodos[i].text] = {}
            # En data se van a guardar todas las etiquetas tr de la posicion i en el arreglo notas
            # se quiere la informacion de estas etiquetas ya que ahi se encierra la información de las materias
            data = notas[i].find_all("tr")
            # El primer elemento no nos dice información sobre las materias por lo tanto no lo tomamos en cuenta
            data = data[1:]
            for j in data:
                # En subdata se van a guardar todas las etiquetas span dentro del elemento data en el que estamos
                # se quiere la informacion de estas etiquetas ya que ahi se encuentra la nota, la tipología, los
                # créditos etc de cada asignatura en la historia académica
                subdata = j.find_all("span")
                # Finalmente se guarda un arreglo con la información de las materias en la posición de la materia
                # respectiva en el diccionario
                # subdata[1].text = nombre de la asignatura
                # subdata[5].text = tipología de la asignatura
                # subdata[6].text = número de créditos de la asignatura
                # subdata[9].text = nota que se tuvo la materia
                # Se hace el if porque cuando subdata es de tamaño 10 es porque estamos en un programa posterior al 2008
                if len(subdata) == 10:
                    periodoJSON[periodos[i].text][subdata[0].text] = [subdata[1].text, subdata[5].text, subdata[6].text, subdata[9].text]
                else:
                    periodoJSON[periodos[i].text][subdata[0].text] = [subdata[1].text, subdata[5].text, subdata[7].text, subdata[8].text]

        return periodoJSON


    #Retorna un diccionario con los datos contenidos en el cuadro de resumen-academico
    #Los valores devueltos en creditos son todos arreglos
    def get_resumen(self):
        resumen = {}

        res = self.html.find(id="resumen-academico")

        promedios = res.find_all(class_="total-grande")
        if len(promedios) > 1:
            resumen["PA"] = promedios[0].text[1:4]
            resumen["PAPA"] = promedios[1].text[1:4] 
            resumen["%"] = res.find_all(class_="texto-porcentaje")[0].text[0:-1]
        elif len(promedios) == 1:
            resumen['PA'] = promedios[0].text[3:6]
            resumen["PAPA"] = "---" 
            resumen["%"] = "---"
        else:
            resumen["PA"] = "---"
            resumen["PAPA"] = "---" 
            resumen["%"] = "---"

        filas_creditos = self.find_coincidence(res.find_all("tr"), "lft")[1:]
        resumen["creditos"] = {}
        for f in filas_creditos:
            data = f.find_all("td")
            if len(data) == 3:
                resumen["creditos"][data[0].text] = [data[1].text]
            else:
                resumen["creditos"][data[0].text] = [d.text for d in data[1:]]

        data = res.find_all(class_="total2")[5:7]
        if len(data) > 0:
            resumen["creditos"]["Total Créditos Excedentes"] = data[0].text
            resumen["creditos"]["Total de Créditos Cancelados en los Periodos Cursados"] = data[1].text

        return resumen

    # Toma un arreglo de datos extraidos con bs4.find_all()
    # y retorna solo las que contengan almenos una etiqueta con clase @_class
    def find_coincidence(self, src, class_):
        result = []

        for i in src:
            if i.find(class_=class_):
                result.append(i)

        return result
