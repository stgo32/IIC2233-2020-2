import sys
sys.path.append('..')

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, QTimer, pyqtSignal

from T02.back_end.zona_de_ritmo import CapturaFlechas, CreadorFlechas
from T02.parametros import (
    GENERADOR_PASOS_PRINCIPIANTE, GENERADOR_PASOS_AFICIONADO, GENERADOR_PASOS_MAESTRO,
    DURACION_PRINCIPIANTE, DURACION_AFICIONADO, DURACION_MAESTRO, PUNTOS_FLECHA,
    APROBACION_PRINCIPIANTE, APROBACION_AFICIONADO, APROBACION_MAESTRO, MINIMO_APROBACION,
    MINIMO_DINERO, PRECIO_PINGUIRIN, DINERO_INICIAL, DINERO_TRAMPA, FACTOR_FLECHAS_X2,
    FACTOR_FLECHAS_DORADAS
)


class Partida(QObject):

    senal_mostrar_resumen = pyqtSignal(int, int, int, int, int, int)
    senal_iniciacion_incompleta = pyqtSignal()

    def __init__(self, ventana_juego):
        super().__init__()
        self.juego = ventana_juego
        self._dinero = DINERO_INICIAL  # property
        self.canciones = []  # rutas canciones
        self.puntaje_acumulado = 0
        self.dificultad = None
        self.misma_partida = True
        self.color_ultimo_pingu = None
        self.gano = False
        self.jugando = False
        self.temporizador = 0
        # combos
        self.combo_actual = 0
        self.combo_mayor = 0
        # aprobacion
        self._aprobacion = 0
        # pasos
        self.pasos_correctos = 0
        self.pasos_incorrectos = 0
        # configuraciones nivel
        self.tiempo_nivel = None
        self.timer_crea_flecha = None
        # cantidad de flechas
        self.flechas_normales = 0
        self.flechas_x2 = 0
        self.flechas_doradas = 0
        self.flechas_hielo = 0
        self._suma_flechas = 0
        # operadores externos
        self.captura_flechas = CapturaFlechas(ventana_juego)
        self.crea_flechas = CreadorFlechas(ventana_juego)
        # senales
        self.captura_flechas.senal_paso_correcto.connect(self.receptor_pasos_correctos)
        self.captura_flechas.senal_tipo_flecha.connect(self.suma_flechas)

        for droper in self.juego.lista_dropers:
            self.captura_flechas.senal_bailar.connect(droper.bailar)
            droper.senal_get_color_pingu.connect(self.drop_pingu_color)
            droper.senal_gastar_dinero.connect(self.set_dinero)

        self.juego.pingu_amarillo.senal_enviar_color_pingu.connect(self.drag_pingu_color)
        self.juego.pingu_celeste.senal_enviar_color_pingu.connect(self.drag_pingu_color)
        self.juego.pingu_morado.senal_enviar_color_pingu.connect(self.drag_pingu_color)
        self.juego.pingu_verde.senal_enviar_color_pingu.connect(self.drag_pingu_color)
        self.juego.pingu_rojo.senal_enviar_color_pingu.connect(self.drag_pingu_color)

    @property
    def aprobacion(self):
        if self._aprobacion < MINIMO_APROBACION:
            self._aprobacion = MINIMO_APROBACION
        return self._aprobacion

    @aprobacion.setter
    def aprobacion(self, valor):
        if self._aprobacion < MINIMO_APROBACION:
            self.aprobacion = MINIMO_APROBACION
        else:
            self._aprobacion = valor

    @property
    def dinero(self):
        if self._dinero < MINIMO_DINERO:
            self._dinero = MINIMO_DINERO
        return self._dinero

    @dinero.setter
    def dinero(self, valor):
        if self._dinero < MINIMO_DINERO:
            self.dinero = MINIMO_DINERO
        else:
            self._dinero = valor
        self.juego.label_dinero_usuario.setText(f'Dinero: ${self.dinero}')
        for droper in self.juego.lista_dropers:
            droper.dinero = self.dinero

    def set_dinero(self):
        self.dinero -= PRECIO_PINGUIRIN
        self.juego.label_dinero_usuario.setText(f'Dinero: ${self.dinero}')

    def set_nombre_usuario(self, nombre):
        self.misma_partida = False
        self.dinero = DINERO_INICIAL
        self.juego.label_dinero_usuario.setText(f'Dinero: ${self.dinero}')
        self.usuario = nombre

    def inicio_de_nivel(self, dificultad, cancion):
        self.dificultad = self.juego.combo_box_dificultad.currentIndex()
        self.juego.media_player.setMedia(cancion)
        self.juego.media_player.play()
        self.gano = False
        self.jugando = True

        self.juego.pingu_amarillo.setEnabled(False)
        self.juego.pingu_celeste.setEnabled(False)
        self.juego.pingu_morado.setEnabled(False)
        self.juego.pingu_rojo.setEnabled(False)
        self.juego.pingu_verde.setEnabled(False)

        if self.timer_crea_flecha is None:
            self.timer_crea_flecha = QTimer(self)
            if self.dificultad == 0:
                self.timer_crea_flecha.setInterval(GENERADOR_PASOS_PRINCIPIANTE)
            elif self.dificultad == 1:
                self.timer_crea_flecha.setInterval(GENERADOR_PASOS_AFICIONADO)
            elif self.dificultad == 2:
                self.timer_crea_flecha.setInterval(GENERADOR_PASOS_MAESTRO)
            self.timer_crea_flecha.timeout.connect(self.crear_flechas)
            self.timer_crea_flecha.start()
        if self.tiempo_nivel is None:
            self.tiempo_nivel = QTimer(self)
            self.tiempo_nivel.setInterval(1000)
            if self.dificultad == 0:
                self.temporizador = DURACION_PRINCIPIANTE
            elif self.dificultad == 1:
                self.temporizador = DURACION_AFICIONADO
            elif self.dificultad == 2:
                self.temporizador = DURACION_MAESTRO
            self.tiempo_nivel.timeout.connect(self.progreso_de_nivel)
            self.tiempo_nivel.start()

    def progreso_de_nivel(self):
        self.temporizador -= 1
        print(self.temporizador)
        if self.dificultad == 0:
            duracion = DURACION_PRINCIPIANTE
        elif self.dificultad == 1:
            duracion = DURACION_AFICIONADO
        elif self.dificultad == 2:
            duracion = DURACION_MAESTRO
        self.aprobacion = self.calcular_aprobacion()
        self.juego.barra_progreso.setValue(100*(duracion-self.temporizador)/duracion)
        self.juego.barra_aprobacion.setValue(self.aprobacion)
        ''' TERMINO NIVEL '''
        if self.temporizador == 0:
            self.termino_de_nivel()

    def termino_de_nivel(self):
        print('tiempo terminado')
        self.jugando = False
        puntaje = self.calcular_puntaje()
        self.dinero += puntaje
        print('puntaje:', puntaje)
        self.juego.barra_aprobacion.setValue(0)
        self.juego.barra_progreso.setValue(0)
        self.juego.combo_actual.setText('Combo:')
        self.juego.boton_comenzar.setEnabled(True)
        self.juego.combo_box_cancion.setEnabled(True)
        self.juego.combo_box_dificultad.setEnabled(True)
        self.juego.media_player.pause()
        print('aprobacion:', self.aprobacion)
        print('dificultad:', self.dificultad)
        self.senal_mostrar_resumen.emit(puntaje, self.puntaje_acumulado,
                                        self.combo_mayor, self.pasos_incorrectos,
                                        self.aprobacion, self.dificultad)
        self.gano = True
        if self.dificultad == 0:
            if self.aprobacion < APROBACION_PRINCIPIANTE:
                self.juego.combo_mayor.setText('Mayor Combo:')
                self.juego.hide()
                self.gano = False
                for drop_pingu in self.juego.lista_dropers:
                    drop_pingu.color = None
                    drop_pingu.setPixmap(QPixmap())
        elif self.dificultad == 1:
            if self.aprobacion < APROBACION_AFICIONADO:
                self.juego.combo_mayor.setText('Mayor Combo:')
                self.juego.hide()
                self.gano = False
                for drop_pingu in self.juego.lista_dropers:
                    drop_pingu.color = None
                    drop_pingu.setPixmap(QPixmap())
        elif self.dificultad == 2:
            if self.aprobacion < APROBACION_MAESTRO:
                self.juego.combo_mayor.setText('Mayor Combo:')
                self.juego.hide()
                self.gano = False
                for drop_pingu in self.juego.lista_dropers:
                    drop_pingu.color = None
                    drop_pingu.setPixmap(QPixmap())
        self.resetear_partida()

    def resetear_partida(self):
        if not self.gano:
            print('ACUMULADO', self.puntaje_acumulado)
            self.puntaje_acumulado = 0
            self.combo_mayor = 0

        self.tiempo_nivel.stop()
        self.timer_crea_flecha.stop()
        self.tiempo_nivel = None
        self.timer_crea_flecha = None
        self.gano = False
        self.jugando = False

        flechas = set(self.juego.flechas)
        for flecha in flechas:
            self.juego.flechas.pop(self.juego.flechas.index(flecha))
            flecha.label.setParent(None)
            flecha.stop()

        self.juego.pingu_amarillo.setEnabled(True)
        self.juego.pingu_celeste.setEnabled(True)
        self.juego.pingu_morado.setEnabled(True)
        self.juego.pingu_rojo.setEnabled(True)
        self.juego.pingu_verde.setEnabled(True)

        self.aprobacion = 0
        self.pasos_correctos = 0
        self.pasos_incorrectos = 0
        self.combo_actual = 0
        self.flechas_normales = 0
        self.flechas_x2 = 0
        self.flechas_doradas = 0
        self.flechas_hielo = 0
        self._suma_flechas = 0

    def capturar_flechas(self, lista_teclas):
        self.captura_flechas.capturar(lista_teclas)

    def crear_flechas(self):
        self.crea_flechas.creador_flechas(self.dificultad)

    def calcular_puntaje(self):
        puntaje = self.combo_mayor * self._suma_flechas * PUNTOS_FLECHA
        self.puntaje_acumulado += puntaje
        self.guardar_puntaje(self.puntaje_acumulado)
        return puntaje

    def receptor_pasos_correctos(self, paso_correcto):
        if paso_correcto:
            self.pasos_correctos += 1
        else:
            self.pasos_incorrectos += 1
        self.combos(paso_correcto)

    def calcular_aprobacion(self):
        pasos_totales = self.pasos_correctos + self.pasos_incorrectos
        if pasos_totales != 0:
            aprobacion = 100 * (self.pasos_correctos - self.pasos_incorrectos) / pasos_totales
        else:
            aprobacion = 0
        return aprobacion

    def combos(self, paso_correcto):
        if paso_correcto:
            self.combo_actual += 1
            self.juego.combo_actual.setText(f'Combo: {self.combo_actual}')
        else:
            self.combo_actual = 0
        if self.combo_actual > self.combo_mayor:
            self.combo_mayor = self.combo_actual
            self.juego.combo_mayor.setText(f'Mayor Combo: {self.combo_mayor}')

    def suma_flechas(self, tipo_flecha):
        if tipo_flecha == 'normal':
            self.flechas_normales += 1
        elif tipo_flecha == 'x2':
            self.flechas_x2 += 1
        elif tipo_flecha == 'dorada':
            self.flechas_doradas += 1
        elif tipo_flecha == 'hielo':
            self.flechas_hielo += 1
        self._suma_flechas = (self.flechas_normales +
                              self.flechas_x2 * FACTOR_FLECHAS_X2 +
                              self.flechas_doradas * FACTOR_FLECHAS_DORADAS +
                              self.flechas_hielo)

    def guardar_puntaje(self, puntaje):
        archivo = open('ranking.txt', 'rt')
        puntajes = archivo.readlines()
        archivo.close()
        archivo = open('ranking.txt', 'w')
        if self.misma_partida:
            for i in range(len(puntajes) - 1):
                archivo.write(puntajes[i])
            archivo.write(f'{self.usuario},{self.puntaje_acumulado}')
        else:
            self.misma_partida = True
            for i in range(len(puntajes)):
                archivo.write(puntajes[i])
            archivo.write(f'\n{self.usuario},{self.puntaje_acumulado}')
        archivo.close()

    def drop_pingu_color(self, drop_label):
        if self.color_ultimo_pingu is None:
            pass
        else:
            drop_label.color = self.color_ultimo_pingu

    def drag_pingu_color(self, color):
        self.color_ultimo_pingu = color
        print('color', color)

    def cheat_code_money(self):
        self.dinero = DINERO_TRAMPA

    def cheat_code_nivel(self):
        print('CHEAT CODE NIV')
        print(self.aprobacion)
        if self.jugando:
            puntaje = self.calcular_puntaje()
            self.senal_mostrar_resumen.emit(puntaje, self.puntaje_acumulado,
                                            self.combo_mayor, self.pasos_incorrectos,
                                            self.aprobacion, self.dificultad)
            self.juego.barra_aprobacion.setValue(self.aprobacion)
            self.juego.media_player.pause()
            self.juego.combo_actual.setText('Combo:')
            self.juego.boton_comenzar.setEnabled(True)
            self.juego.combo_box_cancion.setEnabled(True)
            self.juego.combo_box_dificultad.setEnabled(True)
            self.gano = True
            if self.dificultad == 0:
                if self.aprobacion < APROBACION_PRINCIPIANTE:
                    self.juego.combo_mayor.setText('Mayor Combo:')
                    self.juego.hide()
                    self.gano = False
                    for drop_pingu in self.juego.lista_dropers:
                        drop_pingu.color = None
                        drop_pingu.setPixmap(QPixmap())
            elif self.dificultad == 1:
                if self.aprobacion < APROBACION_AFICIONADO:
                    self.juego.combo_mayor.setText('Mayor Combo:')
                    self.juego.hide()
                    self.gano = False
                    for drop_pingu in self.juego.lista_dropers:
                        drop_pingu.color = None
                        drop_pingu.setPixmap(QPixmap())
            elif self.dificultad == 2:
                if self.aprobacion < APROBACION_MAESTRO:
                    self.juego.combo_mayor.setText('Mayor Combo:')
                    self.juego.hide()
                    self.gano = False
                    for drop_pingu in self.juego.lista_dropers:
                        drop_pingu.color = None
                        drop_pingu.setPixmap(QPixmap())
            if self.gano:
                self.juego.barra_progreso.setValue(100)
            elif not self.gano:
                self.juego.barra_progreso.setValue(0)
            self.resetear_partida()

    def pausar(self, accion):
        if self.jugando and accion == 'Pausar':
            print('pausando')
            self.timer_crea_flecha.stop()
            self.tiempo_nivel.stop()
            self.juego.media_player.pause()
            for flecha in self.juego.flechas:
                flecha.stop()
        if self.jugando and accion == 'Play':
            self.timer_crea_flecha.start()
            self.tiempo_nivel.start()
            self.juego.media_player.play()
            for flecha in self.juego.flechas:
                flecha.start()
