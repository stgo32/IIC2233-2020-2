import sys
sys.path.append('..')

from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QApplication, QComboBox,
    QProgressBar, QShortcut, QErrorMessage
)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QPixmap, QKeySequence

from T02.back_end.pinguinirines import DragPingu, DropPingu
from T02.parametros import (
    RUTA_LOGO, LOGO_SIZE, RUTA_FONDO, FONDO_SIZE, RUTA_FLECHA_RITMO_LEFT, RUTA_FLECHA_RITMO_UP,
    RUTA_FLECHA_RITMO_DOWN, RUTA_FLECHA_RITMO_RIGHT, MAX_TAMANO_FLECHA, STYLE_CUADROS_FLECHA_IMPAR,
    STYLE_CUADROS_FLECHA_PAR, BORDE_INFERIOR, BORDE_IZQUIERDA, MIN_WIDTH_TIENDA, MAX_WIDTH_BARRA,
    MAX_WIDTH_COMBO, RUTA_CANCION_1, RUTA_CANCION_2, DINERO_INICIAL, DINERO_TRAMPA,
    PRECIO_PINGUIRIN
)

#  codigo de captura de multiples teclas basado en:
#  https://stackoverflow.com/questions/7176951/how-to-get-multiple-key-presses-in-single-event


class fJuego(QWidget):

    senal_mostrar_juego = pyqtSignal(str)
    senal_volver_inicio = pyqtSignal()
    senal_capturar_flecha = pyqtSignal(list)
    senal_nombre_usuario = pyqtSignal(str)
    senal_inicio_de_nivel = pyqtSignal(int, QMediaContent)
    senal_resetear_partida = pyqtSignal()
    senal_cheat_code_money = pyqtSignal()
    senal_cheat_code_nivel = pyqtSignal()
    senal_pausar = pyqtSignal(str)

    def __init__(self, min_size):
        super().__init__()
        self.min_size = min_size  # tuple
        self.max_size = self.min_size
        self.firstrelease = None
        self.keylist = []
        # senales
        self.senal_mostrar_juego.connect(self.inicializar)
        # gui
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('Menú de Juego DCCumbia')
        self.setMinimumWidth(self.min_size[0])
        self.setMinimumHeight(self.min_size[1])
        self.focusPolicy()
        ''' 1. PISTA DE BAILE '''
        self.fondo = QLabel(self)
        self.fondo.setPixmap(QPixmap(RUTA_FONDO))
        self.fondo.setMaximumWidth(FONDO_SIZE[0]/2)
        self.fondo.setMaximumHeight(FONDO_SIZE[1]/2)
        self.fondo.setScaledContents(True)

        self.lista_dropers = [DropPingu(self, i) for i in range(20)]
        for i in range(len(self.lista_dropers)):
            if i < 6:
                self.lista_dropers[i].setGeometry(410 + 100*i, 530, 100, 100)
            elif i < 13:
                self.lista_dropers[i].setGeometry(350 + 100*(i-6), 630, 100, 100)
            else:
                self.lista_dropers[i].setGeometry(360 + 100*(i-13), 730, 100, 100)

        ''' 2. ZONA DE RITMO '''
        self.cuadro_left = QLabel(self)
        self.cuadro_left.setGeometry(BORDE_IZQUIERDA,
                                     self.height() - MAX_TAMANO_FLECHA - BORDE_INFERIOR,
                                     MAX_TAMANO_FLECHA,
                                     MAX_TAMANO_FLECHA)
        self.cuadro_left.setStyleSheet(STYLE_CUADROS_FLECHA_IMPAR)
        self.cuadro_up = QLabel(self)
        self.cuadro_up.setGeometry(MAX_TAMANO_FLECHA + BORDE_IZQUIERDA,
                                   self.height() - MAX_TAMANO_FLECHA - BORDE_INFERIOR,
                                   MAX_TAMANO_FLECHA,
                                   MAX_TAMANO_FLECHA)
        self.cuadro_up.setStyleSheet(STYLE_CUADROS_FLECHA_PAR)
        self.cuadro_down = QLabel(self)
        self.cuadro_down.setGeometry(MAX_TAMANO_FLECHA*2 + BORDE_IZQUIERDA,
                                     self.height() - MAX_TAMANO_FLECHA - BORDE_INFERIOR,
                                     MAX_TAMANO_FLECHA,
                                     MAX_TAMANO_FLECHA)
        self.cuadro_down.setStyleSheet(STYLE_CUADROS_FLECHA_IMPAR)
        self.cuadro_right = QLabel(self)
        self.cuadro_right.setGeometry(MAX_TAMANO_FLECHA*3 + BORDE_IZQUIERDA,
                                      self.height() - MAX_TAMANO_FLECHA - BORDE_INFERIOR,
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

        self.flechas = []
        ''' 3. TIENDA '''
        self.label_tienda = QLabel('Tienda', self)
        self.label_tienda.setObjectName('labelTienda')
        self.label_tienda.setMinimumWidth(MIN_WIDTH_TIENDA)
        self.label_dinero_usuario = QLabel(f'Dinero: ${DINERO_INICIAL}', self)
        self.label_dinero_usuario.setObjectName('_labelDinero')
        self.label_valor_piguino = QLabel(f'Valor pingüino: ${PRECIO_PINGUIRIN}', self)
        self.label_valor_piguino.setObjectName('_labelDinero')
        vbox_labels_tienda = QVBoxLayout()
        self.pingu_amarillo = DragPingu(self, 'amarillo')
        self.pingu_celeste = DragPingu(self, 'celeste')
        hbox_pingu_1 = QHBoxLayout()
        hbox_pingu_1.addWidget(self.pingu_amarillo)
        hbox_pingu_1.addWidget(self.pingu_celeste)
        self.pingu_morado = DragPingu(self, 'morado')
        self.pingu_verde = DragPingu(self, 'verde')
        hbox_pingu_2 = QHBoxLayout()
        hbox_pingu_2.addWidget(self.pingu_morado)
        hbox_pingu_2.addWidget(self.pingu_verde)
        self.pingu_rojo = DragPingu(self, 'rojo')
        hbox_pingu_3 = QHBoxLayout()
        hbox_pingu_3.addWidget(self.pingu_rojo)
        vbox_labels_tienda.addWidget(self.label_tienda)
        vbox_labels_tienda.addWidget(self.label_dinero_usuario)
        vbox_labels_tienda.addWidget(self.label_valor_piguino)
        vbox_labels_tienda.addLayout(hbox_pingu_1)
        vbox_labels_tienda.addLayout(hbox_pingu_2)
        vbox_labels_tienda.addLayout(hbox_pingu_3)
        vbox_labels_tienda.addStretch(1)
        hbox_tienda = QHBoxLayout()
        hbox_tienda.addLayout(vbox_labels_tienda)
        hbox_tienda.setAlignment(Qt.AlignCenter)
        ''' 4. ZONA DE ESTADISTICAS '''
        # logo
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(RUTA_LOGO))
        self.logo.setMaximumWidth(LOGO_SIZE[0]/4)
        self.logo.setMaximumHeight(LOGO_SIZE[1]/4)
        self.logo.setScaledContents(True)
        # combos
        vbox_combos = QVBoxLayout()
        self.combo_actual = QLabel('Combo: ', self)
        self.combo_mayor = QLabel('Mayor Combo: ', self)
        vbox_combos.addWidget(self.combo_actual)
        vbox_combos.addWidget(self.combo_mayor)
        # barras de progreso
        vbox_barras = QVBoxLayout()
        self.label_progreso = QLabel('Progreso: ', self)
        self.label_aprobacion = QLabel('Aprobación: ', self)
        self.barra_progreso = QProgressBar(self)
        self.barra_aprobacion = QProgressBar(self)
        self.barra_progreso.setMaximumWidth(MAX_WIDTH_BARRA)
        self.barra_aprobacion.setMaximumWidth(MAX_WIDTH_BARRA)
        vbox_barras.addWidget(self.label_progreso)
        vbox_barras.addWidget(self.barra_progreso)
        vbox_barras.addWidget(self.label_aprobacion)
        vbox_barras.addWidget(self.barra_aprobacion)
        # combo boxes
        vbox_combo_boxes = QVBoxLayout()
        vbox_cancion = QVBoxLayout()
        self.label_cancion = QLabel('Canción:', self)
        self.combo_box_cancion = QComboBox(self)
        self.combo_box_cancion.setMaximumWidth(MAX_WIDTH_COMBO)
        self.combo_box_cancion.addItems(['Cancion 1', 'Cancion 2'])
        vbox_cancion.addWidget(self.label_cancion)
        vbox_cancion.addWidget(self.combo_box_cancion)
        vbox_dificultad = QVBoxLayout()
        self.label_dificultad = QLabel('Dificultad:', self)
        self.combo_box_dificultad = QComboBox(self)
        self.combo_box_dificultad.setMaximumWidth(MAX_WIDTH_COMBO)
        self.combo_box_dificultad.addItems(['Principiante', 'Aficionado', 'Maestro Cumbia'])
        vbox_dificultad.addWidget(self.label_dificultad)
        vbox_dificultad.addWidget(self.combo_box_dificultad)
        vbox_combo_boxes.addLayout(vbox_cancion)
        vbox_combo_boxes.addLayout(vbox_dificultad)
        # botones
        vbox_botones = QVBoxLayout()
        self.boton_pausar = QPushButton('Pausar', self)
        self.boton_pausar.clicked.connect(self.pausar)
        self.boton_salir = QPushButton('Salir', self)
        self.boton_salir.clicked.connect(self.volver_a_inicio)
        self.boton_comenzar = QPushButton('Comenzar Partida', self)
        self.boton_comenzar.clicked.connect(self.inicio_de_nivel)
        vbox_botones.addWidget(self.boton_pausar)
        vbox_botones.addWidget(self.boton_salir)
        vbox_botones.addWidget(self.boton_comenzar)
        # layout zona estadisticas
        hbox_zona_estca = QHBoxLayout()
        hbox_zona_estca.addWidget(self.logo)
        hbox_zona_estca.addLayout(vbox_combos)
        hbox_zona_estca.addLayout(vbox_barras)
        hbox_zona_estca.addLayout(vbox_combo_boxes)
        hbox_zona_estca.addLayout(vbox_botones)
        hbox_zona_estca.setObjectName('hboxZonaEstca')
        # media player
        self.media_player = QMediaPlayer()
        # shortcuts
        self.shortcut_money = QShortcut(QKeySequence(Qt.Key_M, Qt.Key_O, Qt.Key_N), self)
        self.shortcut_money.activated.connect(self.cheat_code_money)
        self.shortcut_nivel = QShortcut(QKeySequence(Qt.Key_N, Qt.Key_I, Qt.Key_V), self)
        self.shortcut_nivel.activated.connect(self.cheat_code_nivel)
        self.shortcut_pausa = QShortcut(QKeySequence(Qt.Key_P), self)
        self.shortcut_pausa.activated.connect(self.pausar)
        ''' LAYOUT GENERAL '''
        hbox_juego = QHBoxLayout()
        hbox_juego.addLayout(vbox_flechas)
        hbox_juego.addWidget(self.fondo)
        hbox_juego.addLayout(hbox_tienda)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_zona_estca)
        vbox.addLayout(hbox_juego)
        self.setMaximumWidth(self.max_size[0])
        self.setMaximumHeight(self.max_size[1])
        self.setLayout(vbox)
        self.setMinimumWidth(self.min_size[0])
        self.setMinimumHeight(self.min_size[1])

    def inicializar(self, nombre_usuario):
        self.senal_nombre_usuario.emit(nombre_usuario)
        self.show()

    def volver_a_inicio(self):
        self.combo_mayor.setText('Mayor Combo:')
        self.barra_progreso.setValue(0)
        self.barra_aprobacion.setValue(0)
        self.boton_comenzar.setEnabled(True)
        self.combo_box_cancion.setEnabled(True)
        self.combo_box_dificultad.setEnabled(True)

        for drop_pingu in self.lista_dropers:
            drop_pingu.color = None
            drop_pingu.setPixmap(QPixmap())

        self.media_player.pause()
        self.senal_resetear_partida.emit()
        self.senal_volver_inicio.emit()
        self.hide()

    def inicio_de_nivel(self):
        iniciacion_completa = False
        for drop_pingu in self.lista_dropers:
            if drop_pingu.color is not None:
                iniciacion_completa = True
                continue
        if iniciacion_completa:
            dificultad = self.combo_box_dificultad.currentIndex()
            cancion = self.combo_box_cancion.currentIndex()
            if cancion == 0:
                self.senal_inicio_de_nivel.emit(dificultad,
                                                QMediaContent(QUrl.fromLocalFile(RUTA_CANCION_1)))
            elif cancion == 1:
                self.senal_inicio_de_nivel.emit(dificultad,
                                                QMediaContent(QUrl.fromLocalFile(RUTA_CANCION_2)))
            self.combo_box_cancion.setEnabled(False)
            self.combo_box_dificultad.setEnabled(False)
            self.boton_comenzar.setEnabled(False)
        else:
            alerta_comenzar = QErrorMessage(self)
            alerta_comenzar.setWindowTitle('ALERTA')
            alerta_comenzar.showMessage('Debe tener al menos un pingüirín en la pista de baile')

    def actualizar_label(self, label, x, y):
        label.move(x, y)

    def keyPressEvent(self, event):
        self.firstrelease = True
        self.keylist.append(event.key())

    def keyReleaseEvent(self, event):
        if self.firstrelease:
            self.processmultikeys(self.keylist)
        self.firstrelease = False
        if self.keylist != []:
            self.keylist.pop(-1)

    def processmultikeys(self, keyspressed):
        print('senal', keyspressed)
        self.senal_capturar_flecha.emit(keyspressed)

    def cheat_code_money(self):
        self.senal_cheat_code_money.emit()
        self.label_dinero_usuario.setText(f'Dinero: ${DINERO_TRAMPA}')

    def cheat_code_nivel(self):
        print('cheat code nivel')
        self.senal_cheat_code_nivel.emit()

    def pausar(self):
        if self.boton_pausar.text() == 'Pausar':
            self.boton_pausar.setText('Play')
            self.senal_pausar.emit('Pausar')
        elif self.boton_pausar.text() == 'Play':
            self.boton_pausar.setText('Pausar')
            self.senal_pausar.emit('Play')

    def iniciacion_incompleta(self):
        print('incompleta')
        self.combo_box_cancion.setEnabled(True)
        self.combo_box_dificultad.setEnabled(True)
        self.boton_comenzar.setEnabled(True)


if __name__ == "__main__":
    app = QApplication([])
    ventana = fJuego((1600, 900))
    ventana.show()
    sys.exit(app.exec_())
