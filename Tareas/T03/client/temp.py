import socket
import threading
import json


# from parametros import p

# basado en cliente.py de AF05
class Cliente:

    def __init__(self, host, port):
        self.host = host
        self.port = port

        # Inicializar UI
        # self.controlador = Controlador(self)

        # Crear socket IPv4, TCP
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Conectarse con el servidor
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True

            # Escuchar los mensajes del servidor
            thread = threading.Thread(
                target=self.escuchar_servidor,
                daemon=True
            )
            thread.start()
            # self.controlador.mostrar_sala_espera()
        except ConnectionRefusedError:
            print(f"No se pudo conectar a {self.host}:{self.port}")
            self.socket_cliente.close()

        # self.enviar({'evento': 'Intento de conexion'})

        # self.enviar({
        #     'evento': 'Conexion exitosa',
        #     'detalles': 'Cliente instanciado'
        # })

    def escuchar_servidor(self):
        """Ciclo principal que escucha al servidor.

        Recibe mensajes desde el servidor, y genera una respuesta adecuada.
        """
        try:
            while True:
                mensaje = self.recibir()
                # if mensaje['comando'] == 'intento_conexion':
                    # print('aaaaaaaaaaaaaaa')
                    # self.controlador = Controlador(self, mensaje['grafos'], mensaje['cant_jugadores'])
                    # self.controlador.mostrar_sala_espera()
                    # print('bbbbbbbbbbbbb')
                # else:
                self.controlador.manejar_mensaje(mensaje)
        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            self.socket_cliente.close()

    def recibir(self):
        """Recibe un mensaje del servidor.

        Recibe el mensaje, lo decodifica usando el protocolo establecido,
        y lo des-serializa (via decodificar_mensaje).

        Retorna:
            dict: contiene el mensaje, después de ser decodificado.
        """
        print('>>> recibiendo')
        response_bytes_length = self.socket_cliente.recv(4)
        response_length = int.from_bytes(response_bytes_length, byteorder='big')
        response = bytearray()
        while len(response) < response_length:
            index = self.socket_cliente.recv(4)
            read_length = min(60, response_length - len(response))
            response.extend(self.socket_cliente.recv(read_length))

        mensaje = self.decodificar_mensaje(response)
        print('mensaje:', mensaje)
        return mensaje

    def enviar(self, mensaje):
        """Envía un mensaje a un cliente.

        Argumentos:
            mensaje (dict) de llaves:
                'evento': str
                'detalles': any (opcional)
                'log_activado': bool (opcional)
        """
        # bytes_mensaje = self.codificar_mensaje(mensaje)
        # largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
        # self.socket_cliente.sendall(largo_mensaje + bytes_mensaje)

        bytes_mensaje = self.codificar_mensaje(mensaje)        
        largo_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='big')
        TAMANO_CHUNK = 60

        message = largo_mensaje
        for i in range(0, len(bytes_mensaje), TAMANO_CHUNK):
            # Aqui obtenemos nuestro chunk
            index = bytearray(i.to_bytes(4, byteorder='big'))
            chunk = bytearray(index + bytes_mensaje[i:i+TAMANO_CHUNK])
            print(chunk)
            message += chunk
        print(f'\n{message}')

        self.socket_cliente.sendall(message)


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

    # parametros = cargar_parametros('parametros.json')
    # Se instancia el Cliente.
    cliente = Cliente(HOST, PORT)

    for i in 'kakakakakakakakakakakkaka':
        mensaje = {'evento': i}
        cliente.enviar(mensaje)

    # mensaje = {'evento': 'parametros', 'detalles': parametros}
    # cliente.enviar(mensaje)

