sia_url         = 'https://siabog.unal.edu.co/academia/apoyo-administrativo/mis-estudiantes/'
jsessionid      = '06616586AF5E9C2B910FD8C677966090'
sia_hist_acad   = 'historia-academica.do'
sia_dato_pers   = 'datos-personales.do'
headers_sia     = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def get_sia_url(sia_modifier, dni_per):
    return sia_url \
          + sia_modifier + ';jsessionid=' \
          + jsessionid \
          + '.websia1?documento=' \
          + str(dni_per)

def get_sia_url_login():
    return 'https://siabog.unal.edu.co/academia/inicio/do-login'