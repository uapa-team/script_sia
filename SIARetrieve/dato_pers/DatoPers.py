class DatoPers:
    def __init__(self, dato_pers):
        self.raw            = dato_pers
        self.calculate()
    
    def calculate(self):
        self.calculate_resi()
        self.calculate_naci()
        self.calculate_siad()
        self.calculate_salu()
        self.calculate_hist_acad()

    def calculate_resi(self):
        self.resi = {}
        self.resi['dire']   = None
        self.resi['muni']   = None
        self.resi['pais']   = None
        self.resi['tel1']   = None
        self.resi['tel2']   = None
        self.resi['tido']   = None
        self.resi['depa']   = None

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
            