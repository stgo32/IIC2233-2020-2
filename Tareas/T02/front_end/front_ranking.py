import sys
sys.path.append('..')

from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout, QApplication
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from T02.parametros import (MAX_WIDTH_BOTON_RANKING, SET_GEO_BOTON_RANKING, PUFFLE_SET_GEO,
                            CANTIDAD_PUNTAJES_RANKING, RUTA_PUFFLE_CELESTE)


class fRanking(QWidget):

    senal_mostrar_ranking = pyqtSignal(dict)
    senal_volver_inicio = pyqtSignal()

    def __init__(self, min_size):
        super().__init__()
        self.min_size = min_size  # tuple
        self.senal_mostrar_ranking.connect(self.actualizar_ranking)
        self.vbox_list = [QLabel('') for i in range(CANTIDAD_PUNTAJES_RANKING)]
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('Ranking DCCumbia')
        self.setMinimumWidth(self.min_size[0])
        self.setMinimumHeight(self.min_size[1])

        self.label = QLabel('Ranking de puntajes:', self)
        self.label.setObjectName('labelRanking')
        self.vbox_label = QVBoxLayout

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        for label in self.vbox_list:
            label.setObjectName('_labelPuntaje')
            self.vbox.addWidget(label)

        self.boton_volver_inicio = QPushButton('Volver a Inicio', self)
        self.boton_volver_inicio.setMaximumWidth(MAX_WIDTH_BOTON_RANKING)
        self.boton_volver_inicio.clicked.connect(self.volver_a_inicio)
        self.boton_volver_inicio.setGeometry(*SET_GEO_BOTON_RANKING)
        self.boton_volver_inicio.setMaximumWidth(MAX_WIDTH_BOTON_RANKING)
        self.boton_volver_inicio.show()

        self.puffle = QLabel(self)
        self.puffle.setPixmap(QPixmap(RUTA_PUFFLE_CELESTE))
        self.puffle.setGeometry(*PUFFLE_SET_GEO)
        self.puffle.setScaledContents(True)

        self.setLayout(self.vbox)

    def volver_a_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()

    def actualizar_ranking(self, ranking):
        i = 0
        for puntaje in ranking:
            self.vbox_list[i].setText(f'{i + 1}. {puntaje}: {ranking[puntaje]}')
            i += 1
        self.vbox.addStretch(1)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    punt = {'ppp': 50, 'dadad': 100}
    ventana = fRanking((500, 500))
    ventana.show()
    sys.exit(app.exec_())
