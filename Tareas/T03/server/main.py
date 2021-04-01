from server import Servidor

from parametros import p

if __name__ == "__main__":

    server = Servidor(p.HOST, p.PORT)

    try:
        while True:
            input("Presione Ctrl+C para cerrar el servidor...")
    except KeyboardInterrupt:
        print("Cerrando servidor...")
