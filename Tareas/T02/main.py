import sys
from PyQt5.QtWidgets import QApplication

from front_end.front_inicio import fInicio
from front_end.front_ranking import fRanking
from front_end.front_juego import fJuego
from front_end.front_resumen import fResumen
from back_end.back_ranking import bRanking
from back_end.partida import Partida

from parametros import (MIN_SIZE_INICIO, MIN_SIZE_RANKING, MIN_SIZE_JUEGO, MIN_SIZE_RESUMEN,
                        APP_STYLE_SHEET)


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    sys.__excepthook__ = hook

    app = QApplication([])
    app.setStyleSheet(APP_STYLE_SHEET)

    # instancias de ventanas
    ventana_inicio = fInicio(MIN_SIZE_INICIO)
    ventana_ranking = fRanking(MIN_SIZE_RANKING)
    ventana_juego = fJuego(MIN_SIZE_JUEGO)
    ventana_resumen = fResumen(MIN_SIZE_RESUMEN)

    # instancias de clases logicas
    logica_ranking = bRanking()
    partida = Partida(ventana_juego)

    ''' conectar senales '''
    # senales ranking
    ventana_inicio.senal_calcular_ranking.connect(logica_ranking.calcular_ranking)
    logica_ranking.senal_enviar_ranking.connect(ventana_ranking.actualizar_ranking)

    # senales partida
    ventana_juego.senal_nombre_usuario.connect(partida.set_nombre_usuario)
    ventana_juego.senal_inicio_de_nivel.connect(partida.inicio_de_nivel)
    ventana_juego.senal_capturar_flecha.connect(partida.capturar_flechas)
    ventana_juego.senal_resetear_partida.connect(partida.resetear_partida)
    ventana_juego.senal_cheat_code_money.connect(partida.cheat_code_money)
    ventana_juego.senal_cheat_code_nivel.connect(partida.cheat_code_nivel)
    ventana_juego.senal_pausar.connect(partida.pausar)

    partida.senal_iniciacion_incompleta.connect(ventana_juego.iniciacion_incompleta)

    # senañes entre ventanas
    ventana_ranking.senal_volver_inicio = ventana_inicio.senal_volver_de_ranking
    ventana_inicio.senal_comenzar = ventana_juego.senal_mostrar_juego
    ventana_juego.senal_volver_inicio = ventana_inicio.senal_volver_de_juego
    partida.senal_mostrar_resumen = ventana_resumen.senal_mostrar_resumen
    ventana_resumen.senal_volver_inicio = ventana_inicio.senal_volver_de_resumen

    sys.exit(app.exec_())
