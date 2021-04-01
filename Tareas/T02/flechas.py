import sys
from time import sleep
from random import randint
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QApplication, QShortcut
)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QEventLoop, QTimer, QThread
from PyQt5.QtGui import QPixmap, QKeySequence

from parametros import (
    RUTA_FLECHA_RITMO_LEFT, RUTA_FLECHA_RITMO_RIGHT, RUTA_FLECHA_RITMO_UP, RUTA_FLECHA_RITMO_DOWN,
    MAX_TAMANO_FLECHA, STYLE_CUADROS_FLECHA_IMPAR, STYLE_CUADROS_FLECHA_PAR,
    RUTA_FLECHA_NORMAL_LEFT, RUTA_FLECHA_NORMAL_UP, RUTA_FLECHA_NORMAL_DOWN, 
    RUTA_FLECHA_NORMAL_RIGHT, FLECHA_IZQUIERDA, FLECHA_ARRIBA, FLECHA_ABAJO, FLECHA_DERECHA
)


def dormir(segundos):
    loop = QEventLoop()
    QTimer.singleShot(segundos*1000, loop.quit)
    loop.exec_()


class Flechas(QWidget):


    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size  # tuple
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('flechas temp')
        self.setGeometry(300, 300, self.max_size[0], self.max_size[1])

        self.cuadro_left = QLabel(self)
        self.cuadro_left.setGeometry(5,
                                     620,
                                     MAX_TAMANO_FLECHA, 
                                     MAX_TAMANO_FLECHA)
        self.cuadro_left.setStyleSheet(STYLE_CUADROS_FLECHA_IMPAR)

        self.cuadro_up = QLabel(self)
        self.cuadro_up.setGeometry(MAX_TAMANO_FLECHA+5,
                                     620,
                                     MAX_TAMANO_FLECHA, 
                                     MAX_TAMANO_FLECHA)
        self.cuadro_up.setStyleSheet(STYLE_CUADROS_FLECHA_PAR)

        self.cuadro_down = QLabel(self)
        self.cuadro_down.setGeometry(MAX_TAMANO_FLECHA*2+5,
                                     620,
                                     MAX_TAMANO_FLECHA, 
                                     MAX_TAMANO_FLECHA)
        self.cuadro_down.setStyleSheet(STYLE_CUADROS_FLECHA_IMPAR)

        self.cuadro_right = QLabel(self)
        self.cuadro_right.setGeometry(MAX_TAMANO_FLECHA*3+5,
                                     620,
                                     MAX_TAMANO_FLECHA, 
                                     MAX_TAMANO_FLECHA)
        self.cuadro_right.setStyleSheet(STYLE_CUADROS_FLECHA_PAR)
        self.f_left = QLabel(self)
        self.f_left.setPixmap(QPixmap(RUTA_FLECHA_RITMO_LEFT))
        self.f_left.setMaximumWidth(MAX_TAMANO_FLECHA)
        self.f_left.setMaximumHeight(MAX_TAMANO_FLECHA)
        self.f_left.setScaledContents(True)
        self.f_up = QLabel(self)
        self.f_up.setPixmap(QPixmap(RUTA_FLECHA_RITMO_UP))
        self.f_up.setMaximumWidth(MAX_TAMANO_FLECHA)
        self.f_up.setMaximumHeight(MAX_TAMANO_FLECHA)
        self.f_up.setScaledContents(True)
        self.f_down = QLabel(self)
        self.f_down.setPixmap(QPixmap(RUTA_FLECHA_RITMO_DOWN))
        self.f_down.setMaximumWidth(MAX_TAMANO_FLECHA)
        self.f_down.setMaximumHeight(MAX_TAMANO_FLECHA)
        self.f_down.setScaledContents(True)
        self.f_right = QLabel(self)
        self.f_right.setPixmap(QPixmap(RUTA_FLECHA_RITMO_RIGHT))
        self.f_right.setMaximumWidth(MAX_TAMANO_FLECHA)
        self.f_right.setMaximumHeight(MAX_TAMANO_FLECHA)
        self.f_right.setScaledContents(True)

        hbox_flechas = QHBoxLayout()
        hbox_flechas.addWidget(self.f_left)
        hbox_flechas.addWidget(self.f_up)
        hbox_flechas.addWidget(self.f_down)
        hbox_flechas.addWidget(self.f_right)
        vbox_flechas = QVBoxLayout()
        self.f_label = QLabel('', self)
        vbox_flechas.addWidget(self.f_label)
        vbox_flechas.addLayout(hbox_flechas)
        self.setLayout(vbox_flechas)

        self.timer_crea_flecha = QTimer(self)
        self.timer_crea_flecha.setInterval(1000)
        self.timer_crea_flecha.timeout.connect(self.creador_flechas)
        self.timer_crea_flecha.start()

        self.flechas = []
        self.firstrelease = None
        self.keylist = []

    def creador_flechas(self):
        columna = randint(0, 3)
        nueva_flecha = PosicionFlechas(self, self.width(), self.height(), columna)
        nueva_flecha.actualizar.connect(self.actualizar_label)
        self.flechas.append(nueva_flecha)

    def actualizar_label(self, label, x, y):
        label.move(x, y)

    def keyPressEvent(self, event):
        print(event.key())
        self.firstrelease = True
        astr = "pressed: " + str(event.key())
        self.keylist.append(astr)

    def keyReleaseEvent(self, event):
        if self.firstrelease == True: 
            self.processmultikeys(self.keylist)

        self.firstrelease = False

        self.keylist.pop(-1)

    def processmultikeys(self, keyspressed):
        print(keyspressed)

        

class PosicionFlechas(QThread):

    actualizar = pyqtSignal(QLabel, int, int)

    def __init__(self, parent, limite_x, limite_y, columna):
        """
        Una Comida es un QThread que movera una imagen de comida
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            limite_x e limite_y: Los límites rectangulares de la ventana
        """
        super().__init__()
        self.columna = columna
        # Guardamos el path de la imagen que tendrá el Label
        rutas = [RUTA_FLECHA_NORMAL_LEFT, RUTA_FLECHA_NORMAL_UP, RUTA_FLECHA_NORMAL_DOWN, 
                 RUTA_FLECHA_NORMAL_RIGHT]
        self.ruta_imagen = rutas[self.columna]

        # Creamos el Label y definimos su tamaño
        self.label = QLabel(parent)
        self.label.setGeometry(MAX_TAMANO_FLECHA*2+5, -50, MAX_TAMANO_FLECHA, MAX_TAMANO_FLECHA)
        self.label.setPixmap(QPixmap(self.ruta_imagen))
        self.label.setScaledContents(True)
        self.label.setVisible(True)

        # Guardamos los limites de la ventana para que no pueda salirse de ella
        self.limite_x = limite_x
        self.limite_y = limite_y
        # Seteamos la posición inicial y la guardamos para usarla como una property
        self.__posicion = (0, 0)
        self.posicion = (MAX_TAMANO_FLECHA*self.columna + 5, -50)

        self.label.show()
        self.start()

    @property
    def posicion(self):
        return self.__posicion

    # Cada vez que se actualicé la posición,
    # se actualiza la posición de la etiqueta
    @posicion.setter
    def posicion(self, valor):
        self.__posicion = valor
        self.actualizar.emit(self.label, *self.posicion)

    def run(self):
        while self.posicion[0] < self.limite_x and self.posicion[1] < self.limite_y:
            sleep(0.1)
            nuevo_x = MAX_TAMANO_FLECHA*self.columna + 5
            nuevo_y = self.posicion[1] + 10
            self.posicion = (nuevo_x, nuevo_y)


if __name__ == "__main__":
    app = QApplication([])
    ventana = Flechas((MAX_TAMANO_FLECHA*4, 700))
    ventana.show()
    sys.exit(app.exec_())