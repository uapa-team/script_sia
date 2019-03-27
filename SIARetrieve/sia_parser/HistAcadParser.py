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
        