import ssl
import urllib.request
import requests
import os
import re
from SIARetrieve import SIAInfo

def data_validator(post_data):
    if not(post_data is None):
        post_data = urllib.parse.urlencode(post_data).encode('ascii'),
    return post_data

def build_request(url, data, headers):
    req = urllib.request.Request(url,data,headers)
    return req

def build_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def make_request(sia_modifier, dni_per, post_data):
    url         = SIAInfo.get_sia_url(sia_modifier, dni_per)
    post_data   = data_validator(post_data)
    req         = build_request(url, post_data, SIAInfo.headers_sia)
    ctx         = build_context()
    return str(urllib.request.urlopen(req, context=ctx).read())

def get_login_ans(user, passw):
    url         = SIAInfo.get_sia_url_login()
    post_data   = data_validator({'nombre' : user, 'password' : passw})
    req         = build_request(url, post_data, SIAInfo.headers_sia)
    ctx         = build_context()
    return str(urllib.request.urlopen(req, context=ctx).read())

def set_jsessionid():
    login_ans = get_login_ans(os.environ['SIAUSER'], os.environ['SIAPASS'])
    match = re.search('[0-9|A-Z]*.web', str(login_ans))
    if match is None:
        SIAInfo.jsessionid = ''
    else:
        SIAInfo.jsessionid = login_ans[match.start() : match.end()-4]

set_jsessionid()