import sys
import os

from PyQt5.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication
)
from PyQt5.QtGui import QPixmap

from parametros import p


class VentanaFinPartida(QWidget):

    def __init__(self, size):
        super().__init__()
        self.size = size  # tuple
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('Fin de DCColonos')
        self.setMinimumSize(*self.size)
        self.setStyleSheet('background-color: brown')

        vbox = QVBoxLayout()

        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(os.path.join(*tuple(p.LOGO_SOL_RUTA))))
        self.logo.setMaximumSize(p.LOGO_SOL_SIZE[0]/2, p.LOGO_SOL_SIZE[1]/2)
        self.logo.setScaledContents(True)

        hbox_jugadores = QHBoxLayout()
        vbox_izq = QVBoxLayout()
        self.label_resultados = QLabel('Resultados:', self)
        self.label_resultados.setStyleSheet('color: gold; font-size: 30px')
        self.label_ha_ganado = QLabel('', self)
        self.label_ha_ganado.setStyleSheet('color: gold')
        vbox_izq.addWidget(self.label_resultados)
        vbox_izq.addWidget(self.label_ha_ganado)

        vbox_jugadores = QVBoxLayout()
        self.lista_labels_jugadores = []
        for i in range(p.MAX_JUGADORES_PARTIDA):
            label_jugador = QLabel('', self)
            label_jugador.setObjectName(str(i))
            label_jugador.setStyleSheet('color: goldenrod')
            self.lista_labels_jugadores.append(label_jugador)
            vbox_jugadores.addWidget(label_jugador)
        
        hbox_jugadores.addLayout(vbox_izq)
        hbox_jugadores.addLayout(vbox_jugadores)
 
        vbox.addWidget(self.logo)
        vbox.addLayout(hbox_jugadores)
        self.setLayout(vbox)

    def mostrar_puntajes(self, ha_ganado, lista_puntajes):
        if ha_ganado:
            text_gano = 'Haz Ganado!!'
        else:
            text_gano = 'Haz Perdido :('
        self.label_ha_ganado.setText(text_gano)

        print('label', len(self.lista_labels_jugadores))
        print('jug', len(lista_puntajes))
        for i in range(len(lista_puntajes)):
            text = f'{i+1}. {lista_puntajes[i]["nombre"]}: {lista_puntajes[i]["puntos"]} pts.'
            self.lista_labels_jugadores[i].setText(text)


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaSalaEspera((1500, 600))
    sys.exit(app.exec_())
    
