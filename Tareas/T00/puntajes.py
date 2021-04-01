from parametros import NUM_BARCOS


# cargar archivo
def cargar_puntajes(puntajes):
    with open(puntajes, 'rt') as archivo:
        datos = archivo.readlines()
    lista_puntajes = []
    for puntaje in datos:
        puntaje = puntaje.split(",")
        if "\n" in puntaje[1]:
            puntaje[1] = puntaje[1][:-1]
        puntaje[1] = int(puntaje[1])
        lista_puntajes.append(puntaje)
    archivo.close()
    return lista_puntajes


# ver ranking de puntajes
def ver_ranking_puntajes(puntajes):
    lista_puntajes = cargar_puntajes(puntajes)
    registros_lista_puntajes = []
    for puntaje in lista_puntajes:
        registros_lista_puntajes.append(puntaje[1])
    registros_lista_puntajes.sort(reverse=True)
    sort_lista_puntajes = []
    for registro in registros_lista_puntajes:
        for puntaje in lista_puntajes:
            if registro == puntaje[1]:
                sort_lista_puntajes.append(puntaje)
                lista_puntajes.pop(lista_puntajes.index(puntaje))
    if len(sort_lista_puntajes) != 0:
        print("Los mejores puntajes son:")
    else:
        print("No hay puntajes registrados")
    if len(sort_lista_puntajes) < 5:
        for i in range(len(sort_lista_puntajes)):
            print(f'   {i+1}. {sort_lista_puntajes[i][0]}: {sort_lista_puntajes[i][1]}')
    else:
        for i in range(5):
            print(f'   {i+1}. {sort_lista_puntajes[i][0]}: {sort_lista_puntajes[i][1]}')
    return


# calculo de puntaje
def calcular_puntaje(jugador, oponente):
    filas = len(jugador.tablero)
    columnas = len(jugador.tablero[0])
    enemigos_desc = oponente.contar_fuegos()
    aliados_desc = jugador.contar_fuegos()
    nombre = jugador.apodo
    puntos = max(0, (filas * columnas * NUM_BARCOS * (enemigos_desc - aliados_desc)))
    print(f"{jugador.apodo} tu puntaje fue: {puntos}")
    puntaje = [nombre, puntos]
    return puntaje


# agregar puntaje a puntajes.txt
def agregar_puntaje(puntaje, archivo):
    puntajes = open(archivo, "a")
    puntajes.write(f"\n{puntaje[0]},{puntaje[1]}")
    puntajes.close()
    pass
