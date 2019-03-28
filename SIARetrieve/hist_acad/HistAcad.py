from SIARetrieve.sia_parser.HistAcadParser import HistAcadParser

class HistAcad:
    def __init__(self, hist_acad):
        self.parser = HistAcadParser(hist_acad)
        self.programa = self.parser.get_programa()
        self.historias = self.parser.get_historias()
        self.periodos = []

        self.calculate()
    
    def calculate(self):
        JSON = self.parser.get_info() 
        for i in JSON:
            print(i)
            for j in JSON[i]:
                print(j + " " + str(JSON[i][j]))