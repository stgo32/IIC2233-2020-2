import sys
sys.path.append('..')

from T02.parametros import RUTA_LOGO, LOGO_SIZE

from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QApplication,
    QErrorMessage
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class fInicio(QWidget):

    senal_calcular_ranking = pyqtSignal()
    senal_volver_de_ranking = pyqtSignal()

    senal_comenzar = pyqtSignal(str)
    senal_volver_de_juego = pyqtSignal()
    senal_volver_de_resumen = pyqtSignal()

    def __init__(self, min_size):
        super().__init__()
        self.min_size = min_size  # tuple
        self.senal_volver_de_ranking.connect(self.show)
        self.senal_volver_de_juego.connect(self.show)
        self.senal_volver_de_resumen.connect(self.show)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('Inicio DCCumbia')
        self.setMinimumWidth(self.min_size[0])
        self.setMinimumHeight(self.min_size[1])

        vbox = QVBoxLayout()

        self.logo = QLabel(self)
        self.logo.resize(LOGO_SIZE[0], LOGO_SIZE[1])
        self.logo.setPixmap(QPixmap(RUTA_LOGO))
        self.logo.setScaledContents(True)

        hbox_nombre = QHBoxLayout()
        self.label_nombre = QLabel('Ingresa tu nombre:', self)
        self.etiqueta_nombre = QLineEdit('', self)
        hbox_nombre.addWidget(self.label_nombre)
        hbox_nombre.addWidget(self.etiqueta_nombre)

        hbox_botones = QHBoxLayout()
        self.boton_comenzar = QPushButton('Comenzar', self)
        self.boton_ranking = QPushButton('Ranking de Puntajes')
        hbox_botones.addWidget(self.boton_comenzar)
        hbox_botones.addWidget(self.boton_ranking)

        self.boton_comenzar.clicked.connect(self.comenzar)
        self.boton_ranking.clicked.connect(self.mostrar_ranking)

        vbox.addWidget(self.logo)
        vbox.addLayout(hbox_nombre)
        vbox.addLayout(hbox_botones)
        self.setLayout(vbox)
        self.show()

    def mostrar_ranking(self):
        self.hide()
        self.senal_calcular_ranking.emit()

    def comenzar(self):
        nombre_usuario = self.etiqueta_nombre.text()
        if self.etiqueta_nombre.text().isalnum():
            self.hide()
            self.senal_comenzar.emit(nombre_usuario)
            self.etiqueta_nombre.clear()
        else:
            alerta = QErrorMessage(self)
            alerta.setWindowTitle('ALERTA')
            alerta.showMessage('El nombre debe ser alfanumerico')


if __name__ == "__main__":
    app = QApplication([])
    ventana = fInicio((500, 500))
    sys.exit(app.exec_())
