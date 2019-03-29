from SIARetrieve.sia_parser.Parser import Parser
import re

class HistAcadParser(Parser):
    
    def __init__(self, ha):
        Parser.__init__(self, ha)
        self.raw = ha


    def get_programa(self):
        match_string = 'plan=[0-9A-Z]*'
        match = re.search(match_string, self.raw)
        return self.raw[match.start() +5:match.end()]
        

    def get_expediente(self):
        match_string = 'expediente=[0-9A-Z]*'
        match = re.search(match_string, self.raw)
        return self.raw[match.start() + 11:match.end()]

    def get_historias(self):
        historias = []
        match_string = str("doSubmitSelectorPlanes..'([0-9A-Z]*).....([0-9A-Z]*)")
        omit = False
        match = re.finditer(match_string, self.raw)
        
        if match is None:
            match = []

        for ma in match:
            omit = not omit
            if omit:
                continue
            plan = ma.group(1)
            expediente = ma.group(2)
            historias.append([plan, expediente])
        return historias

    def get_info(self):
        periodoJSON = {}

        periodos = self.html.find_all(class_="periodo-academico")
        notas = self.html.find_all(id="calificaciones")

        for i in range(len(periodos)):
            periodoJSON[periodos[i].text] = {}
            data = notas[i].find_all("tr")
            data = data[1:]
            for j in data:
                subdata = j.find_all("span")
                periodoJSON[periodos[i].text][subdata[0].text] = [subdata[1].text, subdata[5].text, subdata[6].text, subdata[9].text]

        return periodoJSON

    def get_resumen(self):
        resumen = {}

        res = self.html.find(id="resumen-academico")

        promedios = res.find_all(class_="total-grande")
        resumen["PA"] = promedios[0].text[1:4]
        resumen["PAPA"] = promedios[1].text[1:4]
        resumen["%"] = res.find(class_="texto-porcentaje").text[0:-1]

        filas_creditos = self.find_coincidence(res.find_all("tr"), "lft")[1:]
        resumen["creditos"] = {}
        for f in filas_creditos:
            data = f.find_all("td")
            if len(data) == 3:
                resumen["creditos"][data[0].text] = data[1].text
            else:
                resumen["creditos"][data[0].text] = [d.text for d in data[1:]]
                

        data = res.find_all(class_="total2")[5:7]
        resumen["creditos"]["Total Créditos Excedentes"] = data[0].text
        resumen["creditos"]["Total de Créditos Cancelados en los Periodos Cursados"] = data[1].text

        return resumen

    #Toma un arreglo de datos extraidos con bs4.find_all()
    #y retorna solo las que contengan almenos una etiqueta con clase @_class
    def find_coincidence(self, src, class_):
        result = []

        for i in src:
            if i.find(class_=class_):
                result.append(i)

        return result
