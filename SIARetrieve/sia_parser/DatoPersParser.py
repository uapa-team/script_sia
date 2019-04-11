from .Parser import Parser


# DatoPersParser es una clase, hija de Parser
class DatoPersParser(Parser):

    # Es el constructor donde se parsea el html recibido al hacer la petición de los datos académicos
    # recibe ha que es el html de la historia academica
    def __init__(self, datos_per):
        Parser.__init__(self, datos_per)
        # En el arreglo datos se guardan todas las etiquetas cuya clase se llame titulo-2
        # en este arreglo se quiere guardar todos los titulos de los datos personales de la persona
        # ej: Ciudad o municipio, País, Telefono
        self.titulos = [i.text for i in self.html.find_all(class_="titulo-2")]
        # En el arreglo datos se guardan todas las etiquetas cuya clase se llame cuerpo
        # en este arreglo se quiere guardar todos los valores de los datos personales de la persona
        # ej: Bogota d.c, Colombia, 1234567
        self.data = [i.text for i in self.html.find_all(class_="cuerpo")]

    # Este método devuelve el dni
    def get_dni(self):
        return self.data[0].split('\\')[0]

    # Este método devuelve el sexo
    def get_sexo(self):
        return self.data[1].split('\\')[0]

    # Este método devuelve la edad
    def get_edad(self):
        return self.data[2].split(' ')[0]

    # Este método devuelve el estado civil
    def get_estado_civil(self):
        return self.data[3].split('\\')[0]

    # Este método devuelve el pais de su nacionalidad
    def get_pais(self):
        return self.data[4].split('\\')[0]

    # Este método devuelve la dirección de procedencia
    def get_proc_dir(self):
        return self.data[5].split('\\')[0]

    # Este método devuelve el tipo de domicilio, ej: urbano
    def get_tipo_dom(self):
        return self.data[6].split('\\')[0]

    # Este método devuelve el municipio de procedencia
    def get_proc_muni(self):
        return self.data[7].split('\\')[0]

    # Este método devuelve el departamento de procedencia
    def get_proc_depa(self):
        return self.data[8].split('\\')[0]

    # Este método devuelve el país de procedencia
    def get_proc_pais(self):
        return self.data[9].split('\\')[0]

    # Este método devuelve el teléfono de la dirección de residencia
    def get_proc_tel1(self):
        return self.data[10].split('\\')[0]

    # Este método devuelve el otro teléfono de la dirección de residencia
    def get_proc_tel2(self):
        return self.data[11].split('\\')[0]

    # Este método devuelve la dirección de residencia
    def get_resi_dir(self):
        return self.data[12].split('\\')[0]

    # Este método devuelve el municipio de residencia
    def get_resi_muni(self):
        return self.data[13].split('\\')[0]

    # Este método devuelve el departamento de residencia
    def get_resi_depa(self):
        return self.data[14].split('\\')[0]

    # Este método devuelve el país de residencia
    def get_resi_pais(self):
        return self.data[15].split('\\')[0]

    # Este método devuelve el teléfono de residencia
    def get_resi_tel1(self):
        return self.data[16].split('\\')[0]

    # Este método devuelve otro teléfono de residencia
    def get_resi_tel2(self):
        return self.data[17].split('\\')[0]

    # Este método devuelve la fecha de nacimiento
    def get_naci_fecha(self):
        return self.data[18].split('\\')[0]

    # Este método devuelve el municipio de nacimiento
    def get_naci_muni(self):
        return self.data[19].split('\\')[0]

    # Este método devuelve el departamento de nacimiento
    def get_naci_depa(self):
        return self.data[20].split('\\')[0]

    # Este método devuelve el país de nacimiento
    def get_naci_pais(self):
        return self.data[21].split('\\')[0]

    # Este método devuelve el país de la nacionalidad
    def get_nacionalidad(self):
        return self.data[22].split('\\')[0]

    # Este método devuelve el número de la libreta militar
    def get_mili_numero(self):
        return self.data[23].split('\\')[0]

    # Este método devuelve la clase de la libreta militar
    def get_mili_clase(self):
        return self.data[24].split('\\')[0]

    # Este método devuelve el distrito militar
    def get_mili_distri(self):
        return self.data[25].split('\\')[0]

    # Este método devuelve la situación en cuanto a la libreta militar
    def get_mili_situacion(self):
        return self.data[26].split('\\')[0]

    # Este método devuelve el usuario del sia
    def get_usuario(self):
        return self.data[27].split('\\')[0]

    # Este método devuelve el correo de la unal
    def get_correo_unal(self):
        return self.data[28].split('\\')[0]

    # Este método devuelve un correo alterno
    def get_correo_alterno(self):
        return self.data[29].split('\\')[0]

    # Este método devuelve el grupo sanguíneo
    def get_grupo_sanguineo(self):
        return self.data[30].split('\\')[0]

    # Este método devuelve el rh
    def get_rh(self):
        return self.data[31].split('\\')[0]

    # Este método devuelve la eps
    def get_eps(self):
        return self.data[32].split('\\')[0]

    def get_ha(self):
        subdata = self.data[33:]
        ha = {}
        for i in range(0, len(subdata), 6):
            programa = subdata[i+1].split('\\')[0]
            codigo_p = programa.split(" | ")[0]
            ha[codigo_p] = {}
            ha[codigo_p]["estado"]      = subdata[i].split('\\')[0]
            ha[codigo_p]["programa"]    = programa
            ha[codigo_p]["nivel"]       = subdata[i+2].split('\\')[0]
            ha[codigo_p]["codigo"]      = subdata[i+3].split('\\')[0]
            ha[codigo_p]["p_ingreso"]   = subdata[i+4].split('\\')[0]
            ha[codigo_p]["t_ingreso"]   = subdata[i+5].split('\\')[0]

        return ha
