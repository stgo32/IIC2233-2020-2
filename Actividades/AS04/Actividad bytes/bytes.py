import os

TOTAL = 32
MITAD = TOTAL/2

def reparar_imagen(ruta_entrada, ruta_salida):
    with open(ruta_entrada, 'rb') as archivo:
        bytes_contenido = bytearray(file.read())

    for i in range(0, len(bytes_contenido, TOTAL)):
        chunk = bytearray(bytes_contenido[i:i+TOTAL])
        mitad = chunk[:MITAD]
        pass

#--- NO MODIFICAR ---#
def reparar_imagenes(carpeta_entrada, carpeta_salida):
    for filename in os.listdir(os.path.join(os.getcwd(), carpeta_entrada)):
        reparar_imagen(
            os.path.join(os.getcwd(), carpeta_entrada, filename),
            os.path.join(os.getcwd(), carpeta_salida, filename)
        )


if __name__ == '__main__':
    try:
        reparar_imagenes('corruptas', 'caratulas')
        print("Imagenes reparadas (recuerda revisar que se carguen correctamente)")
    except Exception as error:
        print(f'Error: {error}')
        print("No has podido reparar las caratulas :'c")
