from SIARetrieve.sia_parser.DatoPersParser import DatoPersParser

class DatoPers:
    def __init__(self, dato_pers):
        self.parser = DatoPersParser(dato_pers)
        self.data = {}

        self.proc       = {}
        self.resi       = {}
        self.naci       = {}
        self.mili       = {}
        self.siad       = {}
        self.salu       = {}
        self.hist_acad  = {}

        self.calculate()
    
    def calculate(self):
        self.data['dni']    = self.parser.get_dni()
        self.data['sexo']   = self.parser.get_sexo()
        self.data['edad']   = self.parser.get_edad()
        self.data['est_civ'] = self.parser.get_estado_civil()
        self.data['pais']   = self.parser.get_pais()

        self.calculate_proc()
        self.calculate_resi()
        self.calculate_naci()
        self.calculate_mili()
        self.calculate_siad()
        self.calculate_salu()
        self.calculate_hist_acad()


    def calculate_proc(self):
        self.proc['dire']   = self.parser.get_proc_dir()
        self.proc['muni']   = self.parser.get_proc_muni()
        self.proc['pais']   = self.parser.get_proc_pais()
        self.proc['tel1']   = self.parser.get_proc_tel1()
        self.proc['tel2']   = self.parser.get_proc_tel2()
        self.proc['depa']   = self.parser.get_proc_depa()

    def calculate_resi(self):
        self.resi['dire']   = self.parser.get_resi_dir()
        self.resi['muni']   = self.parser.get_resi_muni()
        self.resi['pais']   = self.parser.get_resi_pais()
        self.resi['tel1']   = self.parser.get_resi_tel1()
        self.resi['tel2']   = self.parser.get_resi_tel2()
        self.resi['depa']   = self.parser.get_resi_depa()

    def calculate_naci(self):
        self.naci['fecha']  = self.parser.get_naci_fecha()
        self.naci['muni']   = self.parser.get_naci_muni()
        self.naci['depa']   = self.parser.get_naci_depa()
        self.naci['pais']   = self.parser.get_naci_pais()
        self.naci['nacionalidad'] = self.parser.get_nacionalidad()

    def calculate_mili(self):
        self.mili['numero'] = self.parser.get_mili_numero()
        self.mili['clase']  = self.parser.get_mili_clase()
        self.mili['distri'] = self.parser.get_mili_distri()
        self.mili['situacion'] = self.parser.get_mili_situacion()

    def calculate_siad(self):
        self.siad['user']   = self.parser.get_usuario()
        self.siad['mai1']   = self.parser.get_correo_unal()
        self.siad['mai2']   = self.parser.get_correo_alterno()

    def calculate_salu(self):
        self.salu['gs']     = self.parser.get_grupo_sanguineo()
        self.salu['rh']     = self.parser.get_rh()
        self.salu['eps']    = self.parser.get_eps()

    def calculate_hist_acad(self):
        #TODO: Hacer para N historias academicas
        self.hist_acad  = {}          