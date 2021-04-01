import sys

from PyQt5.QtWidgets import QApplication

from client import Cliente
from parametros import p
'''
from interfaces.sala_de_juego import VentanaSalaJuego
from interfaces_back_end.tablero import Tablero
if __name__ == "__main__":
    app = QApplication([])
    # ventana_sala_espera = VentanaSalaEspera((600, 500))
    # ventana_sala_espera.show()
    ventana_sala_juego = VentanaSalaJuego((1300, 900))
    ventana_sala_juego.tablero = Tablero()
    ventana_sala_juego.generar_tablero()
    ventana_sala_juego.show()
    sys.exit(app.exec_())

'''

if __name__ == "__main__":

    app = QApplication([])

    # Se instancia el Cliente.
    cliente = Cliente(p.HOST, p.PORT)

    # Se inicia la app de PyQt.
    sys.exit(app.exec_())
