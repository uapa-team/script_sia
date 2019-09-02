class Resumen:

    #llaves contiene las claves que debe tener infocreditos y la cantidad de datos que deben tener asociados
    __llaves = {}
    __llaves["Exigidos"]   = ["---"]*9
    __llaves["Aprobados"]  = ["---"]*9
    __llaves["Pendientes"] = ["---"]*9
    __llaves["Cursados"]   = ["---"]*9
    __llaves["Inscritos"]  = ["---"]*9
    __llaves["Créditos adicionales"] = ["---"]
    __llaves["Cupo de créditos"] = ["---"]
    __llaves["Créditos disponibles"] = ["---"]
    __llaves["Créditos estudio doble titulación"] = ["---"]
    __llaves["Total Créditos Excedentes"] = ["---"]
    __llaves["Total de Créditos Cancelados en los Periodos Cursados"] = ["---"]

    def __init__(self, dni, programa, PA, PAPA, porc, infocreditos):
        self.dni = dni
        self.programa = programa
        self.PA = PA
        self.PAPA = PAPA
        self.porc = porc
        self.infocreditos = infocreditos

        self.fill_infocreditos()

    #Completa los campos no existentes con "---" (respecto a los campos de resumen de Pregrado)
    def fill_infocreditos(self):
        for k in Resumen.__llaves:
            try:
                for _ in range(len(self.infocreditos[k]), len(Resumen.__llaves[k])):
                    if type(self.infocreditos[k]) == list:
                        self.infocreditos[k].append("---")
            except KeyError:
                self.infocreditos[k] = Resumen.__llaves[k]
            except Exception:
                self.infocreditos[k] = "---"


    def __str__(self):
        string = self.dni + "\t" + self.programa + "\t" + self.PA + "\t" + self.PAPA + "\t" + self.porc + "\t"
        for i in self.infocreditos:
            for d in self.infocreditos[i]:
                string += d + "\t"

        return string + "\n"
