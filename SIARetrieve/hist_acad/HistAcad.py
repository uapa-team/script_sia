from ..sia_parser.HistAcadParser import HistAcadParser
from .Periodo import Periodo
from .Materia import Materia
from .Resumen import Resumen

class HistAcad:
    def __init__(self, hist_acad):
        self.parser = HistAcadParser(hist_acad)
        self.programa = self.parser.get_programa()
        self.historias = self.parser.get_historias()
        self.periodos = []

        self.calculate()


    def calculate(self):
        self.calculate_ha()
        self.calculate_resumen()
    
    def calculate_ha(self):
        infoJSON = self.parser.get_info() 
        for periodo in infoJSON:
            P = Periodo(periodo)
            self.periodos.append(P)

            for materia in infoJSON[periodo]:
                M = Materia(materia, infoJSON[periodo][materia][0], infoJSON[periodo][materia][1], infoJSON[periodo][materia][2], infoJSON[periodo][materia][3])
                P.materias.append(M)

    def calculate_resumen(self):
        infoJSON = self.parser.get_resumen()
        self.resumen = Resumen(infoJSON["PA"], infoJSON["PAPA"], infoJSON["creditos"])

        #TODO: Crear las llaves de creditos sin valor por --- 
