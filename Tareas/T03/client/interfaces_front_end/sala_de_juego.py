import os

from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QErrorMessage
)
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QPixmap, QIcon

from interfaces_front_end.chozas import DragChoza, DropChoza

from parametros import p


class VentanaSalaJuego(QWidget):

    senal_lanzar_dados = pyqtSignal()
    senal_dejar_de_actuar_turno = pyqtSignal(dict)
    senal_terminar_turno = pyqtSignal()
    senal_preguntar_por_choza = pyqtSignal(int)
    senal_abrir_chat = pyqtSignal()

    def __init__(self, size):
        super().__init__()
        self.size = size  # tuple
        self.tablero = None
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle('DCColonos')
        self.setMinimumSize(*self.size)

        ''' Mazo '''
        self.label_arcilla_user = QLabel(self)
        ruta = os.path.join(*tuple(p.MATERIAS_PRIMAS["RUTA_CARTA_ARCILLA"]))
        self.label_arcilla_user.setPixmap(QPixmap(ruta))
        self.label_arcilla_user.setMaximumSize(p.TAMANO_CARTA[0]/3, p.TAMANO_CARTA[1]/3)
        self.label_arcilla_user.setScaledContents(True)
        self.label_arcilla_user.move(20,
                                     self.size[1]-p.TAMANO_CARTA[1]/3-30)

        self.label_madera_user = QLabel(self)
        ruta = os.path.join(*tuple(p.MATERIAS_PRIMAS["RUTA_CARTA_MADERA"]))
        self.label_madera_user.setPixmap(QPixmap(ruta))
        self.label_madera_user.setMaximumSize(p.TAMANO_CARTA[0]/3, p.TAMANO_CARTA[1]/3)
        self.label_madera_user.setScaledContents(True)
        self.label_madera_user.move(20+40+p.TAMANO_CARTA[0]/3,
                                    self.size[1]-p.TAMANO_CARTA[1]/3-30)

        self.label_trigo_user = QLabel(self)
        ruta = os.path.join(*tuple(p.MATERIAS_PRIMAS["RUTA_CARTA_TRIGO"]))
        self.label_trigo_user.setPixmap(QPixmap(ruta))
        self.label_trigo_user.setMaximumSize(p.TAMANO_CARTA[0]/3, p.TAMANO_CARTA[1]/3)
        self.label_trigo_user.setScaledContents(True)
        self.label_trigo_user.move(20+40*2+p.TAMANO_CARTA[0]/3*2,
                                   self.size[1]-p.TAMANO_CARTA[1]/3-30)

        self.label_contador_arcilla = QLabel(': 1', self)
        self.label_contador_arcilla.move(20+5+p.TAMANO_CARTA[0]/3,
                                         self.size[1]-p.TAMANO_CARTA[1]/6-30)
        self.label_contador_madera = QLabel(': 1', self)
        self.label_contador_madera.move(20+5+40+p.TAMANO_CARTA[0]/3*2,
                                        self.size[1]-p.TAMANO_CARTA[1]/6-30)
        self.label_contador_trigo = QLabel(': 1', self)
        self.label_contador_trigo.move(20+5+40*2+p.TAMANO_CARTA[0]/3*3,
                                       self.size[1]-p.TAMANO_CARTA[1]/6-30)

        ''' Tienda '''
        self.drag_choza = DragChoza(self, 'azul')
        print(self.drag_choza.color)
        self.drag_choza.setMaximumSize(100, 100)
        self.drag_choza.setScaledContents(True)
        self.drag_choza.move(self.size[0]/2-100, self.size[1]-50-100)

        self.label_camino = QLabel(self)
        ruta = os.path.join(*tuple(p.CONSTRUCCIONES['RUTA_CAMINO_AZUL_0']))
        self.label_camino.setPixmap(QPixmap(ruta))
        self.label_camino.setMaximumSize(p.TAMANO_CAMINO[0]*2/3, p.TAMANO_CAMINO[1]*2/3)
        self.label_camino.setScaledContents(True)
        self.label_camino.move(self.size[0]/2+20, self.size[1]-50-p.TAMANO_CAMINO[1]*3/2)

        self.label_desarrollo = QLabel(self)
        ruta = os.path.join(*tuple(p.DESARROLLO["RUTA_CARTA_REVERSO"]))
        self.label_desarrollo.setPixmap(QPixmap(ruta))
        self.label_desarrollo.setMaximumSize(p.TAMANO_CARTA[0]/3, p.TAMANO_CARTA[1]/3)
        self.label_desarrollo.setScaledContents(True)
        self.label_desarrollo.move(self.size[0]/2+100+20*2, self.size[1]-p.TAMANO_CARTA[1]/3-30)

        ''' Dados e intercambio '''
        self.label_dado_izq = QLabel(self)
        ruta = os.path.join(*tuple(p.DADOS["RUTA_DADO_6"]))
        self.label_dado_izq.setPixmap(QPixmap(ruta))
        self.label_dado_izq.setMaximumSize(100, 100)
        self.label_dado_izq.setScaledContents(True)
        self.label_dado_izq.move(self.size[0]-100*2-20*2, self.size[1]-30-100)

        self.label_dado_der = QLabel(self)
        ruta = os.path.join(*tuple(p.DADOS["RUTA_DADO_6"]))
        self.label_dado_der.setPixmap(QPixmap(ruta))
        self.label_dado_der.setMaximumSize(100, 100)
        self.label_dado_der.setScaledContents(True)
        self.label_dado_der.move(self.size[0]-100-20, self.size[1]-30-100)

        self.boton_dados = QPushButton('Lanzar Dados', self)
        self.boton_dados.move(self.size[0]-100-50-20*3/2, self.size[1]-p.TAMANO_CARTA[1]/3-30)
        self.boton_dados.clicked.connect(self.senal_lanzar_dados.emit)

        ruta = os.path.join(*tuple(p.RUTA_ICONO_INTERCAMBIO))
        self.boton_intercambio_cartas = QPushButton(QIcon(ruta), '', self)
        self.boton_intercambio_cartas.setIconSize(QSize(90, 90))
        self.boton_intercambio_cartas.setMinimumSize(90, 90)
        self.boton_intercambio_cartas.move(self.size[0]-100*3-20*3, self.size[1]-50-100)
        self.boton_intercambio_cartas.clicked.connect(self.intercambio_cartas)

        ''' Boton terminar turno '''
        self.boton_terminar_turno = QPushButton('Terminar mi Turno', self)
        self.boton_terminar_turno.move(20, self.size[1]-p.TAMANO_CARTA[1]/3-70)
        self.boton_terminar_turno.setEnabled(False)
        self.boton_terminar_turno.clicked.connect(self.terminar_turno)

        ''' Boton chat '''
        self.boton_chat = QPushButton('Abrir Chat', self)
        self.boton_chat.move(150, self.size[1]-p.TAMANO_CARTA[1]/3-70)
        self.boton_chat.setEnabled(True)
        self.boton_chat.clicked.connect(self.senal_abrir_chat)

        ''' Turnos y puntajes '''
        self.label_encuadre_turnos = QLabel('', self)
        self.label_encuadre_turnos.setMinimumSize(400, 650)
        self.label_encuadre_turnos.move(self.size[0]-400-20, 30)
        self.label_encuadre_turnos.setStyleSheet('border: 1px solid')

        self.label_turno_actual = QLabel('Turno de: Jugador0', self)
        self.label_turno_actual.move(self.size[0]-400+20, 50)
        self.label_turno_actual.setMinimumWidth(200)

        self.lista_jugadores = []
        for i in range(p.MAX_JUGADORES_PARTIDA - 1):
            label_nombre = QLabel(f'Jugador{i}', self)
            label_nombre.move(self.size[0]-400+20, 50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1))
            label_puntos = QLabel('Puntos: 0', self)
            label_puntos.move(self.size[0]-400/2+20, 50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1))

            label_arcilla_user = QLabel(self)
            ruta = os.path.join(*tuple(p.MATERIAS_PRIMAS["RUTA_CARTA_ARCILLA"]))
            label_arcilla_user.setPixmap(QPixmap(ruta))
            label_arcilla_user.setMaximumSize(p.TAMANO_CARTA[0]/6, p.TAMANO_CARTA[1]/6)
            label_arcilla_user.setScaledContents(True)
            label_arcilla_user.move(self.size[0]-400+20,
                                    50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1) + 30)

            label_madera_user = QLabel(self)
            ruta = os.path.join(*tuple(p.MATERIAS_PRIMAS["RUTA_CARTA_MADERA"]))
            label_madera_user.setPixmap(QPixmap(ruta))
            label_madera_user.setMaximumSize(p.TAMANO_CARTA[0]/6, p.TAMANO_CARTA[1]/6)
            label_madera_user.setScaledContents(True)
            label_madera_user.move(self.size[0] - 400 + 20 + p.TAMANO_CARTA[0]/6*2.5,
                                   50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1) + 30)

            label_trigo_user = QLabel(self)
            ruta = os.path.join(*tuple(p.MATERIAS_PRIMAS["RUTA_CARTA_TRIGO"]))
            label_trigo_user.setPixmap(QPixmap(ruta))
            label_trigo_user.setMaximumSize(p.TAMANO_CARTA[0]/6, p.TAMANO_CARTA[1]/6)
            label_trigo_user.setScaledContents(True)
            label_trigo_user.move(self.size[0] - 400 + 20 + p.TAMANO_CARTA[0]/6*2.5*2,
                                  50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1) + 30)

            label_contador_arcilla = QLabel(': 0', self)
            label_contador_arcilla.move(self.size[0] - 400 + 25 + p.TAMANO_CARTA[0]/6,
                                        50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1) + 50)
            label_contador_madera = QLabel(': 0', self)
            label_contador_madera.move(self.size[0] - 400 + 25 + p.TAMANO_CARTA[0]/6*3.5,
                                       50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1) + 50)
            label_contador_trigo = QLabel(': 0', self)
            label_contador_trigo.move(self.size[0] - 400 + 25 + p.TAMANO_CARTA[0]/6*6,
                                      50 + p.TAMANO_CARTA[1]/6*i + 40*(i+1) + 50)

            self.lista_jugadores.append({
                'label_nombre': label_nombre,
                'label_puntos': label_puntos,
                'label_arcilla_user': label_arcilla_user,
                'label_madera_user': label_madera_user,
                'label_trigo_user': label_trigo_user,
                'label_contador_madera': label_contador_madera,
                'label_contador_arcilla': label_contador_arcilla,
                'label_contador_trigo': label_contador_trigo
            })

        self.label_carretera_mas_larga = QLabel('Carretera mas larga: Jugador0', self)
        self.label_carretera_mas_larga.move(self.size[0]-400+20, 450)

        self.label_nombre_usuario = QLabel('Jugador3 (Tú)', self)
        self.label_nombre_usuario.move(self.size[0]-400+20, 500)

        self.label_carta_puntos_victoria_usuario = QLabel(self)
        ruta = os.path.join(*tuple(p.DESARROLLO["RUTA_CARTA_VICTORIA_1"]))
        self.label_carta_puntos_victoria_usuario.setPixmap(QPixmap(ruta))
        self.label_carta_puntos_victoria_usuario.setMaximumSize(p.TAMANO_CARTA[0]/4,
                                                                p.TAMANO_CARTA[1]/4)
        self.label_carta_puntos_victoria_usuario.setScaledContents(True)
        self.label_carta_puntos_victoria_usuario.move(self.size[0] - 400 + 20, 500 + 30)

        self.label_puntos_victoria_usuario = QLabel(': 0', self)
        self.label_puntos_victoria_usuario.move(self.size[0]-400+25+p.TAMANO_CARTA[0]/4, 500 + 70)

    def generar_tablero(self):
        self.lista_labels_hexagonos = []
        for hexagono in self.tablero.lista_hexagonos:
            label_hexagono = QLabel(self)
            ruta = os.path.join(*p.MATERIAS_PRIMAS["RUTA_HEXAGONO_ARCILLA"])
            label_hexagono.setPixmap(QPixmap(ruta))
            label_hexagono.setMaximumSize(*hexagono.size())
            label_hexagono.setScaledContents(True)
            label_hexagono.move(*hexagono.posicion())
            self.lista_labels_hexagonos.append(label_hexagono)

        self.lista_nodos = []
        for nodo in self.tablero.lista_nodos:
            drop_choza = DropChoza(self)
            # drop_choza.senal_colocar_choza.connect(self.dejar_de_actuar_turno)
            drop_choza.senal_preguntar_por_choza.connect(self.preguntar_por_choza)
            nodo.choza = drop_choza
            drop_choza.nodo = nodo
            drop_choza.move(*nodo.posicion_choza())
            self.lista_nodos.append(nodo)
            self.tablero.lista_nodos[self.tablero.lista_nodos.index(nodo)] = nodo

    def lanzar_dados(self, valor_izq, valor_der):
        ruta_izq = f'RUTA_DADO_{valor_izq}'
        ruta_der = f'RUTA_DADO_{valor_der}'
        self.label_dado_izq.setPixmap(QPixmap(os.path.join(*p.DADOS[ruta_izq])))
        self.label_dado_der.setPixmap(QPixmap(os.path.join(*p.DADOS[ruta_der])))

    def intercambio_cartas(self):
        pass

    def iniciar_turno(self):
        self.boton_dados.setEnabled(True)
        self.drag_choza.setEnabled(False)

    def actuar_turno(self):
        self.boton_dados.setEnabled(False)
        self.drag_choza.setEnabled(True)
        self.boton_terminar_turno.setEnabled(True)

    def dejar_de_actuar_turno(self, evento):
        self.drag_choza.setEnabled(False)
        self.senal_dejar_de_actuar_turno.emit(evento)

    def terminar_turno(self):
        self.senal_terminar_turno.emit()

    def iniciar_partida(self, jugador, lista_jugadores, lista_hexagonos):
        c = jugador.color
        if jugador.color == 'rojo':
            c = 'roja'
        llave_color = 'RUTA_CHOZA_' + c.upper()
        imagen = os.path.join(*tuple(p.CONSTRUCCIONES[llave_color]))
        self.drag_choza.setPixmap(QPixmap(imagen))

        if jugador in lista_jugadores:
            lista_jugadores.pop(lista_jugadores.index(jugador))
        for i in range(len(lista_jugadores)):
            self.lista_jugadores[i]['label_nombre'].setText(lista_jugadores[i].nombre)
            if lista_jugadores[i].color == 'azul':
                color = 'blue'
            elif lista_jugadores[i].color == 'verde':
                color = 'green'
            elif lista_jugadores[i].color == 'violeta':
                color = 'darkviolet'
            elif lista_jugadores[i].color == 'rojo':
                color = 'red'
            self.lista_jugadores[i]['label_nombre'].setStyleSheet(f'color: {color}')

        for i in range(len(self.lista_jugadores) - len(lista_jugadores)):
            a = len(self.lista_jugadores) - 1 - i
            self.lista_jugadores[a]['label_nombre'].setParent(None)
            self.lista_jugadores[a]['label_puntos'].setParent(None)
            self.lista_jugadores[a]['label_arcilla_user'].setParent(None)
            self.lista_jugadores[a]['label_madera_user'].setParent(None)
            self.lista_jugadores[a]['label_trigo_user'].setParent(None)
            self.lista_jugadores[a]['label_contador_madera'].setParent(None)
            self.lista_jugadores[a]['label_contador_arcilla'].setParent(None)
            self.lista_jugadores[a]['label_contador_trigo'].setParent(None)

        text = jugador.nombre + ' (Tu)'
        self.label_nombre_usuario.setText(text)
        if jugador.color == 'azul':
            color = 'blue'
        elif jugador.color == 'verde':
            color = 'green'
        elif jugador.color == 'violeta':
            color = 'darkviolet'
        elif jugador.color == 'rojo':
            color = 'red'
        self.label_nombre_usuario.setStyleSheet(f'color: {color}')

        for i in range(len(self.lista_labels_hexagonos)):
            if lista_hexagonos[i].materia_prima == 'arcilla':
                ruta = os.path.join(*p.MATERIAS_PRIMAS["RUTA_HEXAGONO_ARCILLA"])
            elif lista_hexagonos[i].materia_prima == 'madera':
                ruta = os.path.join(*p.MATERIAS_PRIMAS["RUTA_HEXAGONO_MADERA"])
            elif lista_hexagonos[i].materia_prima == 'trigo':
                ruta = os.path.join(*p.MATERIAS_PRIMAS["RUTA_HEXAGONO_TRIGO"])
            self.lista_labels_hexagonos[i].setPixmap(QPixmap(ruta))
            img_label_numero = QLabel(self)
            ruta = os.path.join(*p.MATERIAS_PRIMAS["RUTA_FICHA_NUMERO"])
            img_label_numero.setPixmap(QPixmap(ruta))
            img_label_numero.setMaximumSize(100, 100)
            lista_hexagonos[i].ubicar_imagen_numero(img_label_numero)
            img_label_numero.setScaledContents(True)

        for i in range(len(lista_hexagonos)):
            label = QLabel(str(lista_hexagonos[i].numero), self)
            label.setStyleSheet('font-size: 50px')
            lista_hexagonos[i].ubicar_label_numero(label)

    def actualizar_materias_primas(self, jugador, lista_jugadores):
        print('j mp', jugador.materias_primas)
        self.label_contador_arcilla.setText(': ' + str(jugador.materias_primas['arcilla']))
        self.label_contador_madera.setText(': ' + str(jugador.materias_primas['madera']))
        self.label_contador_trigo.setText(': ' + str(jugador.materias_primas['trigo']))

        if jugador in lista_jugadores:
            lista_jugadores.pop(lista_jugadores.index(jugador))
        for i in range(len(lista_jugadores)):
            self.lista_jugadores[i]['label_contador_arcilla'].setText(
                ': ' + str(lista_jugadores[i].materias_primas['arcilla']))
            self.lista_jugadores[i]['label_contador_madera'].setText(
                ': ' + str(lista_jugadores[i].materias_primas['madera']))
            self.lista_jugadores[i]['label_contador_trigo'].setText(
                ': ' + str(lista_jugadores[i].materias_primas['trigo']))
            # self.lista_jugadores[i][]

        # self.lista_jugadores.append({
        #         'label_nombre': label_nombre,
        #         'label_puntos': label_puntos,
        #         'label_arcilla_user': label_arcilla_user,
        #         'label_madera_user': label_madera_user,
        #         'label_trigo_user': label_trigo_user,
        #         'label_contador_madera': label_contador_madera,
        #         'label_contador_arcilla': label_contador_arcilla,
        #         'label_contador_trigo': label_contador_trigo
        #     })

    def preguntar_por_choza(self, valor_nodo):
        self.senal_preguntar_por_choza.emit(valor_nodo)

    def enviar_mensaje_error(self, mensaje):
        alerta = QErrorMessage(self)
        alerta.setWindowTitle('ERROR')
        alerta.showMessage(mensaje)

    def actualizar_label_turno(self, turno_jugador):
        self.label_turno_actual.setText(f'Turno de: {turno_jugador}')

    def actualizar_puntos_de_victoria(self, lista_puntos, jugador, lista_jugadores):
        if jugador in lista_jugadores:
            lista_jugadores.pop(lista_jugadores.index(jugador))
        for i in range(len(lista_jugadores)):
            for jug in lista_puntos:
                if jug['nombre'] == lista_jugadores[i].nombre:
                    self.lista_jugadores[i]['label_puntos'].setText(
                        'Puntos: ' + str(jug['puntos']))

        for j in lista_puntos:
            if j['nombre'] == jugador.nombre:
                self.label_puntos_victoria_usuario.setText(': ' + str(j['puntos']))
