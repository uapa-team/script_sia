import urllib.request
import ssl
import re

#documentos = [676282, 1034312454, 1032504867, 1015483888, 1019153887, 1022444458, 1022422960, 1010247857, 1072675255, 1022446697, 1023978203, 1054094756, 1022446491, 1019150906, 1015483594, 1013676197, 1090532516, 1013690465, 1018514802, 1023972837, 1019150623, 1034314393, 1032507009, 1014307450, 1032506771, 1032506797, 1015484315, 1014302980, 1118576430, 1233893557, 1019153159, 1013688452, 1015477927, 1026599210, 1026598270, 1018495753, 1233896908, 1051955701, 1030699723, 1057413298, 1033815640, 1032504342, 1053617187, 1032502876, 1032508406, 1023977495, 1019153307, 1032505241, 1020844346, 1023970694, 1020843548, 1026600420, 1013691373, 1233909519, 1032506510, 1015484224, 1000514224, 1020843708, 1019153302, 1026303986, 1014308663, 1032508994, 1118576135, 1032508849, 1015474730, 1016112197, 1015483283, 1019146749, 1032487380, 1014309208, 1032506705, 1030700200, 1032506760, 1016112381, 1032508359, 1136889517, 1014309186, 1019153786, 1032495165, 1026306378, 1087213009, 1020845289, 1121873797, 1087007236, 1032507639, 1016112584, 1072673395, 1032493901, 1020843703, 1031182122]
#documento_programa_map = {1013678335: 2549}

documentos = [

]


documento_programa_map = {}

documento_periodo_map = {}
documento_edad_map = {}
documento_nodo_map = {}
documento_tipo_acceso_map = {}
documento_tipo_subacceso_map = {}
documento_correo_map = {}


def make_req(sia_modifier, jsessionid, documento):
    url = 'https://siabog.unal.edu.co/academia/apoyo-administrativo/mis-estudiantes/' \
          + sia_modifier + ';jsessionid=' \
          + jsessionid \
          + '.websia1?documento=' \
          + str(documento)

    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    req.set_proxy('proxy4.unal.edu.co:8080', 'http')

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return str(urllib.request.urlopen(req, context=ctx).read())


def get_datos_personales(jsessionid, documento):
    return make_req('datos-personales.do', jsessionid, documento)


def get_historia_academica(jsessionid, documento):
    return make_req('historia-academica.do', jsessionid, documento)


def get_periodo_ingreso(datos_personales, programa):
    match_string = str(programa)
    match = re.search(match_string, datos_personales)
    start_programa = int(match.end())
    match_string = str(programa) + '.*<td><span class="titulo-2">Periodo de ingreso<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">'
    match = re.search(match_string, datos_personales[0:start_programa + 700])
    start = int(match.end())
    match_string = str(
        programa) + '.*<td><span class="titulo-2">Periodo de ingreso<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">[0-9]*-[I]*'
    match = re.search(match_string, datos_personales[0:start_programa + 700])
    end = int(match.end())
    return datos_personales[start:end]


def get_edad_actual(datos_personales):
    match_string = 'a&ntilde;os'
    match = re.search(match_string, datos_personales)
    start = int(match.start())
    return datos_personales[start - 3:start]


def get_nodo_inicio(historia_academica):
    match_string = '.*<span class="titulo-causa-bloqueo">'
    match = re.search(match_string, historia_academica)
    start = int(match.end())
    match_string = '.*<span class="titulo-causa-bloqueo">[a-z | " " | "&" | ";" | "\-"]+\[[0-9]*'
    match = re.search(match_string, historia_academica)
    end = int(match.end())
    return historia_academica[start:end+1]


def get_tipo_acceso(datos_personales, programa):
    match_string = str(
        programa) + '.*</span></td><td><span class="titulo-2">Tipo de ingreso<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">'
    match = re.search(match_string, datos_personales)
    start = int(match.end())
    match_string = str(
        programa) + '.*</span></td><td><span class="titulo-2">Tipo de ingreso<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">[a-z | "&" | ";"]*<'
    match = re.search(match_string, datos_personales)
    end = int(match.end()) - 1
    return datos_personales[start:end]


def get_tipo_subacceso(datos_personales, programa):
    match_string = str(
        programa) + '.*</span></td><td><span class="titulo-2">Tipo de ingreso<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">[a-z | "&" | ";"]*<br>'
    match = re.search(match_string, datos_personales)
    start = int(match.end())
    match_string = str(
        programa) + '.*</span></td><td><span class="titulo-2">Tipo de ingreso<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">[a-z | "&" | ";"]*<br>[a-z | "&" | ";"]*<'
    match = re.search(match_string, datos_personales)
    end = int(match.end()) - 1
    return datos_personales[start:end]


def get_correo_oficial(datos_personales):
    match_string = '</span></td><td width="50%"><span class="titulo-2">Correo oficial<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">'
    match = re.search(match_string, datos_personales)
    start = int(match.end())
    match_string = '</span></td><td width="50%"><span class="titulo-2">Correo oficial<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">[a-z | "@" | "."]*'
    match = re.search(match_string, datos_personales)
    end = int(match.end())
    return datos_personales[start:end]

def get_exists(datos_personales):
    match_string = 'EL DOCUMENTO ESPECIFICADO NO EXISTE'
    match = re.search(match_string, datos_personales)
    return match == None

def get_vio_materia(historia_academica, materia):
    match_string = materia
    match = re.search(match_string, historia_academica)
    return match != None

def get_correo_alterno(datos_personales):
    match_string = '<td colspan="2"><span class="titulo-2">Correo alterno<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">'
    match = re.search(match_string, datos_personales)
    start = int(match.end())
    match_string = '<td colspan="2"><span class="titulo-2">Correo alterno<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">[a-z | "@" | "."]*'
    end = int(match.end())
    return datos_personales[start:end]

def get_genero(datos_personales):
    match_string = 'masculino'
    if re.search(match_string,datos_personales) == None:
        return 'F'
    else:
        return 'M'

def get_fecha_nacimiento(datos_personales):
    match_string = '<td width="50%"><span class="titulo-2">Fecha<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">'
    match = re.search(match_string, datos_personales)
    start = int(match.end())
    match_string = '<td width="50%"><span class="titulo-2">Fecha<br>[^\n]n</span><span class="cuerpo" style="font-size: 11px;">[0-9 | "/" ]*'
    match = re.search(match_string, datos_personales)
    end = int(match.end())
    return datos_personales[start:end]

def get_telefono1(datos_personales):
    match_string = 'Datos de Residencia'
    match = re.search(match_string, datos_personales)
    start_string = int(match.end())
    match_string = '<td><span class="titulo-2">Tel&eacute;fono 1<br>'
    match = re.search(match_string, datos_personales[start_string:start_string + 1000])
    start = int(match.end()) + start_string
    match_string = 'span class="cuerpo" style="font-size: 11px;">[0-9]*'
    match = re.search(match_string, datos_personales[start:start_string + 1000])
    end = int(match.end()) + start
    return datos_personales[start + 55:end]

def get_telefono2(datos_personales):
    match_string = 'Datos de Residencia'
    match = re.search(match_string, datos_personales)
    start_string = int(match.end())
    match_string = '<td><span class="titulo-2">Tel&eacute;fono 2<br>'
    match = re.search(match_string, datos_personales[start_string:start_string + 1000])
    start = int(match.end()) + start_string
    match_string = 'span class="cuerpo" style="font-size: 11px;">[0-9]*'
    match = re.search(match_string, datos_personales[start:start_string + 1000])
    end = int(match.end()) + start
    return datos_personales[start + 55:end]

def get_direccion(datos_personales):
    match_string = 'Datos de Residencia'
    match = re.search(match_string, datos_personales)
    start_string = int(match.end())
    match_string = '<td width="50%"><span class="titulo-2">Direcci&oacute;n<br>'
    match = re.search(match_string, datos_personales[start_string:start_string + 800])
    start = int(match.end()) + start_string
    match_string = '</span><span class="cuerpo" style="font-size: 11px;">["&" | ";" | a-z | 0-9 |"\." | "\#" | "\-"]*'
    match = re.search(match_string, datos_personales[start:start_string + 800])
    end = int(match.end()) + start
    return datos_personales[start + 55:end]

def get_departamento_nacimiento(datos_personales):
    match_string = 'Datos de Nacimiento'
    match = re.search(match_string, datos_personales)
    start_string = int(match.end())
    match_string = '<td><span class="titulo-2">Departamento<br>'
    match = re.search(match_string, datos_personales[start_string:start_string+800])
    start = int(match.end()) + start_string
    match_string = '<span class="cuerpo" style="font-size: 11px;">[a-z | 0-9 |"\."]*'
    match = re.search(match_string, datos_personales[start:start_string+800])
    end = int(match.end()) + start
    return datos_personales[start + 55:end]

def get_ciudad_nacimiento(datos_personales):
    match_string = 'Datos de Nacimiento'
    match = re.search(match_string, datos_personales)
    start_string = int(match.end())
    match_string = '</span></td><td width="50%"><span class="titulo-2">Ciudad<br>'
    match = re.search(match_string, datos_personales[start_string:start_string + 800])
    start = int(match.end()) + start_string
    match_string = '<span class="cuerpo" style="font-size: 11px;">[a-z | 0-9 |"\."]*'
    match = re.search(match_string, datos_personales[start:start_string + 800])
    end = int(match.end()) + start
    return datos_personales[start + 55:end]

def get_ciudad_residencia(datos_personales):
    match_string = 'Datos de Residencia'
    match = re.search(match_string, datos_personales)
    start_string = int(match.end())
    match_string = 'Ciudad'
    match = re.search(match_string, datos_personales[start_string:start_string + 800])
    start = int(match.end()) + start_string
    match_string = '<span class="cuerpo" style="font-size: 11px;">[a-z | 0-9 |"\."]*'
    match = re.search(match_string, datos_personales[start:start_string + 800])
    end = int(match.end()) + start
    return datos_personales[start + 71:end]

def get_ciudad_procedencia(datos_personales):
    match_string = 'Datos de Procedencia'
    match = re.search(match_string, datos_personales)
    start_string = int(match.end())
    match_string = 'Ciudad'
    match = re.search(match_string, datos_personales[start_string:start_string + 800])
    start = int(match.end()) + start_string
    match_string = '<span class="cuerpo" style="font-size: 11px;">[a-z | 0-9 |"\."]*'
    match = re.search(match_string, datos_personales[start:start_string + 800])
    end = int(match.end()) + start
    return datos_personales[start + 71:end]


def main():
    for documento in documentos:
        #print(documento)
        jsessionid = 'D98C76CBB0209F9E1F3A9B92F753C14E'

        #historia_academica = get_historia_academica(jsessionid, documento, documento_programa_map[documento])

        #historia_academica = get_historia_academica(jsessionid, documento)

        #documento_periodo_map[documento] = get_periodo_ingreso(datos_personales, documento_programa_map[documento])

        #documento_edad_map[documento] = get_edad_actual(datos_personales)

        #documento_nodo_map[documento] = get_nodo_inicio(historia_academica)

        #documento_tipo_acceso_map[documento] = get_tipo_acceso(datos_personales, documento_programa_map[documento])

        #documento_tipo_subacceso_map[documento] = get_tipo_subacceso(datos_personales,
        #                                                            documento_programa_map[documento])

        #documento_correo_map[documento] = get_correo_oficial(datos_personales)
        # print(str(documento) + ";" + str(documento_programa_map[documento]) + ";" +
        #        str(documento_periodo_map[documento]) + ";" +
        #        str(documento_nodo_map[documento]) + ";" +
        #        str(documento_edad_map[documento]) + ";")



main()
