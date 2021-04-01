from random import choice


class Jugador:

    def __init__(self, socket_cliente, address):
        self.socket_cliente = socket_cliente
        self.address = address

        self.nombre = None
        self.id = 0
        self.color = None

        self.puntos_de_victoria = 0

        self.siguiente = None  # jugador
        self.turno = -1

    def generar_nombre(self, nombres):
        nombre = choice(nombres)
        self.nombre = nombre
        return nombre
