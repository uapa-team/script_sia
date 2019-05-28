import os
import ssl
import urllib.request
from . import SIAInfo
from .sia_parser.SiaData import SiaData


# Recibe post_data que es un diccionario con el Form Data necesario para hacer la petición
# este diccionario se convierte en un json usando la codificación ascii
# lo hace utilizando la función parse.urlencode de la libreria urllib
# se verifica que post_data no sea None
def data_validator(post_data):
    if not(post_data is None):
        post_data = urllib.parse.urlencode(post_data).encode('ascii')
    return post_data


# Construye la petición, recibe una url, un Form Data y unos headers
# retorna un objeto url request
def build_request(url, data, headers):
    req = urllib.request.Request(url, data, headers)
    return req


# Construye un contexto ssl que ignora el hostname y no establece ningún certificado ssl
# retorna el contexto ssl
def build_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


# En esta función se hace la request, añadiendo el contexto
# retorna un string con la respuesta de la petición, la respuesta es un html
def make_request(sia_modifier, dni_per, post_data):
    url         = SIAInfo.get_sia_url(sia_modifier, dni_per)
    post_data   = data_validator(post_data)
    req         = build_request(url, post_data, SIAInfo.headers_sia)
    ctx         = build_context()
    return str(urllib.request.urlopen(req, context=ctx).read())


def make_request_mat(cod_materia):
    url         = SIAInfo.get_sia_url_mat(cod_materia)
    req = build_request(url, None, SIAInfo.headers_sia)
    ctx = build_context()
    return str(urllib.request.urlopen(req, context=ctx).read())


# En esta función se hace la petición para obtener el html que contiene el jsessionid
# recibe el usuario del sia y la contraseña
# retorna un string con la respuesta de la petición, la respuesta es un html
def get_login_ans(user, passw):
    url         = SIAInfo.get_sia_url_login()
    post_data   = data_validator({'nombre' : user, 'password' : passw})
    req         = build_request(url, post_data, SIAInfo.headers_sia)
    ctx         = build_context()
    return str(urllib.request.urlopen(req, context=ctx).read())


# Establece en SIAInfo el jsessionid que se va a usar
# utiliza las variables de ambiente SIAUSER y SIAPASS que son el usuario del sia y la contraseña respectivamente
def set_jsessionid():
    login_ans = get_login_ans(os.environ['SIAUSER'], os.environ['SIAPASS'])
    SIAInfo.jsessionid = SiaData.get_jsessionid(login_ans)


# Se invoca esta funcion cada que se importa NetworkUtils
set_jsessionid()
