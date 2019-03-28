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


            return resumen