from . import NetworkUtils
from . import SIAInfo
from .hist_acad.HistAcad import HistAcad
from .dato_pers.DatoPers import DatoPers

def build_data(prog, exped):
    return {'plan':prog, 'expediente':exped}

def get_ha_prog(prog, exped, dni_per):
    post_data = build_data(prog, exped)
    hist_acad = HistAcad(NetworkUtils.make_request(SIAInfo.sia_hist_acad, dni_per, post_data))
    return hist_acad

def get_ha_per(dni_per):
    return HistAcad(NetworkUtils.make_request(SIAInfo.sia_hist_acad, dni_per, None))

def get_dp_per(dni_per):
    return DatoPers(NetworkUtils.make_request(SIAInfo.sia_dato_pers, dni_per, None))