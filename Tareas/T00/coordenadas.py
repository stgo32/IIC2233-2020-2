abcdario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# convertir de coordenada numérica a coordenada de tablero
def de_nm_a_coordenada(fila, columna):
    letra = abcdario[columna]
    coordenada = letra + str(fila)
    return coordenada


# convertir de coordenada de tablero a coodenada numérica
def de_coordenada_a_nm(coordenada):
    coordenada = str(coordenada[0]) + " " + str(coordenada[1])
    coordenada = coordenada.split(" ")
    fila = int(coordenada[1])
    col = abcdario.index(coordenada[0])
    coord = [fila, col]
    return coord
