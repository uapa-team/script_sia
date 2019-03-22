import re


#documento_programa_map = {1013678335: 2549}

documentos = [

]


documento_programa_map = {}
documentos_programa_expediente = {}
documento_periodo_map = {}
documento_edad_map = {}
documento_nodo_map = {}
documento_tipo_acceso_map = {}
documento_tipo_subacceso_map = {}1013600424
documento_correo_map = {}

def get_expediente_programa(documento, historia_academica):
    get_expediente_programa1(documento, historia_academica)
    return get_expediente_programa2(documento, historia_academica)

def get_expediente_programa1(documento, historia_academica):
    match_string = 'plan=[0-9A-Z]*'
    match = re.search(match_string, historia_academica)
    plan = historia_academica[match.start() +5:match.end()]
    match_string = 'expediente=[0-9A-Z]*'
    match = re.search(match_string, historia_academica)
    expediente = historia_academica[match.start() + 11:match.end()]
    documentos_programa_expediente[documento] = []
    documentos_programa_expediente[documento].append([plan, expediente])

def get_expediente_programa2(documento, historia_academica):
    match_string = str("doSubmitSelectorPlanes..'([0-9A-Z]*).....([0-9A-Z]*)")
    omit = False
    match = re.finditer(match_string, historia_academica)
    for ma in match:
        omit = not omit
        if omit:
            continue
        #match_string1 = "'[A-Z0-9]*'"
        #match1 = re.finditer(match_string1, historia_academica[ma.start():ma.end()])
        #print(ma.group(1) + " " + ma.group(2))
        #for i in match1:
        #    print(i)
        plan = ma.group(1)
        expediente = ma.group(2)
        documentos_programa_expediente[documento].append([plan, expediente])
    return documentos_programa_expediente





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

def get_porcentaje(historia_academica):
    match_string = '<table class="progreso-porcentaje" border="0" cellspacing="0" cellpadding="0" width="'
    match = re.search(match_string, historia_academica)
    if(match is None):
        return '0.0%'
    return historia_academica[match.end(): match.end() + 5]


def get_last_periodo(historia_academica):
    match_string = 'academico\">[0-9|"\-"|"I"]+'
    match = re.search(match_string, historia_academica)
    #print(match)
    return historia_academica[match.start() + 11 : match.end()]


def main():
    for documento in documentos:
        jsessionid = 'DD6DEE09DB92FC240DB1536DA1DBCF9A'

        historia_academica = get_historia_academica(jsessionid, documento)
        programa_expediente = get_expediente_programa(documento, historia_academica)

        for dupla in programa_expediente.get(documento):
            if(dupla[0] == '2703'):
                historia_academica = get_historia_academica_post(dupla[0], dupla[1], documento, jsessionid)
                print(documento, end = '\t')
                print(dupla[0], end = '\t')
                print(dupla[1], end = '\t')
                print(get_porcentaje(historia_academica), end = '\t')
                print(get_last_periodo(historia_academica), end = '')
                print()


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
