class Periodo:
    def __init__(self, periodo):
        self.periodo = periodo
        self.materias = []

    def __str__(self):
        string = periodo  + " "
        for m in materias:
            string += str(m) + " "
        return string