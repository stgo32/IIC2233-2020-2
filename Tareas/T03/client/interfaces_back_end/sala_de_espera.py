from PyQt5.QtCore import pyqtSignal, QObject


class BackSalaEspera(QObject):

    senal_agregar_jugador = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()

    def agregar_jugador(self, lista_jugadores):
        for jugador in lista_jugadores:
            nombre = jugador.nombre
            ide = jugador.id
            self.senal_agregar_jugador.emit(nombre, ide)

