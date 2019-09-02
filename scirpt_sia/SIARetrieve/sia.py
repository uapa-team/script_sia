from . import NetworkUtils
from . import SIAInfo
from .hist_acad.HistAcad import HistAcad
from .dato_pers.DatoPers import DatoPers
from .mate_info.Materia import Materia
from .schedule.schedule import Schedule


def build_data(prog, exped):
    return {'plan': prog, 'expediente': exped}


def get_ha_prog(prog, exped, dni_per):
    post_data = build_data(prog, exped)
    hist_acad = HistAcad(NetworkUtils.make_request(SIAInfo.sia_hist_acad, dni_per, post_data), dni_per)
    return hist_acad


def get_ha_per(dni_per):
    return HistAcad(NetworkUtils.make_request(SIAInfo.sia_hist_acad, dni_per, None), dni_per)


def get_dp_per(dni_per):
    return DatoPers(NetworkUtils.make_request(SIAInfo.sia_dato_pers, dni_per, None))


def get_mat_info(cod_materia):
    return Materia(NetworkUtils.make_request_mat(cod_materia))

def get_schedule(dni_per):
    return Schedule(NetworkUtils.make_request(SIAInfo.sia_schedule, dni_per, None))

def get_schedule_prog(prog, exped, dni_per):
    post_data = build_data(prog, exped)
    return Schedule(NetworkUtils.make_request(SIAInfo.sia_schedule, dni_per, post_data))
