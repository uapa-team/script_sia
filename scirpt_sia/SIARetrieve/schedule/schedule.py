from ..sia_parser.ScheduleParser import ScheduleParser


class Schedule:
    def __init__(self, horario):
        self.parser = ScheduleParser(horario)
        self.data = {}
        self.schedule = {}
        self.parser.get_subjects()
