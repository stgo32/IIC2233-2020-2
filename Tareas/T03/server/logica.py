import json

from threading import Lock
from random import choice, shuffle

from jugador import Jugador
from banco import Banco
from parametros import p


class Logica():

    lock_lista_nombres = Lock()
    lock_id_jugador = Lock()
    lock_manejar_mensaje = Lock()
    lock_colores = Lock()
    lock_pasar_turno = Lock()
    lock_choza_inicial = Lock()
    lock_choza_regular = Lock()

    def __init__(self, server):
        self.server = server
        self.lista_nombres = self.cargar_nombres()
        self.banco = None

        self.colores = ['azul', 'rojo', 'verde', 'violeta']

        self.id_jugador = 0
        self.contador_inicializador_partida = 0

    def cargar_nombres(self, ruta='nombres.txt'):
        with open(ruta, 'rt') as archivo:
            nombres = archivo.readlines()
        for i in range(len(nombres)):
            if '\n' in nombres[i]:
                nombre = nombres[i][:-1]
                nombres[i] = nombre
        return nombres

    def instanciar_jugador(self, socket_cliente, address):
        with self.lock_lista_nombres:
            jugador = Jugador(socket_cliente, address)
            nombre = jugador.generar_nombre(self.lista_nombres)
            self.lista_nombres.pop(self.lista_nombres.index(f'{nombre}'))

        with self.lock_id_jugador:
            jugador.id = self.id_jugador
            self.id_jugador += 1

        with self.lock_colores:
            jugador.color = self.colores.pop()

        return jugador

    def manejar_mensaje(self, mensaje, jugador, lista_jugadores):
        # with self.lock_manejar_mensaje:
        evento = mensaje['evento']
        try:
            detalles = mensaje['detalles']
        except KeyError:
            pass
        lista_respuestas = []

        if evento == 'Intento de conexion':
            grafos = self.cargar_archivo_json(p.RUTA_GRAFOS)
            respuesta = {
                'receptor': 'individual',
                'mensaje': {
                    'comando': 'intento_conexion',
                    'grafos': grafos,
                    'parametros': self.cargar_archivo_json('parametros.json')
                }}
            lista_respuestas.append(respuesta)

        elif evento == 'Conexion exitosa':
            respuesta1 = {
                'receptor': 'individual',
                'mensaje': {
                    'comando': 'login',
                    'username': jugador.nombre,
                    'id': jugador.id,
                    'color': jugador.color
                }}
            lista_respuestas.append(respuesta1)
            respuesta2 = {
                'receptor': 'todos',
                'mensaje': {
                    'comando': 'agregar_jugador',
                    'lista_jugadores':
                    [{'nombre': jugador.nombre, 'id': jugador.id, 'color': jugador.color}
                     for jugador in lista_jugadores]
                }}
            lista_respuestas.append(respuesta2)
            if len(lista_jugadores) == p.CANTIDAD_JUGADORES_PARTIDA:
                respuesta3 = self.configurar_inicio_partida(lista_jugadores)
                self.banco = Banco(lista_jugadores)  # se configura el orden de turnos
                lista_respuestas.append(respuesta3)

        elif evento == 'Inicio de partida':
            self.contador_inicializador_partida += 1
            if self.contador_inicializador_partida == p.CANTIDAD_JUGADORES_PARTIDA:
                self.comenzar_turnos(lista_jugadores)

        elif evento == 'Cambio turno':
            with self.lock_pasar_turno:
                lista_puntos = [{'nombre': j.nombre, 'puntos': j.puntos_de_victoria}
                                for j in self.banco.lista_jugadores]
                print('')
                self.server.log(self.banco.jugador_siguiente.nombre,
                                {'evento': 'Puntos victoria', 'detalles': lista_puntos})
                self.server.log(self.banco.jugador_siguiente.nombre,
                                {'evento': evento, 'detalles': self.banco.turno})
                if self.banco.turno < 1:
                    respuesta = {
                        'receptor': 'todos',
                        'mensaje': {
                            'comando': 'cambio_turno',
                            'turno_jugador': self.banco.jugador_siguiente.nombre,
                            'accion': 'choza_inicial',
                            'ganancia': p.GANANCIA_MATERIA_PRIMA,
                            'puntos': p.PUNTO_DE_VICTORIA
                        }}
                    lista_respuestas.append(respuesta)
                elif self.banco.turno >= 1:
                    respuesta = {
                        'receptor': 'todos',
                        'mensaje': {
                            'comando': 'cambio_turno',
                            'turno_jugador': self.banco.jugador_siguiente.nombre,
                            'accion': 'jugar',
                            'ganancia': p.GANANCIA_MATERIA_PRIMA,
                            'puntos': p.PUNTO_DE_VICTORIA,
                            'puntos_de_victoria': lista_puntos
                        }}
                    lista_respuestas.append(respuesta)
                self.banco.contador_turnos += 1
                self.banco.set_siguiente()

        elif evento == 'Choza inicial':
            with self.lock_choza_inicial:
                self.banco.contador_chozas += 1
                if type(detalles).__name__ == 'dict':
                    self.banco.sumar_puntos_victoria(jugador, 'choza')
                    respuesta = {
                        'receptor': 'todos',
                        'mensaje': {
                            'comando': 'choza',
                            'tipo': 'inicial',
                            'jugador': detalles['jugador'],
                            'nodo': detalles['nodo'],
                            'ganancia': p.GANANCIA_MATERIA_PRIMA
                        }}
                    lista_respuestas.append(respuesta)
                else:
                    if self.banco.contador_chozas == p.CANTIDAD_JUGADORES_PARTIDA:
                        self.pasar_turno(lista_jugadores)

        elif evento == 'Choza':
            with self.lock_choza_regular:
                if type(detalles).__name__ == 'dict':
                    self.banco.sumar_puntos_victoria(jugador, 'choza')
                    ganador = self.banco.revisar_puntos_victoria()
                    if ganador is None:
                        costo = {
                            'arcilla': p.CANTIDAD_ARCILLA_CHOZA,
                            'madera': p.CANTIDAD_MADERA_CHOZA,
                            'trigo': p.CANTIDAD_TRIGO_CHOZA
                        }
                        respuesta = {
                            'receptor': 'todos',
                            'mensaje': {
                                'comando': 'choza',
                                'tipo': 'regular',
                                'jugador': detalles['jugador'],
                                'nodo': detalles['nodo'],
                                'costo_choza': costo
                            }}
                        lista_respuestas.append(respuesta)
                    else:
                        self.fin_del_juego(ganador)

        elif evento == 'Lanzar dados':
            respuesta = {
                'receptor': 'todos',
                'mensaje': {
                    'comando': 'lanzar_dados',
                    'dados': detalles
                }}
            lista_respuestas.append(respuesta)

        elif evento == 'Fin del juego':
            respuesta = {
                'receptor': 'todos',
                'mensaje': {
                    'comando': 'fin_juego',
                    'lista_puntos': detalles
                }}
            lista_respuestas.append(respuesta)

        elif evento == 'Mensaje chat':
            text = f'> {jugador.nombre}: {detalles}'
            respuesta = {
                'receptor': 'todos',
                'mensaje': {
                    'comando': 'mensaje_chat',
                    'texto': text
                }}
            lista_respuestas.append(respuesta)

        return lista_respuestas

    def cargar_archivo_json(self, ruta):
        with open(ruta, 'rt') as archivo:
            grafos = json.load(archivo)
        return grafos

    def configurar_inicio_partida(self, lista_jugadores):
        cuatro = ['madera', 'arcilla', 'trigo']
        lista_materias = ['madera' for i in range(3)] + ['arcilla' for i in range(3)] + \
            ['trigo' for i in range(3)]
        lista_materias.append(choice(cuatro))
        shuffle(lista_materias)
        dict_hexagonos = {i: lista_materias[i] for i in range(p.CANTIDAD_HEXAGONOS)}

        lista_numeros = p.LISTA_NUMEROS
        shuffle(lista_numeros)

        respuesta = {
            'receptor': 'todos',
            'mensaje': {
                'comando': 'iniciar_partida',
                'materias_primas': dict_hexagonos,
                'num_hexagonos': lista_numeros
                }
        }
        return respuesta

    def comenzar_turnos(self, lista_jugadores):
        mensaje = {'evento': 'Cambio turno'}
        jugador = self.banco.jugador_siguiente
        lista_respuestas = self.manejar_mensaje(mensaje, jugador, lista_jugadores)
        self.server.enviar_lista_respuestas(jugador, lista_respuestas)

    def pasar_turno(self, lista_jugadores):
        mensaje = {'evento': 'Cambio turno'}
        jugador = self.banco.jugador_siguiente
        lista_respuestas = self.manejar_mensaje(mensaje, jugador, lista_jugadores)
        self.server.enviar_lista_respuestas(jugador, lista_respuestas)

    def fin_del_juego(self, ganador):
        lista_puntos = []
        lista_jug = []
        lista_p = [j.puntos_de_victoria for j in self.banco.lista_jugadores]
        lista_p.sort(reverse=True)
        for puntaje in lista_p:
            for j in self.banco.lista_jugadores:
                if j.puntos_de_victoria == puntaje and j not in lista_jug:
                    lista_jug.append(j)
        for j in lista_jug:
            lista_puntos.append({'nombre': j.nombre, 'puntos': j.puntos_de_victoria})
        mensaje = {'evento': 'Fin del juego', 'detalles': lista_puntos}
        self.server.log(ganador.nombre, mensaje)
        lista_respuestas = self.manejar_mensaje(mensaje, ganador, self.banco.lista_jugadores)
        self.server.enviar_lista_respuestas(ganador, lista_respuestas)
