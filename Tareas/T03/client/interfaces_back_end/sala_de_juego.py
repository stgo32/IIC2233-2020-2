from random import randint

from PyQt5.QtCore import pyqtSignal, QObject


class BackSalaJuego(QObject):

    senal_dados_lanzados = pyqtSignal(int, int)
    senal_actuar = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()

    def lanzar_dados(self):
        dado_izq = randint(1, 6)
        dado_der = randint(1, 6)
        self.senal_dados_lanzados.emit(dado_izq, dado_der)
        self.senal_actuar.emit(dado_izq, dado_der)
