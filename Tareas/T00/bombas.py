from coordenadas import de_nm_a_coordenada


# bomba regular
def regular(fila, celda, tablero_contrincante):
    acierto = False
    fuego = False
    descubierta = False
    if (tablero_contrincante[fila][celda] == " ") or (tablero_contrincante[fila][celda] == "B"):
        coordenada = de_nm_a_coordenada(fila, celda)
        if tablero_contrincante[fila][celda] == " ":
            tablero_contrincante[fila][celda] = "X"
            acierto = True
            print(f"Se ha lanzado una bomba en la coordenada {coordenada}: Agua...")
        else:
            tablero_contrincante[fila][celda] = "F"
            fuego = True
            print(f"Se ha lanzado una bomba en la coordenada {coordenada}: Fuego!!")
    else:
        descubierta = True
        print("La celda ya ha sido descubierta")
    return acierto, tablero_contrincante, fuego, descubierta


# BOMBAS ESPECIALES:
def cruz(fila, celda, tablero_contrincante, radio):
    acierto = False
    fuego = False
    descubierta = False
    filas = len(tablero_contrincante) - 1
    columnas = len(tablero_contrincante[0]) - 1
    for i in range(radio):
        # Cada if agrega una linea desde el centro de la explosión
        if (celda + i) <= columnas:
            if (tablero_contrincante[fila][celda + i] == " ") or \
                    (tablero_contrincante[fila][celda + i] == "B"):
                if tablero_contrincante[fila][celda + i] == " ":
                    tablero_contrincante[fila][celda + i] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila][celda + i] = "F"
                    fuego = True
            else:
                descubierta = True

        if (fila + i) <= filas:
            if (tablero_contrincante[fila + i][celda] == " ") or \
                    (tablero_contrincante[fila + i][celda] == "B"):
                if tablero_contrincante[fila + i][celda] == " ":
                    tablero_contrincante[fila + i][celda] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila + i][celda] = "F"
                    fuego = True
            else:
                descubierta = True

        if (celda - i) >= 0:
            if (tablero_contrincante[fila][celda - i] == " ") or \
                    (tablero_contrincante[fila][celda - i] == "B"):
                if tablero_contrincante[fila][celda - i] == " ":
                    tablero_contrincante[fila][celda - i] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila][celda - i] = "F"
                    fuego = True
            else:
                descubierta = True

        if (fila - i) >= 0:
            if (tablero_contrincante[fila - i][celda] == " ") or \
                    (tablero_contrincante[fila - i][celda] == "B"):
                if tablero_contrincante[fila - i][celda] == " ":
                    tablero_contrincante[fila - i][celda] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila - i][celda] = "F"
                    fuego = True
            else:
                descubierta = True
    return acierto, tablero_contrincante, fuego, descubierta


def equis(fila, celda, tablero_contrincante, radio):
    filas = len(tablero_contrincante) - 1
    columnas = len(tablero_contrincante[0]) - 1
    for i in range(radio):
        # Cada if crea diagonales a medida que vanza el for
        if (fila + i) <= filas and (celda + i) <= columnas:

            if (tablero_contrincante[fila + i][celda + i] == " ") or \
                    (tablero_contrincante[fila + i][celda + i] == "B"):
                if tablero_contrincante[fila + i][celda + i] == " ":
                    tablero_contrincante[fila + i][celda + i] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila + i][celda + i] = "F"
                    fuego = True
            else:
                descubierta = True

        if (fila + i) <= filas and (celda - i) >= 0:

            if (tablero_contrincante[fila + i][celda - i] == " ") or \
                    (tablero_contrincante[fila + i][celda - i] == "B"):
                if tablero_contrincante[fila + i][celda - i] == " ":
                    tablero_contrincante[fila + i][celda - i] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila + i][celda - i] = "F"
                    fuego = True
            else:
                descubierta = True

        if (fila - i) >= 0 and (celda - i) >= 0:
            if (tablero_contrincante[fila - i][celda - i] == " ") or \
                    (tablero_contrincante[fila - i][celda - i] == "B"):
                if tablero_contrincante[fila - i][celda - i] == " ":
                    tablero_contrincante[fila - i][celda - i] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila - i][celda - i] = "F"
                    fuego = True
            else:
                descubierta = True

        if (fila - i) >= 0 and (celda + i) <= columnas:
            if (tablero_contrincante[fila - i][celda + i] == " ") or \
                    (tablero_contrincante[fila - i][celda + i] == "B"):
                if tablero_contrincante[fila - i][celda + i] == " ":
                    tablero_contrincante[fila - i][celda + i] = "X"
                    acierto = True
                else:
                    tablero_contrincante[fila - i][celda + i] = "F"
                    fuego = True
            else:
                descubierta = True
    return acierto, tablero_contrincante, fuego, descubierta


def diamante(fila, celda, tablero_contrincante, radio):
    filas = len(tablero_contrincante) - 1
    columnas = len(tablero_contrincante[0]) - 1
    # Cada for crea un triangulo rectandulo, donde el angulo recto se
    # ubica en el centro de explosion. Basicamente es un triangulo
    # que se rota 4 veces.
    for i in range(radio-1, -1, -1):
        for j in range(radio):
            a = (fila - i + j)
            if a > fila:
                a = fila
            if (a >= 0) and (celda + j) <= columnas:
                if (tablero_contrincante[a][celda + j] == " ") or \
                        (tablero_contrincante[a][celda + j] == "B"):
                    if tablero_contrincante[a][celda + j] == " ":
                        tablero_contrincante[a][celda + j] = "X"
                        acierto = True
                    else:
                        tablero_contrincante[a][celda + j] = "F"
                        fuego = True
                else:
                    descubierta = True

    for i in range(radio-1, -1, -1):
        for j in range(radio):
            a = (fila - i + j)
            if a > fila:
                a = fila
            if (a >= 0) and (celda - j) >= 0:
                if (tablero_contrincante[a][celda - j] == " ") or \
                        (tablero_contrincante[a][celda - j] == "B"):
                    if tablero_contrincante[a][celda - j] == " ":
                        tablero_contrincante[a][celda - j] = "X"
                        acierto = True
                    else:
                        tablero_contrincante[a][celda - j] = "F"
                        fuego = True
                else:
                    descubierta = True

    for i in range(radio):
        for j in range(radio):
            a = (fila + i - j)
            if a < fila:
                a = fila
            if (a <= filas) and (celda - j) >= 0:
                if (tablero_contrincante[a][celda - j] == " ") or \
                        (tablero_contrincante[a][celda - j] == "B"):
                    if tablero_contrincante[a][celda - j] == " ":
                        tablero_contrincante[a][celda - j] = "X"
                        acierto = True
                    else:
                        tablero_contrincante[a][celda - j] = "F"
                        fuego = True
                else:
                    descubierta = True
    for i in range(radio):
        for j in range(radio):
            a = (fila + i - j)
            if a < fila:
                a = fila
            if (a <= filas) and (celda + j) <= columnas:
                if (tablero_contrincante[a][celda + j] == " ") or \
                        (tablero_contrincante[a][celda + j] == "B"):
                    if tablero_contrincante[a][celda + j] == " ":
                        tablero_contrincante[a][celda + j] = "X"
                        acierto = True
                    else:
                        tablero_contrincante[a][celda + j] = "F"
                        fuego = True
                else:
                    descubierta = True
    return acierto, tablero_contrincante, fuego, descubierta
