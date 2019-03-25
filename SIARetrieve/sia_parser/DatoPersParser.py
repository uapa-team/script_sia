import re

class DatoPersParser:

    def __init__(self, datos_per):
        self.raw = datos_per

    def get_resi_info_size(self):
        match_string = 'Datos de Residencia.*Direcci&oacute;n.*Ciudad o Municipio.*Departamento.*Pa&iacute;s.*Tel&eacute;fono.*Tel&eacute;fono 2'
        match = re.search(match_string, self.raw)
        self.resi_info_start = match.start()
        self.resi_info_end   = match.end()
    
    def get_resi_dir(self):
        residencia_string =self.raw[self.resi_info_start-200:self.resi_info_end+200]
        match_string = 'Direcci&oacute;n<br>..</span><span class="cuerpo" style="font-size: 11px;">[0-9A-Za-z"&""\-"";""\."" "]*<br>'
        match = re.search(match_string, residencia_string)
        return residencia_string[match.start()+75:match.end()-4]
    
    def get_resi_muni(self):
        residencia_string =self.raw[self.resi_info_start-200:self.resi_info_end+200]
        match_string = 'Ciudad o Municipio<br>..</span><span class="cuerpo" style="font-size: 11px;">[0-9A-Za-z"&""\-"";""\."" "]*<br>'
        match = re.search(match_string, residencia_string)
        return residencia_string[match.start()+77:match.end()-4]
        
    def get_resi_pais(self):
        residencia_string =self.raw[self.resi_info_start-200:self.resi_info_end+200]
        match_string = 'Pa&iacute;s<br>..</span><span class="cuerpo" style="font-size: 11px;">[0-9A-Za-z"&""\-"";""\."" "]*<br>'
        match = re.search(match_string, residencia_string)
        return residencia_string[match.start()+70:match.end()-4]

    def get_resi_tel1(self):
        residencia_string =self.raw[self.resi_info_start-200:self.resi_info_end+200]
        match_string = 'Tel&eacute;fono 1<br>..</span><span class="cuerpo" style="font-size: 11px;">[0-9A-Za-z"&""\-"";""\."" "]*<br>'
        match = re.search(match_string, residencia_string)
        return residencia_string[match.start()+76:match.end()-4]

    def get_resi_tel2(self):
        residencia_string =self.raw[self.resi_info_start-200:self.resi_info_end+200]
        match_string = 'Tel&eacute;fono 2<br>..</span><span class="cuerpo" style="font-size: 11px;">[0-9A-Za-z"&""\-"";""\."" "]*<'
        match = re.search(match_string, residencia_string)
        return residencia_string[match.start()+76:match.end()-4]

    def get_resi_depa(self):
        residencia_string =self.raw[self.resi_info_start-200:self.resi_info_end+200]
        match_string = 'Departamento<br>..</span><span class="cuerpo" style="font-size: 11px;">[0-9A-Za-z"&""\-"";""\."" "]*<br>'
        match = re.search(match_string, residencia_string)
        return residencia_string[match.start()+71:match.end()-4]
