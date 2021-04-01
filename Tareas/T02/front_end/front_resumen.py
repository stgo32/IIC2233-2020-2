import sys
sys.path.append('..')
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout, QApplication
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from T02.parametros import (
    APROBACION_PRINCIPIANTE, APROBACION_AFICIONADO, APROBACION_MAESTRO, SET_GEO_LABEL_PERDIDA,
    MAX_WIDTH_BOTON_RESUMEN, SET_GEO_BOTON_RESUMEN, MIN_WIDTH_BOTON_RESUMEN, RUTA_PUFFLE_CANGREJO,
    PUFFLE_SET_GEO
)


class fResumen(QWidget):

    senal_mostrar_resumen = pyqtSignal(int, int, int, int, int, int)
    senal_volver_inicio = pyqtSignal()

    def __init__(self, min_size):
        super().__init__()
        self.min_size = min_size  # tuple
        self.senal_mostrar_resumen.connect(self.actualizar_resumen)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('Ventana de Resumen')
        self.setMinimumWidth(self.min_size[0])
        self.setMinimumHeight(self.min_size[1])

        self.label = QLabel('Resumen de la Ronda\n', self)
        self.label.setObjectName('labelResumen')
        self.vbox = QVBoxLayout(self)

        self.label_p_obtenido = QLabel('Puntaje Obtenido:', self)
        self.label_p_acumulado = QLabel('Puntaje Acumulado:', self)
        self.label_mayor_combo = QLabel('Mayor Combo:', self)
        self.label_pasos_fall = QLabel('Pasos Fallados:', self)
        self.label_aprobacion = QLabel('Aprobacion:', self)

        self.label_perdida = QLabel('', self)
        self.label_perdida.setGeometry(*SET_GEO_LABEL_PERDIDA)
        self.label_perdida.hide()

        self.boton_volver_inicio = QPushButton('Volver a Inicio', self)
        self.boton_volver_inicio.setMaximumWidth(MAX_WIDTH_BOTON_RESUMEN)
        self.boton_volver_inicio.setMinimumWidth(MIN_WIDTH_BOTON_RESUMEN)
        self.boton_volver_inicio.clicked.connect(self.volver_a_inicio)
        self.boton_volver_inicio.setGeometry(*SET_GEO_BOTON_RESUMEN)
        self.boton_volver_inicio.hide()

        self.puffle = QLabel(self)
        self.puffle.setPixmap(QPixmap(RUTA_PUFFLE_CANGREJO))
        self.puffle.setGeometry(*PUFFLE_SET_GEO)
        self.puffle.setScaledContents(True)

        self.label_p_obtenido.setObjectName('_labelResumen')
        self.label_p_acumulado.setObjectName('_labelResumen')
        self.label_mayor_combo.setObjectName('_labelResumen')
        self.label_pasos_fall.setObjectName('_labelResumen')
        self.label_aprobacion.setObjectName('_labelResumen')

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.label_p_obtenido)
        self.vbox.addWidget(self.label_p_acumulado)
        self.vbox.addWidget(self.label_mayor_combo)
        self.vbox.addWidget(self.label_pasos_fall)
        self.vbox.addWidget(self.label_aprobacion)

        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def volver_a_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()

    def actualizar_resumen(self, p_obtenido, p_acumulado, mayor_combo,
                           pasos_fallados, aprobacion, dificultad):

        self.label_p_obtenido.setText(f'Puntaje Obtenido:                       {p_obtenido}pts.')
        self.label_p_acumulado.setText(f'Puntaje Acumulado:                   {p_acumulado}pts.')
        self.label_mayor_combo.setText(f'Mayor Combo:                             X{mayor_combo}')
        self.label_pasos_fall.setText(f'Pasos Fallados:                           {pasos_fallados}')
        self.label_aprobacion.setText(f'Aprobacion:                                 {aprobacion}%')
        print('aprobacion resumen', aprobacion)
        if dificultad == 0:
            if aprobacion < APROBACION_PRINCIPIANTE:
                self.label_perdida.setText('Haz perdido, no obtuviste la suficiente aprobacion')
                self.label_perdida.show()
                self.boton_volver_inicio.show()
        elif dificultad == 1:
            if aprobacion < APROBACION_AFICIONADO:
                self.label_perdida.setText('Haz perdido, no obtuviste la suficiente aprobacion')
                self.label_perdida.show()
                self.boton_volver_inicio.show()
        elif dificultad == 2:
            if aprobacion < APROBACION_MAESTRO:
                self.label_perdida.setText('Haz perdido, no obtuviste la suficiente aprobacion')
                self.label_perdida.show()
                self.boton_volver_inicio.show()

        self.vbox.addStretch(1)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    punt = {'ppp': 50, 'dadad': 100}
    ventana = fResumen((500, 500))
    ventana.show()
    sys.exit(app.exec_())
