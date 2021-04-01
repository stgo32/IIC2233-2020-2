from deportistas import Deportista


def cargar_delegaciones(csv):
    with open(csv, "rt") as archivo:
        data = archivo.readlines()
    lista_final = []
    lista_datos = []
    for fila in data:
        fila = fila.split(",")
        if "\n" in fila[4]:
            fila[4] = fila[4][:-1]
        lista_datos.append(fila)
    fila1 = lista_datos.pop(0)
    for fila in lista_datos:
        dict_datos = {}
        for i in range(len(fila)):
            dict_datos[fila1[i]] = fila[i]
        lista_final.append(dict_datos)
    for dict_ in lista_final:
        dict_["Moral"] = float(dict_["Moral"])
        dict_["Medallas"] = int(dict_["Medallas"])
        dict_["Dinero"] = int(dict_["Dinero"])
        dict_["Equipo"] = dict_["Equipo"].split(";")
    archivo.close()
    return(lista_final)


def cargar_deportistas(csv):
    with open("deportistas.csv", "rt") as archivo:
        data = archivo.readlines()
    lista_final = []
    lista_datos = []
    for fila in data:
        fila = fila.split(",")
        if "\n" in fila[6]:
            fila[6] = fila[6][:-1]
        lista_datos.append(fila)
    fila1 = lista_datos.pop(0)
    for fila in lista_datos:
        dict_datos = {}
        for i in range(len(fila)):
            dict_datos[fila1[i]] = fila[i]
        lista_final.append(dict_datos)
    for dict_ in lista_final:
        dict_["flexibilidad"] = int(dict_["flexibilidad"])
        dict_["moral"] = int(dict_["moral"])
        dict_["precio"] = int(dict_["precio"])
        dict_["velocidad"] = int(dict_["velocidad"])
        dict_["resistencia"] = int(dict_["resistencia"])
    lista_deportistas = []
    for dict_ in lista_final:
        deportista = Deportista(dict_["nombre"], dict_["velocidad"], dict_["resistencia"],
                                dict_["flexibilidad"], dict_["moral"], dict_["lesionado"],
                                dict_["precio"])
        lista_deportistas.append(deportista)
    archivo.close()
    return lista_deportistas


def actualizar_resultados(ganador, deleg_ganadora, deporte, txt):
    puntajes = open(txt, "a")
    puntajes.write(f"\nCompetencia: {deporte}\n"
                   f"Delegacion Ganadora: {deleg_ganadora.nombre}\n"
                   f"Deportista Ganador: {ganador.nombre}\n")
    puntajes.close()


if __name__ == "__main__":
    dep = cargar_deportistas("deportistas.csv")
    for d in dep:
        print(d.lesionado)
