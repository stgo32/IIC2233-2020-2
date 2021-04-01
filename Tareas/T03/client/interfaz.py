from PyQt5.QtCore import pyqtSignal, QObject

from interfaces_front_end.sala_de_espera import VentanaSalaEspera
from interfaces_front_end.sala_de_juego import VentanaSalaJuego
from interfaces_front_end.fin_de_partida import VentanaFinPartida
from interfaces_front_end.chat import VentanaChat

from interfaces_back_end.sala_de_espera import BackSalaEspera
from interfaces_back_end.sala_de_juego import BackSalaJuego
from interfaces_back_end.tablero import Tablero
from interfaces_back_end.jugador import Usuario, Jugador

from parametros import p


class Controlador(QObject):

    senal_generar_tablero = pyqtSignal()
    senal_eliminar_jugador_sala_espera = pyqtSignal(int)
    senal_mostrar_sala_juego = pyqtSignal()
    senal_iniciar_partida = pyqtSignal(Usuario, list, list)
    senal_actualizar_labels_materias_primas = pyqtSignal(Usuario, list)
    senal_lanzar_dados = pyqtSignal()
    senal_iniciar_turno = pyqtSignal()
    senal_actuar_turno = pyqtSignal()
    senal_enviar_mensaje_error = pyqtSignal(str)
    senal_actualizar_puntos_de_victoria = pyqtSignal(list, Usuario, list)
    senal_actualizar_label_turno = pyqtSignal(str)
    senal_ir_a_fin_juego = pyqtSignal(list)
    senal_fin_juego = pyqtSignal(bool, list)
    senal_recibir_mensaje_chat = pyqtSignal(str)

    def __init__(self, client):
        super().__init__()
        self.cliente = client
        self.usuario = None  # Usuario
        self.lista_jugadores = []  # list Jugador
        self.parametros_server = None

        self.ventana_sala_espera = VentanaSalaEspera(tuple(p.SIZE_VENTANA_ESPERA))
        self.ventana_sala_juego = VentanaSalaJuego(tuple(p.SIZE_VENTANA_JUEGO))
        self.ventana_chat = VentanaChat()
        self.ventana_sala_juego.tablero = Tablero()
        self.ventana_fin_partida = VentanaFinPartida(tuple(p.SIZE_VENTANA_FIN))

        self.back_sala_espera = BackSalaEspera()
        self.back_sala_juego = BackSalaJuego()

        self.partida_terminada = False

        # senales sala espera
        self.back_sala_espera.senal_agregar_jugador.connect(
            self.ventana_sala_espera.agregar_jugador)
        self.senal_eliminar_jugador_sala_espera.connect(self.ventana_sala_espera.eliminar_jugador)
        # senales chat
        self.ventana_sala_espera.senal_abrir_chat.connect(self.mostrar_chat)
        self.ventana_sala_juego.senal_abrir_chat.connect(self.mostrar_chat)
        self.ventana_chat.senal_enviar_texto.connect(self.cliente.enviar)
        self.senal_recibir_mensaje_chat.connect(self.ventana_chat.add_message)
        # senales sala juego
        self.senal_enviar_mensaje_error.connect(self.ventana_sala_juego.enviar_mensaje_error)
        self.senal_generar_tablero.connect(self.ventana_sala_juego.generar_tablero)
        self.senal_mostrar_sala_juego.connect(self.mostrar_sala_juego)
        self.senal_iniciar_partida.connect(self.ventana_sala_juego.iniciar_partida)

        self.ventana_sala_juego.senal_lanzar_dados.connect(self.back_sala_juego.lanzar_dados)
        self.back_sala_juego.senal_dados_lanzados.connect(self.ventana_sala_juego.lanzar_dados)

        self.senal_actualizar_labels_materias_primas.connect(
            self.ventana_sala_juego.actualizar_materias_primas)
        self.senal_actualizar_label_turno.connect(self.ventana_sala_juego.actualizar_label_turno)
        self.senal_actualizar_puntos_de_victoria.connect(
            self.ventana_sala_juego.actualizar_puntos_de_victoria)

        self.back_sala_juego.senal_actuar.connect(self.actuar)
        self.senal_iniciar_turno.connect(self.ventana_sala_juego.iniciar_turno)
        self.senal_actuar_turno.connect(self.ventana_sala_juego.actuar_turno)
        self.ventana_sala_juego.senal_dejar_de_actuar_turno.connect(self.dejar_de_actuar)
        self.ventana_sala_juego.senal_terminar_turno.connect(self.terminar_turno)

        self.ventana_sala_juego.senal_preguntar_por_choza.connect(self.preguntar_por_choza)

        # senales fin partida
        self.senal_ir_a_fin_juego.connect(self.fin_del_juego)
        self.senal_fin_juego.connect(self.ventana_fin_partida.mostrar_puntajes)

        self.mostrar_sala_espera()

    def manejar_mensaje(self, mensaje):
        """mensaje: json object"""

        try:
            comando = mensaje['comando']
        except KeyError:
            return None

        if comando == 'intento_conexion':
            self.parametros_server = mensaje['parametros']
            self.crear_tablero(mensaje['grafos'])

        elif comando == 'login':
            self.login(mensaje['username'], mensaje['id'], mensaje['color'])

        elif comando == 'agregar_jugador':
            self.agregar_jugador(mensaje['lista_jugadores'])

        elif comando == 'eliminar_jugador':
            if mensaje['sala'] == 'sala_espera':
                self.eliminar_jugador_sala_espera(mensaje['id'])

        elif comando == 'iniciar_partida':
            self.iniciar_partida(mensaje['materias_primas'], mensaje['num_hexagonos'])

        elif comando == 'cambio_turno':
            if (mensaje['accion'] == 'choza_inicial' and
                    mensaje['turno_jugador'] == self.usuario.nombre):
                print('ARMAR CHOZA INICIAL')
                respuesta = self.usuario.ubicar_choza_inicial(
                    self.ventana_sala_juego.tablero, mensaje['ganancia']
                )
                self.senal_actualizar_labels_materias_primas.emit(
                    self.usuario, self.lista_jugadores)
                print(respuesta)
                self.cliente.enviar(respuesta)
            elif mensaje['accion'] == 'jugar':
                self.actualizar_label_turno(mensaje['turno_jugador'])
                self.actualizar_puntos_de_victoria(mensaje['puntos_de_victoria'])
                if mensaje['turno_jugador'] == self.usuario.nombre:
                    self.iniciar_turno()
                else:
                    self.esperar_turno()

        elif comando == 'choza':
            if mensaje['tipo'] == 'inicial' and mensaje['jugador'] != self.usuario.nombre:
                respuesta = self.ubicar_choza_inicial_espejo(
                    mensaje['jugador'], mensaje['nodo'], mensaje['ganancia'])
                self.cliente.enviar(respuesta)
            elif mensaje['tipo'] == 'regular' and mensaje['jugador'] != self.usuario.nombre:
                respuesta = self.ubicar_choza_regular_espejo(
                    mensaje['jugador'], mensaje['nodo'], mensaje['costo_choza'])
                self.cliente.enviar(respuesta)

        elif comando == 'lanzar_dados':
            self.lanzar_dados(mensaje['dados'][0], mensaje['dados'][1])

        elif comando == 'fin_juego':
            self.senal_ir_a_fin_juego.emit(mensaje['lista_puntos'])

        elif comando == 'mensaje_chat':
            self.senal_recibir_mensaje_chat.emit(mensaje['texto'])

    def crear_tablero(self, grafos):
        self.ventana_sala_juego.tablero.generar_listas_y_grafos(grafos)
        self.senal_generar_tablero.emit()
        self.cliente.enviar({
                'evento': 'Conexion exitosa',
                'detalles': 'Cliente instanciado'
            })

    def mostrar_sala_espera(self):
        # self.senal_mostrar_sala_espera.emit()
        self.ventana_sala_espera.show()

    def mostrar_chat(self):
        self.ventana_chat.show()

    def mostrar_sala_juego(self):
        self.ventana_sala_espera.hide()
        self.ventana_sala_juego.show()
        self.cliente.enviar({
            'evento': 'Inicio de partida',
            'detalles': f'{len(self.lista_jugadores)} jugadores'
            })

    def login(self, nombre, ide, color):
        self.usuario = Usuario(nombre, ide, color)

    def agregar_jugador(self, lista_jugadores):
        self.lista_jugadores = []
        for j in lista_jugadores:
            jug = Jugador(j['nombre'], j['id'], j['color'])
            print(jug.color)
            self.lista_jugadores.append(jug)
        for j in self.lista_jugadores:
            if j.nombre == self.usuario.nombre:
                self.lista_jugadores[self.lista_jugadores.index(j)] = self.usuario
        self.back_sala_espera.agregar_jugador(self.lista_jugadores)

    def eliminar_jugador_sala_espera(self, ide):
        self.senal_eliminar_jugador_sala_espera.emit(ide)

    def iniciar_partida(self, materias_primas, lista_num_hex):
        for i in range(len(self.ventana_sala_juego.tablero.lista_hexagonos)):
            self.ventana_sala_juego.tablero.lista_hexagonos[i].numero = lista_num_hex[i]
            self.ventana_sala_juego.tablero.lista_hexagonos[i].materia_prima = \
                materias_primas[str(i)]
        lista_hexagonos = self.ventana_sala_juego.tablero.lista_hexagonos
        self.ventana_sala_juego.tablero.set_materias_primas_nodos()
        self.senal_iniciar_partida.emit(self.usuario, self.lista_jugadores, lista_hexagonos)
        self.senal_mostrar_sala_juego.emit()

    def ubicar_choza_inicial_espejo(self, nombre_jugador, valor_nodo, ganancia):
        print('UBICAR CHOZA INICIAL')
        for jug in self.lista_jugadores:
            if nombre_jugador == jug.nombre:
                jugador = jug
        nodo = self.ventana_sala_juego.tablero.lista_nodos[valor_nodo]
        nodo.ubicar_choza(jugador.color)
        jugador.chozas.append(nodo)
        jugador.sumar_materias_primas(nodo, ganancia)
        self.lista_jugadores[self.lista_jugadores.index(jugador)] = jugador
        self.senal_actualizar_labels_materias_primas.emit(
                    self.usuario, self.lista_jugadores)
        print('FIN UBICAR CHIZA INICIAL')
        return {'evento': 'Choza inicial', 'detalles': 'Espejo'}

    def ubicar_choza_regular_espejo(self, nombre_jugador, valor_nodo, costo_choza):
        for jug in self.lista_jugadores:
            if nombre_jugador == jug.nombre:
                jugador = jug
        nodo = self.ventana_sala_juego.tablero.lista_nodos[valor_nodo]
        nodo.ubicar_choza(jugador.color)
        jugador.chozas.append(nodo)
        jugador.restar_materias_primas(nodo, costo_choza)
        self.lista_jugadores[self.lista_jugadores.index(jugador)] = jugador
        self.senal_actualizar_labels_materias_primas.emit(
                    self.usuario, self.lista_jugadores)
        return {'evento': 'Choza', 'detalles': 'Espejo'}

    def esperar_turno(self):
        self.ventana_sala_juego.boton_dados.setEnabled(False)
        self.ventana_sala_juego.drag_choza.setEnabled(False)
        self.ventana_sala_juego.boton_terminar_turno.setEnabled(False)

    def iniciar_turno(self):
        self.senal_iniciar_turno.emit()
        self.ventana_sala_juego.boton_dados.setEnabled(True)
        self.ventana_sala_juego.drag_choza.setEnabled(False)

    def lanzar_dados(self, dado_izq, dado_der):
        self.back_sala_juego.senal_dados_lanzados.emit(dado_izq, dado_der)
        self.sumar_materias_primas_dados(dado_izq, dado_der)

    def actuar(self, dado_izq, dado_der):
        self.cliente.enviar({'evento': 'Lanzar dados', 'detalles': [dado_izq, dado_der]})
        self.senal_actuar_turno.emit()

    def dejar_de_actuar(self, evento):
        if evento['evento'] == 'Choza':
            self.senal_actualizar_labels_materias_primas.emit(self.usuario, self.lista_jugadores)
            self.cliente.enviar(evento)

    def terminar_turno(self):
        print('TURNO TERMINADO')
        self.cliente.enviar({'evento': 'Cambio turno', 'detalles': 'Fin turno'})

    def preguntar_por_choza(self, valor_nodo):
        costo_choza = {
            'arcilla': self.parametros_server['CANTIDAD_ARCILLA_CHOZA'],
            'madera': self.parametros_server['CANTIDAD_MADERA_CHOZA'],
            'trigo': self.parametros_server['CANTIDAD_TRIGO_CHOZA']
        }
        if self.usuario.preguntar_por_choza(costo_choza):
            self.usuario.puntos_victoria += self.parametros_server['PUNTO_DE_VICTORIA']
            self.usuario.materias_primas['arcilla'] -= \
                self.parametros_server['CANTIDAD_ARCILLA_CHOZA']
            self.usuario.materias_primas['madera'] -= \
                self.parametros_server['CANTIDAD_MADERA_CHOZA']
            self.usuario.materias_primas['trigo'] -= self.parametros_server['CANTIDAD_TRIGO_CHOZA']
            for nodo in self.ventana_sala_juego.tablero.lista_nodos:
                if nodo.valor == valor_nodo:
                    nodo.ubicar_choza(self.usuario.color)
                    break
            self.dejar_de_actuar({
                'evento': 'Choza',
                'detalles': {
                    'jugador': self.usuario.nombre,
                    'nodo': nodo.valor,
                    'materias_primas_jugador': self.usuario.materias_primas
                    }
                })
        else:
            self.enviar_mensaje_error('No tienes suficientes materias primas para una choza')

    def enviar_mensaje_error(self, mensaje):
        self.senal_enviar_mensaje_error.emit(mensaje)

    def sumar_materias_primas_dados(self, dado_izq, dado_der):
        nodos_a_sumar = []
        for hexa in self.ventana_sala_juego.tablero.lista_hexagonos:
            if hexa.numero == (dado_izq + dado_der):
                for nodo in hexa.vertices:
                    if nodo not in nodos_a_sumar and nodo.choza_ocupada:
                        nodos_a_sumar.append(nodo)

        for nodo in nodos_a_sumar:
            for jug in self.lista_jugadores:
                if nodo in jug.chozas:
                    jug.sumar_materias_primas(
                        nodo, self.parametros_server['GANANCIA_MATERIA_PRIMA'])
        print('SUMANDO MATERIAS PRIMAS')
        self.senal_actualizar_labels_materias_primas.emit(self.usuario, self.lista_jugadores)

    def actualizar_puntos_de_victoria(self, lista_puntos):
        self.senal_actualizar_puntos_de_victoria.emit(
            lista_puntos, self.usuario, self.lista_jugadores)

    def actualizar_label_turno(self, turno_jugador):
        self.senal_actualizar_label_turno.emit(turno_jugador)

    def fin_del_juego(self, lista_puntos):
        if lista_puntos[0]['nombre'] == self.usuario.nombre:
            ha_ganado = True
        else:
            ha_ganado = False
        self.senal_fin_juego.emit(ha_ganado, lista_puntos)
        self.ventana_sala_juego.hide()
        self.ventana_fin_partida.show()
