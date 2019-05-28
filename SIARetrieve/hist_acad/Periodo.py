class Periodo:
    def __init__(self, periodo):
        self.periodo = periodo
        self.materias = []

    def __str__(self):
        string = self.periodo  + "\n"
        for m in self.materias:
            string += str(m) + "\n"
        return string
