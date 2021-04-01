from random import shuffle

from parametros import p


class Banco:

    def __init__(self, lista_jugadores):
        self.lista_jugadores = lista_jugadores

        self.turno = -1
        self._contador_turnos = 1
        self._contador_chozas = 0

        self.set_orden_turnos()

    @property
    def contador_turnos(self):
        return self._contador_turnos

    @contador_turnos.setter
    def contador_turnos(self, valor):
        if self._contador_turnos == p.CANTIDAD_JUGADORES_PARTIDA:
            self.turno += 1
            self._contador_turnos = 1
        else:
            self._contador_turnos = valor

    @property
    def contador_chozas(self):
        return self._contador_chozas

    @contador_chozas.setter
    def contador_chozas(self, valor):
        if self._contador_chozas == p.CANTIDAD_JUGADORES_PARTIDA:
            self._contador_chozas = 1
        else:
            self._contador_chozas = valor

    def set_orden_turnos(self):
        shuffle(self.lista_jugadores)
        for i in range(len(self.lista_jugadores)):
            if i == p.CANTIDAD_JUGADORES_PARTIDA - 1:
                self.lista_jugadores[i].siguiente = self.lista_jugadores[0]
            else:
                self.lista_jugadores[i].siguiente = self.lista_jugadores[i + 1]
        self.jugador_siguiente = self.lista_jugadores[0]

    def set_siguiente(self):
        self.jugador_siguiente = self.jugador_siguiente.siguiente

    def sumar_puntos_victoria(self, jugador, razon):
        if razon == 'choza':
            jugador.puntos_de_victoria += p.PUNTO_DE_VICTORIA
            self.lista_jugadores[self.lista_jugadores.index(jugador)] = jugador

    def revisar_puntos_victoria(self):
        ganador = None
        for j in self.lista_jugadores:
            if j.puntos_de_victoria >= p.PUNTOS_PARA_VICTORIA:
                ganador = j
        return ganador

        
