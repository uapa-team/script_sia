class Resumen:

    def __init__(self, PA, PAPA, infocreditos):
        self.PA = PA
        self.PAPA = PAPA
        self.infocreditos = infocreditos

    def __str__(self):
        string = self.PA + "\n"
        string += self.PAPA + "\n"
        for i in self.infocreditos:
            string += i + ": "
            string += str(self.infocreditos[i]) + "\n"

        return string

