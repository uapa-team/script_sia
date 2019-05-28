from ..sia_parser.HorarioParser import HorarioParser


class Horario:
    def __init__(self, horario):
        self.parser = HorarioParser(horario)
        self.data = {}
        self.horario = {}
        self.parser.get_asignaturas()
