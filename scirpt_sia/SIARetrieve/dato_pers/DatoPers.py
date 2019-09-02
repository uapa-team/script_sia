from ..sia_parser.DatoPersParser import DatoPersParser


class DatoPers:
    def __init__(self, dato_pers):
        self.parser = DatoPersParser(dato_pers)
        self.data = {}
        self.ha = {}

        self.calculate()

    def __str__(self):
        string = ""
        for dic in self.data:
            for dato in self.data[dic]:
                string += self.data[dic][dato] + "\t"
        
        return string + "\n"

    def get_hist_acad(self):
        string = ""
        for historia in self.ha:
            string += self.data["gen"]["dni"] + "\t" + historia + "\t"
            for dato in self.ha[historia]:
                string += self.ha[historia][dato] + "\t"
            string += "\n"
        
        return string
    
    def calculate(self):
        self.calculate_gen()
        self.calculate_proc()
        self.calculate_resi()
        self.calculate_naci()
        self.calculate_mili()
        self.calculate_siad()
        self.calculate_salu()
        self.calculate_hist_acad()

    def calculate_gen(self):
        gen = {}
        gen['dni']     = self.parser.get_dni()
        gen['name']    = self.parser.get_name()
        gen['sexo']    = self.parser.get_sexo()
        gen['edad']    = self.parser.get_edad()
        gen['est_civ'] = self.parser.get_estado_civil()
        gen['pais']    = self.parser.get_pais()
        
        self.data["gen"] = gen

    def calculate_proc(self):
        proc = {}
        proc['dire'] = self.parser.get_proc_dir()
        proc['tipo_dom'] = self.parser.get_tipo_dom()
        proc['muni'] = self.parser.get_proc_muni()
        proc['depa'] = self.parser.get_proc_depa()
        proc['pais'] = self.parser.get_proc_pais()
        proc['tel1'] = self.parser.get_proc_tel1()
        proc['tel2'] = self.parser.get_proc_tel2()
        
        self.data["proc"] = proc

    def calculate_resi(self):
        resi = {}
        resi['dire']   = self.parser.get_resi_dir()
        resi['muni']   = self.parser.get_resi_muni()
        resi['depa']   = self.parser.get_resi_depa()
        resi['pais']   = self.parser.get_resi_pais()
        resi['tel1']   = self.parser.get_resi_tel1()
        resi['tel2']   = self.parser.get_resi_tel2()

        self.data["resi"] = resi

    def calculate_naci(self):
        naci = {}
        naci['fecha']  = self.parser.get_naci_fecha()
        naci['muni']   = self.parser.get_naci_muni()
        naci['depa']   = self.parser.get_naci_depa()
        naci['pais']   = self.parser.get_naci_pais()
        naci['nacionalidad'] = self.parser.get_nacionalidad()

        self.data["naci"] = naci

    def calculate_mili(self):
        mili = {}
        mili['numero']      = self.parser.get_mili_numero()
        mili['clase']       = self.parser.get_mili_clase()
        mili['distri']      = self.parser.get_mili_distri()
        mili['situacion']   = self.parser.get_mili_situacion()

        self.data["mili"] = mili

    def calculate_siad(self):
        siad = {}
        siad['user']   = self.parser.get_usuario()
        siad['mai1']   = self.parser.get_correo_unal()
        siad['mai2']   = self.parser.get_correo_alterno()

        self.data["siad"] = siad

    def calculate_salu(self):
        salu = {}
        salu['gs']     = self.parser.get_grupo_sanguineo()
        salu['rh']     = self.parser.get_rh()
        salu['eps']    = self.parser.get_eps()

        self.data["salu"] = salu

    def calculate_hist_acad(self):
        self.ha  = self.parser.get_ha()
