from collections import namedtuple, defaultdict
import os



def cargar_datos(path):
    with open(path, 'rt') as archivo:
        datos = archivo.readlines() 
    
    lista_ayudantes = []
    for ayudante in datos:
        ayudante = ayudante.split(",")
        ayudante[2] = ayudante[2][:-1]
        lista_ayudantes.append(ayudante)
    lista_ayudantes.pop(0)

    return lista_ayudantes
        
def crear_ayudantes(datos):
    Ayudante = namedtuple("Ayudante_type", ["Nombre", "Cargo", "Usuario"])

    data = []
    for ayudante in datos:
        ayudante = Ayudante(ayudante[0], ayudante[1], ayudante[2])
        data.append(ayudante)

    return data

def encontrar_cargos(ayudantes):
    cargos = set()
    for ayudante in ayudantes:
        cargos.add(ayudante.Cargo)
    return cargos

def ayudantes_por_cargo(ayudantes):
    ayudantes_por_cargo = dict()
    for ayudante in ayudantes:
        ayudantes_por_cargo[ayudante.Cargo] = []

    for ayudante in ayudantes:
        ayudantes_por_cargo[ayudante.Cargo].append(ayudante)

    return ayudantes_por_cargo


if __name__ == '__main__':
    datos = cargar_datos('stgo32-iic2233-2020-2/Actividades/AC00/ayudantes.csv')
    if datos is not None:
        print('Se lograron leer los datos')
    else:
        print('Debes completar la carga de datos')

    ayudantes = crear_ayudantes(datos)
    if ayudantes is not None:
        print('\nLos ayudantes son:')
        for ayudante in ayudantes:
            print(ayudante)
    else:
        print('\nDebes completar la creación de Ayudantes')

    cargos = encontrar_cargos(ayudantes)
    if cargos is not None:
        print('\nLos cargos son:')
        for cargo in cargos:
            print(cargo)
    else:
        print('\nDebes completar la búsqueda de Cargos')

    clasificados = ayudantes_por_cargo(ayudantes)
    if clasificados is not None:
        print('\nLos ayudantes por cargos son:')
        for cargo in clasificados:
            print(f'\n{cargo}')
            for ayudante in clasificados[cargo]:
                print(ayudante)
    else:
        print('\nDebes completar la clasificación de Ayudantes')


