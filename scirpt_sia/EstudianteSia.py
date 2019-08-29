from .SIARetrieve import sia


class EstudianteSia:

    def __init__(self, dni):
        self.dni = dni

        self.dp = sia.get_dp_per(self.dni)
        self.ha = []
        self.summary = []
        self.academic = []
        self.percentage = []
        self.schedule = []
        self.table_resume = []
        self.__get_all_ha()

    def __get_all_ha(self):
        self.ha.append(sia.get_ha_per(self.dni))
        self.summary.append(sia.get_ha_per(
            self.dni).parser.get_resumen()['PA'])
        self.academic.append(sia.get_ha_per(self.dni).periodos)
        self.percentage.append(sia.get_ha_per(
            self.dni).parser.get_resumen()['%'])
        self.schedule.append(sia.get_schedule(self.dni).parser.get_subjects())
        creds_aux = sia.get_ha_per(
            self.dni).parser.get_resumen()['creditos']
        if creds_aux == {}:
            self.table_resume.append({})
        else:
            self.table_resume.append(creds_aux['Aprobados'])

        for h in self.ha[0].historias:
            self.ha.append(sia.get_ha_prog(h[0], h[1], self.dni))
            self.summary.append(sia.get_ha_prog(
                h[0], h[1], self.dni).parser.get_resumen()['PA'])
            self.academic.append(sia.get_ha_prog(
                h[0], h[1], self.dni).periodos)
            self.percentage.append(sia.get_ha_prog(
                h[0], h[1], self.dni).parser.get_resumen()['%'])
            self.schedule.append(sia.get_schedule_prog(
                h[0], h[1], self.dni).parser.get_subjects())
            creds_aux = sia.get_ha_prog(
                h[0], h[1], self.dni).parser.get_resumen()['creditos']
            if creds_aux == {}:
                self.table_resume.append({})
            else:
                self.table_resume.append(creds_aux['Aprobados'])
