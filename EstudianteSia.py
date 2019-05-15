from .SIARetrieve import sia


class EstudianteSia:

    def __init__(self, dni):
        self.dni = dni

        self.dp = sia.get_dp_per(self.dni)
        self.ha = []
        self.horario = sia.get_horario(self.dni)

        self.__get_all_ha()

    def __get_all_ha(self):
        self.ha.append(sia.get_ha_per(self.dni))

        for h in self.ha[0].historias:
            self.ha.append(sia.get_ha_prog(h[0], h[1], self.dni))
