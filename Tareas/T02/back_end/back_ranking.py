from PyQt5.QtCore import QObject, pyqtSignal

from parametros import RUTA_RANKING, PUNTAJES_A_MOSTRAR


class bRanking(QObject):

    senal_enviar_ranking = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        
    def calcular_ranking(self):
        with open(RUTA_RANKING, 'rt') as archivo:
            data = archivo.readlines()
        lista_datos = []
        for fila in data:
            fila = fila.split(",")
            if "\n" in fila[1]:
                fila[1] = fila[1][:-1]
            lista_datos.append(fila)
        lista_datos.sort(key=lambda x: int(x[1]), reverse=True)
        puntajes = {}
        if len(lista_datos) < PUNTAJES_A_MOSTRAR:
            puntajes_a_mostrar = len(lista_datos)
        else:
            puntajes_a_mostrar = PUNTAJES_A_MOSTRAR
        for i in range(puntajes_a_mostrar):
            puntajes[lista_datos[i][0]] = lista_datos[i][1]
        archivo.close()
        self.senal_enviar_ranking.emit(puntajes)

