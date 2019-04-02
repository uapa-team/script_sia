from SIARetrieve import sia

class Persona:

    def __init__(self, dni):
        self.dni = dni

        self.dp = sia.get_dp_per(self.dni)
        self.ha = []

        self.__get_all_ha()


    def __get_all_ha(self):
        self.ha.append(sia.get_ha_per(self.dni))

        for h in self.ha[0].historias:
            self.ha.append(sia.get_ha_prog(h[0], h[1], self.dni))