import sys
sys.path.append('..')

from random import randint, random
from PyQt5.QtWidgets import (
    QLabel
)
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QPixmap

from T02.parametros import (
    MAX_TAMANO_FLECHA, STYLE_CUADROS_FLECHA_IMPAR, STYLE_CUADROS_FLECHA_PAR, FLECHA_IZQUIERDA,
    FLECHA_ARRIBA, FLECHA_ABAJO, FLECHA_DERECHA, PROB_PASO_SIMPLE, PROB_PASO_DOBLE_AFICIONADO,
    PROB_PASO_DOBLE_MAESTRO, PROB_PASO_TRIPLE, VELOCIDAD_FLECHA, PROB_FLECHA_NORMAL,
    PROB_FLECHA_X2, PROB_FLECHA_DORADA, PROB_FLECHA_HIELO, TIPOS_FLECHAS, ALTO_ZONA_ESTCA,
    BORDE_IZQUIERDA, BORDE_INFERIOR
)

#  codigo de Flecha inspirado en el ultimo ejemplo del
#  primer notebook de la semana 10 (el de las comidas)


class Flecha(QTimer):

    senal_actualizar = pyqtSignal(QLabel, int, int)

    def __init__(self, parent, limite_x, limite_y, columna, pasos, tipo):
        super().__init__()
        self.columna = columna
        self.pasos = pasos
        self.tipo = tipo

        self.ruta_imagen = TIPOS_FLECHAS[str(tipo)][columna]

        self.label = QLabel(parent)
        self.label.setPixmap(QPixmap(self.ruta_imagen))
        self.label.setScaledContents(True)
        self.label.setVisible(True)

        self.limite_x = limite_x
        self.limite_y = limite_y

        if self.tipo == 'dorada':
            self.velocidad = VELOCIDAD_FLECHA * 1.5
        else:
            self.velocidad = VELOCIDAD_FLECHA

        self.__posicion = (0, 0)
        self.posicion = (MAX_TAMANO_FLECHA*self.columna + 5, 150)
        self.label.setGeometry(self.posicion[0], ALTO_ZONA_ESTCA,
                               MAX_TAMANO_FLECHA, MAX_TAMANO_FLECHA)
        self.label.show()

        self.setInterval(100)
        self.timeout.connect(self.run)

        self.start()

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, valor):
        self.__posicion = valor
        self.senal_actualizar.emit(self.label, *self.posicion)

    def run(self):
        if self.posicion[0] < self.limite_x and self.posicion[1] < self.limite_y:
            nuevo_x = MAX_TAMANO_FLECHA*self.columna + BORDE_IZQUIERDA
            nuevo_y = self.posicion[1] + self.velocidad
            self.posicion = (nuevo_x, nuevo_y)


class CapturaFlechas(QObject):

    senal_paso_correcto = pyqtSignal(bool)
    senal_tipo_flecha = pyqtSignal(str)
    senal_bailar = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def capturar(self, lista_teclas):
        columnas = self.verificar_columnas(lista_teclas)
        flechas = set(self.parent.flechas)
        flechas_correctas = []
        print(columnas)
        for columna in columnas:
            for flecha in flechas:
                if self.zona_de_captura(flecha, columna):
                    flechas_correctas.append(flecha)
        pasos = self.verificar_pasos(flechas_correctas)
        print(flechas_correctas)
        if len(flechas_correctas) == pasos and len(flechas_correctas) != 0:
            self.senal_bailar.emit(columnas)
            self.senal_paso_correcto.emit(True)
            for flecha in flechas_correctas:
                self.senal_tipo_flecha.emit(flecha.tipo)
                self.style_paso(flecha.columna, 'blue')
                print('correcto')
            for flecha in flechas_correctas:
                self.parent.flechas.pop(self.parent.flechas.index(flecha))
                flecha.label.setParent(None)
                flecha.stop()
        else:
            for columna in columnas:
                self.style_paso(columna, 'red')
            self.senal_paso_correcto.emit(False)
            print('incorrecto')
        self.timer = QTimer(self.parent)
        self.timer.setSingleShot(True)
        self.timer.setInterval(100)
        self.columnas = columnas
        self.timer.timeout.connect(self.style_frame_neutro)
        self.timer.start()

    def verificar_columnas(self, lista_teclas):
        columnas = []
        if FLECHA_IZQUIERDA in lista_teclas:
            columnas.append(0)
        if FLECHA_ARRIBA in lista_teclas:
            columnas.append(1)
        if FLECHA_ABAJO in lista_teclas:
            columnas.append(2)
        if FLECHA_DERECHA in lista_teclas:
            columnas.append(3)
        return columnas

    def zona_de_captura(self, flecha, columna):
        if (MAX_TAMANO_FLECHA*columna + BORDE_IZQUIERDA <= flecha.posicion[0] <=
                MAX_TAMANO_FLECHA*columna + BORDE_IZQUIERDA*2 and
                self.parent.height() - MAX_TAMANO_FLECHA*2 - BORDE_INFERIOR <=
                flecha.posicion[1] <= self.parent.height() - BORDE_INFERIOR):
            return True
        else:
            return False

    def verificar_pasos(self, flechas_correctas):
        try:
            paso = flechas_correctas[0].pasos
            for i in range(len(flechas_correctas)):
                if paso != flechas_correctas[i].pasos:
                    return False
            return paso
        except IndexError:
            return False

    def style_paso(self, columna, color):
        if columna == 0:
            self.parent.cuadro_left.setStyleSheet(f'background-color: {color}')
        elif columna == 1:
            self.parent.cuadro_up.setStyleSheet(f'background-color: {color}')
        elif columna == 2:
            self.parent.cuadro_down.setStyleSheet(f'background-color: {color}')
        elif columna == 3:
            self.parent.cuadro_right.setStyleSheet(f'background-color: {color}')

    def style_frame_neutro(self):
        for columna in self.columnas:
            if columna == 0:
                self.parent.cuadro_left.setStyleSheet(STYLE_CUADROS_FLECHA_IMPAR)
            elif columna == 1:
                self.parent.cuadro_up.setStyleSheet(STYLE_CUADROS_FLECHA_PAR)
            elif columna == 2:
                self.parent.cuadro_down.setStyleSheet(STYLE_CUADROS_FLECHA_IMPAR)
            elif columna == 3:
                self.parent.cuadro_right.setStyleSheet(STYLE_CUADROS_FLECHA_PAR)


class CreadorFlechas:

    def __init__(self, parent):
        self.parent = parent

    def creador_flechas(self, dificultad):
        probabilidad_de_paso = random()
        if dificultad == 0:
            pasos = 1
        elif dificultad == 1:
            if probabilidad_de_paso < PROB_PASO_SIMPLE:
                pasos = 1
            elif probabilidad_de_paso <= PROB_PASO_SIMPLE + PROB_PASO_DOBLE_AFICIONADO:
                pasos = 2
        elif dificultad == 2:
            if probabilidad_de_paso < PROB_PASO_SIMPLE:
                pasos = 1
            elif probabilidad_de_paso < PROB_PASO_SIMPLE + PROB_PASO_DOBLE_MAESTRO:
                pasos = 2
            elif (probabilidad_de_paso <= PROB_PASO_SIMPLE +
                  PROB_PASO_DOBLE_MAESTRO + PROB_PASO_TRIPLE):
                pasos = 3
        probabilidad_tipo_flecha = random()
        if probabilidad_tipo_flecha < PROB_FLECHA_NORMAL:
            tipo = 'normal'
        elif probabilidad_tipo_flecha < PROB_FLECHA_NORMAL + PROB_FLECHA_X2:
            tipo = 'x2'
        elif probabilidad_tipo_flecha < PROB_FLECHA_NORMAL + PROB_FLECHA_X2 + PROB_FLECHA_DORADA:
            tipo = 'dorada'
        elif (probabilidad_tipo_flecha <= PROB_FLECHA_NORMAL + PROB_FLECHA_X2 +
              PROB_FLECHA_DORADA + PROB_FLECHA_HIELO):
            tipo = 'hielo'
        columnas = []
        while len(columnas) < pasos:
            columna = randint(0, 3)
            if columna not in columnas:
                columnas.append(columna)
        for columna in columnas:
            nueva_flecha = Flecha(self.parent, self.parent.width(),
                                  self.parent.height(), columna, pasos, tipo)
            nueva_flecha.senal_actualizar.connect(self.parent.actualizar_label)
            self.parent.flechas.append(nueva_flecha)
