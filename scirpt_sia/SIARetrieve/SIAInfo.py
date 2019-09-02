# Es la parte de la url que no va a cambiar a lo largo del programa
sia_url         = 'https://siabog.unal.edu.co/academia/apoyo-administrativo/mis-estudiantes/'
# Es el token único de la sesión del SIA
jsessionid      = '06616586AF5E9C2B910FD8C677966090'
# Cadena que representa en la url la petición que se quiere hacer,
# es decir si se quiere ver la historia académica o los datos personales
sia_hist_acad   = 'historia-academica.do'
sia_dato_pers   = 'datos-personales.do'
sia_schedule    = 'horario.do'
# Son los headers que avisan al SIA que versión AppleWebKit se está usando
# para que el SIA piense que la petición se está haciendo desde un navegador y no desde una consola
headers_sia     = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/35.0.1916.47 Safari/537.36'}


# Constructor de la url a la que se le va a hacer la petición al SIA
# sia_modifier puede ser sia_hist_acad o sia_dato_pers y dni_per es el dni de la persona a consultar
# retorna la url de la petición
def get_sia_url(sia_modifier, dni_per):
    return sia_url \
          + sia_modifier + ';jsessionid=' \
          + jsessionid \
          + '.websia1?documento=' \
          + str(dni_per)


def get_sia_url_mat(cod_mat):
    return 'https://siabog.unal.edu.co/academia/apoyo-administrativo/ConsultaContenidos.do?action=Info&idAsignatura=' \
           + str(cod_mat) + \
           '&idSession_hd=&txtIdAsignatura=&txtNombreAsignatura='


# Función que devuelve la url con la que se hace la petición para sacar el jsessionid
def get_sia_url_login():
    return 'https://siabog.unal.edu.co/academia/inicio/do-login'
