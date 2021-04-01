# basado en servidor.py de AF05

import json
import socket
import threading

from logica import Logica



class Servidor:

    lock_eliminar_jugador = threading.Lock()

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.log_activado = False

        print("Inicializando servidor...")
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()

        self.lista_jugadores = []

        self.logica = Logica(self)

    def bind_and_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")

    def accept_connections(self):
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()
        print("Servidor aceptando conexiones...")

    def accept_connections_thread(self):
        while True:
            socket_cliente, address = self.socket_server.accept()
            jugador = self.logica.instanciar_jugador(socket_cliente, address)
            listening_client_thread = threading.Thread(
                target=self.escuchar_cliente,
                args=(jugador, ),
                daemon=True)
            listening_client_thread.start()

    def escuchar_cliente(self, jugador):
        """Ciclo principal que escucha a un cliente.

        Recibe mensajes de un cliente, y genera una respuesta adecuada o levanta
        una acción según el mensaje recibido. Puede ser ejecutado en un thread,
        para permitir múltiples clientes paralelos.

        Argumentos:
            jugador (Jugador): El objeto jugador del cliente a escuchar.
        """
        if jugador not in self.lista_jugadores:
            self.lista_jugadores.append(jugador)

        try:
            while True:
                mensaje = self.recibir(jugador.socket_cliente)
                self.log(jugador.nombre, mensaje)

                lista_respuestas = self.logica.manejar_mensaje(
                    mensaje, jugador, self.lista_jugadores
                )
                self.enviar_lista_respuestas(jugador, lista_respuestas)

        except ConnectionResetError:
            self.log(jugador.nombre, {'evento': 'Error de conexion', 'detalles': 'reset'})
        self.log(jugador.nombre, {'evento': 'Cerrando conexion'})
        self.eliminar_cliente(jugador)

    def enviar(self, mensaje, socket_cliente):
        """Envía un mensaje a un cliente.

        Argumentos:
            mensaje (dict): Contiene la información a enviar. Debe ser serializable.
            socket_cliente (socket): El socket objetivo al cual enviar el mensaje.
        """
        if socket_cliente is not None:
            # bytes_mensaje = self.codificar_mensaje(mensaje)
            # largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
            # socket_cliente.sendall(largo_mensaje + bytes_mensaje)
            bytes_mensaje = self.codificar_mensaje(mensaje)        
            largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
            TAMANO_CHUNK = 20

            message = largo_mensaje
            for i in range(0, len(bytes_mensaje), TAMANO_CHUNK):
                # Aqui obtenemos nuestro chunk
                index = bytearray(i.to_bytes(4, byteorder='big'))
                chunk = bytearray(index + bytes_mensaje[i:i+TAMANO_CHUNK])
                # print(chunk)
                message += chunk
            # print(f'\n{message}')

            socket_cliente.sendall(message)

    def enviar_a_todos(self, mensaje):
        """Envía mensaje a todos los usuarios conectados.

        Argumentos:
            mensaje (dict): Contiene la información a enviar. Debe ser serializable.
        """
        for jugador in self.lista_jugadores:
            try:
                if jugador.socket_cliente is not None:
                    self.enviar(mensaje, jugador.socket_cliente)
            except ConnectionError:
                self.eliminar_cliente(jugador)

    def enviar_lista_respuestas(self, jugador, lista_respuestas):
        for respuesta in lista_respuestas:
            receptor = respuesta['receptor']
            mensaje = respuesta['mensaje']
            if receptor == 'individual':
                self.enviar(mensaje, jugador.socket_cliente)
            elif receptor == 'todos':
                self.enviar_a_todos(mensaje)

    def recibir(self, socket_cliente):
        """Recibe un mensaje del cliente.

        Recibe el mensaje, lo decodifica usando el protocolo establecido,
        y lo des-serializa (via decodificar_mensaje).

        Argumentos:
            socket_cliente (socket): El socket del cliente del cual recibir.

        Retorna:
            dict: contiene el mensaje, después de ser decodificado.
        """
        # response_bytes_length = socket_cliente.recv(4)
        # response_length = int.from_bytes(response_bytes_length, byteorder='big')
        # response = bytearray()
        # while len(response) < response_length:
        #     read_length = min(60, response_length - len(response))
        #     response.extend(socket_cliente.recv(read_length))

        # mensaje = self.decodificar_mensaje(response)
        # return mensaje

        # print('>>> recibiendo')
        response_bytes_length = socket_cliente.recv(4)
        response_length = int.from_bytes(response_bytes_length, byteorder='big')
        # print('response_length', response_length)
        response = bytearray()
        while len(response) < response_length:
            index = socket_cliente.recv(4)
            # print('index', index)
            read_length = min(60, response_length - len(response))
            response.extend(socket_cliente.recv(read_length))
            # print('response', response)

        mensaje = self.decodificar_mensaje(response)
        # print('mensaje:', mensaje)
        return mensaje

    def log(self, nombre_cliente, mensaje):
        """Imprime un mensaje con formato a la consola

        Argumentos:
            nombre_cliente: str
            mensaje: dict de llaves 'evento' (str), 'detalles'(str, opcional),
            'log_activado' (str, opcional)
        """
        evento = str(mensaje['evento'])

        try:
            detalles = str(mensaje['detalles'])
        except KeyError:
            detalles = '-'

        try:
            log_activado = bool(mensaje['log_activado'])
        except KeyError:
            log_activado = True

        if log_activado:
            if not self.log_activado:
                nombre_cliente_top = 'Cliente'
                evento_top = 'Evento'
                detalles_top = 'Detalles'
                top = f'\n{nombre_cliente_top:^30.30s}|{evento_top:^30.30s}|{detalles_top:^50.50s}'
                print(top)
                print('_'*112)
                self.log_activado = True

            mensaje = f'{nombre_cliente:^30.30s}|{evento:^30.30s}|    {detalles}'
            print(mensaje)

    def eliminar_cliente(self, jugador):
        """Elimina un jugador de lista_jugadores (lo transforma a bot).

        Argumentos:
            jugador (Jugador): el objeto jugador del cliente a sacar de la lista.
        """
        with self.lock_eliminar_jugador:
            jugador.socket_cliente.close()
            self.logica.id_jugador = jugador.id
            self.lista_jugadores.pop(self.lista_jugadores.index(jugador))
        self.enviar_a_todos(
            mensaje={
                'comando': 'eliminar_jugador',
                'sala': 'sala_espera',
                'id': jugador.id
            })
        self.log(jugador.nombre, {'evento': 'Eliminar cliente', 'detalles': 'Sala de Espera'})

    @staticmethod
    def codificar_mensaje(mensaje):
        """Codifica y serializa un mensaje usando JSON.

        Argumentos:
            mensaje (dict): Contiene llaves de strings, con información útil a enviar a cliente.
              Los valores del diccionario deben ser serializables.

        Retorna:
            bytes: El mensaje serializado
        """
        try:
            # Create JSON object
            json_mensaje = json.dumps(mensaje)
            # Encode JSON object
            bytes_mensaje = json_mensaje.encode('utf-8')

            return bytes_mensaje
        except json.JSONDecodeError:
            print("No se pudo codificar el mensaje")
            return b""

    @staticmethod
    def decodificar_mensaje(bytes_mensaje):
        """Decodifica y des-serializa bytes usando JSON.

        Argumentos:
            bytes_mensaje (bytes): Representa el mensaje serializado. Debe ser des-serializable
                y decodificable.

        Retorna:
            dict: El mensaje des-serializado, en su forma original.
        """
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()


if __name__ == "__main__":

    HOST = "localhost"
    PORT = 47365

    server = Servidor(HOST, PORT)

    try:
        while True:
            input("Presione Ctrl+C para cerrar el servidor...")
    except KeyboardInterrupt:
        print("Cerrando servidor...")
