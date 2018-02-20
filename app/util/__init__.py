__author__ = 'poseidon'
import logging
import random
from random import randint
from decimal import Decimal
from datetime import datetime, date, time as timee
import time
from pytz import timezone
import pytz


def logger_util(name_app):
    l = logging.getLogger(name_app)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] - %(message)s')
    ch.setFormatter(formatter)
    l.addHandler(ch)
    return l


logger = logger_util('app')


def utc_to_local(utc_datetime):
    fmt = '%d-%m-%Y'
    local_tz = pytz.timezone("America/Lima")
    local_dt = utc_datetime.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt).strftime(fmt)


def utc_to_local2(utc_datetime, zone_name):
    fmt = '%d-%m-%Y'
    local_tz = pytz.timezone(zone_name)
    local_dt = utc_datetime.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt).strftime(fmt)


def get_time(fecha, zone_name):
    time_zone = timezone(zone_name)
    return fecha.astimezone(time_zone).strftime("%I:%M %p")

#####Antiguos


def get_fecha_estandar(cadena):
    formato = '%d/%m/%Y'
    return datetime.strptime(cadena, formato)


def fecha_local(fecha):
    utc = pytz.utc
    fmt = '%d-%m-%Y'
    lima = pytz.timezone("America/Lima")

    dt = datetime.strptime(fecha, fmt)
    am_dt = lima.localize(dt)
    fecha_final = am_dt.astimezone(utc).strftime(fmt)
    return fecha_final


def code_generator(size):
        return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(size))


def random_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def sqla_parse_list(mylist):

    lista = []
    for o in mylist:
        a = {}
        for c in o.__dict__.items():
            if c[0] != '_sa_instance_state':
                attr = getattr(o, c[0])
                if isinstance(attr, Decimal):
                    a[c[0]] = float(attr)
                elif isinstance(attr, datetime):
                    a[c[0]] = time.mktime(attr.timetuple())
                elif isinstance(attr, date):
                    # a[c[0]] = time.mktime(attr.timetuple())
                    fecha = time.mktime(attr.timetuple())
                    a[c[0]] = str(fecha).replace(".", "00")
                elif isinstance(attr, timee):
                    a[c[0]] = attr.isoformat()
                else:
                    a[c[0]] = attr

        lista.append(a)

    return lista


def sqla_parse_object(o):
    a = {}
    for c in o.__dict__.items():
        if c[0] != '_sa_instance_state':
                attr = getattr(o, c[0])
                if isinstance(attr, Decimal):
                    a[c[0]] = float(attr)
                elif isinstance(attr, datetime):
                    # a[c[0]] = time.mktime(attr.timetuple())
                    fecha = time.mktime(attr.timetuple())
                    a[c[0]] = str(fecha).replace(".", "00")
                else:
                    a[c[0]] = attr

    return a




