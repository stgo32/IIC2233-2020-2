import sys
import os

from PyQt5.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication, QPushButton
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

from parametros import p


class VentanaSalaEspera(QWidget):

    senal_abrir_chat = pyqtSignal()

    def __init__(self, size):
        super().__init__()
        self.size = size  # tuple
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('Sala de Espera DCColonos')
        self.setMinimumSize(*self.size)
        self.setStyleSheet('background-color: brown')

        vbox = QVBoxLayout()

        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(os.path.join(*tuple(p.LOGO_SOL_RUTA))))
        self.logo.setMaximumSize(p.LOGO_SOL_SIZE[0]/2, p.LOGO_SOL_SIZE[1]/2)
        self.logo.setScaledContents(True)

        hbox_jugadores = QHBoxLayout()
        vbox_izq = QVBoxLayout()
        self.label_conectados = QLabel('Jugadores Conectados:               ', self)
        self.label_conectados.setStyleSheet('color: gold')

        self.boton_chat = QPushButton('Abrir Chat', self)
        self.boton_chat.setEnabled(True)
        self.boton_chat.setMaximumWidth(150)
        self.boton_chat.clicked.connect(self.senal_abrir_chat)

        vbox_jugadores = QVBoxLayout()
        self.lista_labels_jugadores = []
        for i in range(p.MAX_JUGADORES_PARTIDA):
            label_jugador = QLabel('', self)
            label_jugador.setObjectName(str(i))
            label_jugador.setStyleSheet('color: goldenrod')
            self.lista_labels_jugadores.append(label_jugador)
            vbox_jugadores.addWidget(label_jugador)
        
        vbox_izq.addWidget(self.label_conectados)
        vbox_izq.addWidget(self.boton_chat)
        hbox_jugadores.addLayout(vbox_izq)
        hbox_jugadores.addLayout(vbox_jugadores)
 
        vbox.addWidget(self.logo)
        vbox.addLayout(hbox_jugadores)
        self.setLayout(vbox)

    def agregar_jugador(self, nombre, ide):
        self.lista_labels_jugadores[ide].setText(nombre)

    def eliminar_jugador(self, ide):
        self.lista_labels_jugadores[ide].setText('Esperando...')




if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaSalaEspera((1500, 600))
    sys.exit(app.exec_())
    
