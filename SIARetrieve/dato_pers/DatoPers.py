from SIARetrieve.sia_parser.DatoPersParser import DatoPersParser

class DatoPers:
    def __init__(self, dato_pers):
        self.parser = DatoPersParser(dato_pers)
        self.calculate()
    
    def calculate(self):
        self.calculate_proc()
        self.calculate_resi()
        self.calculate_naci()
        self.calculate_siad()
        self.calculate_salu()
        self.calculate_hist_acad()

    def calculate_proc(self):
        self.proc = {}
        self.proc['dire']   = self.parser.get_proc_dir()
        self.proc['muni']   = self.parser.get_proc_muni()
        self.proc['pais']   = self.parser.get_proc_pais()
        self.proc['tel1']   = self.parser.get_proc_tel1()
        self.proc['tel2']   = self.parser.get_proc_tel2()
        self.proc['depa']   = self.parser.get_proc_depa()

    def calculate_resi(self):
        self.resi = {}
        self.resi['dire']   = self.parser.get_resi_dir()
        self.resi['muni']   = self.parser.get_resi_muni()
        self.resi['pais']   = self.parser.get_resi_pais()
        self.resi['tel1']   = self.parser.get_resi_tel1()
        self.resi['tel2']   = self.parser.get_resi_tel2()
        self.resi['depa']   = self.parser.get_resi_depa()

    def calculate_naci(self):
        self.naci           = {}
        self.naci['dire']   = None
        self.naci['muni']   = None
        self.naci['pais']   = None
        self.naci['tel1']   = None
        self.naci['tel2']   = None
        self.naci['tido']   = None
        self.naci['depa']   = None

    def calculate_siad(self):
        self.siad           = {}
        self.siad['user']   = None
        self.siad['mai1']   = None
        self.siad['mai2']   = None

    def calculate_salu(self):
        self.salu           = {}
        self.salu['gs']     = None
        self.salu['rh']     = None
        self.salu['eps']    = None

    def calculate_hist_acad(self):
        self.hist_acad     = {}
            