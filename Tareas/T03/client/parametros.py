import json
import os


def hook(dic):
    return dic


def cargar_parametros(ruta):
    with open(ruta, 'rt') as archivo:
        parametros = json.load(archivo, object_hook=hook)
    return parametros


class Parametros():

    def __init__(self, ruta):
        parametros = cargar_parametros(ruta)
        self.__dict__ = parametros


p = Parametros(os.path.join('parametros.json'))