from ..sia_parser.MateParser import MateParser


class Materia:
    def __init__(self, materia):
        self.parser = MateParser(materia)
        self.nombre = self.parser.get_asig_nombre()
        self.creditos = self.parser.get_asig_creditos()
