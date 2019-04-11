from ..sia_parser.MateParser import MateParser


class Materia:
    def __init__(self, materia):
        self.parser = MateParser(materia)
