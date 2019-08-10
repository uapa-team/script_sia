from .Parser import Parser


# DatoPersParser es una clase, hija de Parser
class DatoPersParser(Parser):

    # Es el constructor donde se parsea el html recibido al hacer la petición de los datos académicos
    # recibe ha que es el html de la historia academica
    def __init__(self, datos_per):
        Parser.__init__(self, datos_per)
        
        self.calculate_gen()
        self.calculate_proc()
        self.calculate_resi()
        self.calculate_naci()
        self.calculate_mili()
        self.calculate_siad()
        self.calculate_salu()
        self.calculate_ha()

    def calculate_gen(self): 
        try:
            self.gen = [i.text.split('\\')[0] for i in self.html.find(id="id-persona").find_all(class_="cuerpo")]
        except AttributeError:
            self.gen = []

    def calculate_proc(self):
        try:
            self.proc = [i.text.split('\\')[0] for i in self.html.find(id="procedencia").find_all(class_="cuerpo")]
        except AttributeError:
            self.proc = []

    def calculate_resi(self):
        try:
            self.resi = [i.text.split('\\')[0] for i in self.html.find(id="residencia").find_all(class_="cuerpo")]
        except AttributeError:
            self.resi = []

    def calculate_naci(self):
        try:
            self.naci = [i.text.split('\\')[0] for i in self.html.find(id="nacimiento").find_all(class_="cuerpo")]
        except AttributeError:
            self.naci = []

    def calculate_mili(self):
        try:
            self.mili = [i.text.split('\\')[0] for i in self.html.find(id="libreta").find_all(class_="cuerpo")]
        except AttributeError:
            self.mili = []

    def calculate_siad(self):
        try:
            self.siad = [i.text.split('\\')[0] for i in self.html.find(id="acceso").find_all(class_="cuerpo")]
        except AttributeError:
            self.siad = []

    def calculate_salu(self):
        try:
            self.salu = [i.text.split('\\')[0] for i in self.html.find(id="salud").find_all(class_="cuerpo")]
        except AttributeError:
            self.salu = []


    # Este método calcula el diccionario con las diferentes historias academicas del estudiante
    def calculate_ha(self):
        data = self.html.find(id="academicos").find_all(id="dato")
        self.hist_acad = {}
        for ha in data:
            subdata = [i.text.split('\\')[0] for i in ha.find_all(class_="cuerpo")]
            programa = subdata[1].split(" | ")[0]

            self.hist_acad[programa] = {}
            self.hist_acad[programa]["estado"]      = subdata[0]
            self.hist_acad[programa]["programa"]    = subdata[1]
            self.hist_acad[programa]["nivel"]       = subdata[2]
            self.hist_acad[programa]["codigo"]      = subdata[3]
            self.hist_acad[programa]["p_ingreso"]   = subdata[4]
            self.hist_acad[programa]["t_ingreso"]   = subdata[5]

    # Este método devuelve el dni
    def get_dni(self):
        try:
            return self.gen[0].split('.')[1]
        except IndexError:
            return "---"

    # Este método devuelve el nombre
    def get_name(self):
        try:
            return self.html.find(class_="identificador").text
        except Exception:
            return "---"

    # Este método devuelve el sexo
    def get_sexo(self):
        try:    
            return self.gen[1]
        except IndexError:
            return "---"

    # Este método devuelve la edad
    def get_edad(self):
        try:    
            return self.gen[2].split(' ')[0]
        except IndexError:
            return "---"

    # Este método devuelve el estado civil
    def get_estado_civil(self):
        try:    
            return self.gen[3]
        except IndexError:
            return "---"

    # Este método devuelve el pais de su nacionalidad
    def get_pais(self):
        try:    
            return self.gen[4]
        except IndexError:
            return "---"

    # Este método devuelve la dirección de procedencia
    def get_proc_dir(self):
        try:    
            return self.proc[0]
        except IndexError:
            return "---"

    # Este método devuelve el tipo de domicilio, ej: urbano
    def get_tipo_dom(self):
        try:    
            return self.proc[1]
        except IndexError:
            return "---"

    # Este método devuelve el municipio de procedencia
    def get_proc_muni(self):
        try:    
            return self.proc[2]
        except IndexError:
            return "---"

    # Este método devuelve el departamento de procedencia
    def get_proc_depa(self):
        try:    
            return self.proc[3]
        except IndexError:
            return "---"

    # Este método devuelve el país de procedencia
    def get_proc_pais(self):
        try:    
            return self.proc[4]
        except IndexError:
            return "---"

    # Este método devuelve el teléfono de la dirección de residencia
    def get_proc_tel1(self):
        try:    
            return self.proc[5]
        except IndexError:
            return "---"

    # Este método devuelve el otro teléfono de la dirección de residencia
    def get_proc_tel2(self):
        try:    
            return self.proc[6]
        except IndexError:
            return "---"

    # Este método devuelve la dirección de residencia
    def get_resi_dir(self):
        try:    
            return self.resi[0]
        except IndexError:
            return "---"

    # Este método devuelve el municipio de residencia
    def get_resi_muni(self):
        try:    
            return self.resi[1]
        except IndexError:
            return "---"

    # Este método devuelve el departamento de residencia
    def get_resi_depa(self):
        try:    
            return self.resi[2]
        except IndexError:
            return "---"

    # Este método devuelve el país de residencia
    def get_resi_pais(self):
        try:    
            return self.resi[3]
        except IndexError:
            return "---"

    # Este método devuelve el teléfono de residencia
    def get_resi_tel1(self):
        try:    
            return self.resi[4]
        except IndexError:
            return "---"

    # Este método devuelve otro teléfono de residencia
    def get_resi_tel2(self):
        try:    
            return self.resi[5]
        except IndexError:
            return "---"

    # Este método devuelve la fecha de nacimiento
    def get_naci_fecha(self):
        try:    
            return self.naci[0]
        except IndexError:
            return "---"

    # Este método devuelve el municipio de nacimiento
    def get_naci_muni(self):
        try:    
            return self.naci[1]
        except IndexError:
            return "---"

    # Este método devuelve el departamento de nacimiento
    def get_naci_depa(self):
        try:    
            return self.naci[2]
        except IndexError:
            return "---"

    # Este método devuelve el país de nacimiento
    def get_naci_pais(self):
        try:    
            return self.naci[3]
        except IndexError:
            return "---"

    # Este método devuelve el país de la nacionalidad
    def get_nacionalidad(self):
        try:    
            return self.naci[4]
        except IndexError:
            return "---"

    # Este método devuelve el número de la libreta militar
    def get_mili_numero(self):
        try:    
            return self.mili[0]
        except IndexError:
            return "---"

    # Este método devuelve la clase de la libreta militar
    def get_mili_clase(self):
        try:    
            return self.mili[1]
        except IndexError:
            return "---"

    # Este método devuelve el distrito militar
    def get_mili_distri(self):
        try:    
            return self.mili[2]
        except IndexError:
            return "---"

    # Este método devuelve la situación en cuanto a la libreta militar
    def get_mili_situacion(self):
        try:    
            return self.mili[3]
        except IndexError:
            return "---"

    # Este método devuelve el usuario del sia
    def get_usuario(self):
        try:    
            return self.siad[0]
        except IndexError:
            return "---"

    # Este método devuelve el correo de la unal
    def get_correo_unal(self):
        try:    
            return self.siad[1]
        except IndexError:
            return "---"

    # Este método devuelve un correo alterno
    def get_correo_alterno(self):
        try:    
            return self.siad[2]
        except IndexError:
            return "---"

    # Este método devuelve el grupo sanguíneo
    def get_grupo_sanguineo(self):
        try:    
            return self.salu[0]
        except IndexError:
            return "---"

    # Este método devuelve el rh
    def get_rh(self):
        try:    
            return self.salu[1]
        except IndexError:
            return "---"

    # Este método devuelve la eps
    def get_eps(self):
        try:    
            return self.salu[2]
        except IndexError:
            return "---"

    # Este método devuelve las historias academicas
    def get_ha(self):
        return self.hist_acad
