from SIARetrieve.sia_parser.HistAcadParser import HistAcadParser
from SIARetrieve.hist_acad.Periodo import Periodo
from SIARetrieve.hist_acad.Materia import Materia

class HistAcad:
    def __init__(self, hist_acad):
        self.parser = HistAcadParser(hist_acad)
        self.programa = self.parser.get_programa()
        self.historias = self.parser.get_historias()
        self.periodos = []

        self.calculate()
    
    def calculate(self):
        infoJSON = self.parser.get_info() 
        for periodo in infoJSON:
            P = Periodo(periodo)
            self.periodos.append(P)

            for materia in infoJSON[periodo]:
                M = Materia(materia, infoJSON[periodo][materia][0], infoJSON[periodo][materia][1], infoJSON[periodo][materia][2], infoJSON[periodo][materia][3])
                P.materias.append(M)