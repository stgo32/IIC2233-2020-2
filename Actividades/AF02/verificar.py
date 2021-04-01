from estudiante import cargar_datos, cargar_datos_corto


def verificar_numero_alumno(alumno):  # Levanta la excepción correspondiente
    alumno.n_alumno = str(alumno.n_alumno)
    primero_segundo = alumno.n_alumno[:2]
    tercero_cuarto = alumno.n_alumno[:4]
    ultimo_digito = alumno.n_alumno[7]

    if primero_segundo != str(alumno.generacion)[2:]:
        raise ValueError("El numero de alumno es incorrecto")
    if tercero_cuarto != "61" or tercero_cuarto != "63":
        if alumno.carrera == "Ingeniería":
            if tercero_cuarto != "63":
                raise ValueError("El numero de alumno es incorrecto")
        if alumno.carrera == "College":
            if tercero_cuarto != "61":
                raise ValueError("El numero de alumno es incorrecto")
    if ultimo_digito.isdigit() is False:
        if ultimo_digito != "J":
            raise ValueError("El numero de alumno es incorrecto")


def corregir_alumno(estudiante):  # Captura la excepción anterior
    primero_segundo = alumno.n_alumno[:2]
    tercero_cuarto = alumno.n_alumno[:4]
    ultimo_digito = alumno.n_alumno[7]
    
    estudiante.n_alumno = list(estudiante.n_alumno)
    try:
        verificar_numero_alumno(estudiante)
    except ValueError as err:
        print(estudiante.n_alumno)
        if primero_segundo != str(estudiante.generacion)[2:]:
            estudiante.n_alumno[2] = list(str(estudiante.generacion))[3]
            estudiante.n_alumno[5] = list(str(estudiante.generacion))[4]
        if tercero_cuarto != "61" or tercero_cuarto != "63":
            estudiante.n_alumno[7] = "6"
            if estudiante.carrera == "Ingeniería":
                estudiante.n_alumno[9] = "3"
            if estudiante.carrera == "College":
                estudiante.n_alumno[11] = "1"
        if ultimo_digito.isdigit() is False:
            if ultimo_digito != "J":
                estudiante.n_alumno[] = "J" 
    finally:
        estudiante.n_alumno = "".join(estudiante.n_alumno)
        print(f"{estudiante.nombre} está correctamente inscrite en el curso, todo en orden...\n")

# ************


def verificar_inscripcion_alumno(n_alumno, base_de_datos):  # Levanta la excepción correspondiente
    pass


def inscripcion_valida(estudiante, base_de_datos):  # Captura la excepción anterior
    pass


# ************

def verificar_nota(nota):  # Levanta la excepción correspondiente
    pass


def corregir_nota(estudiante):  # Captura la excepción anterior
    pass


if __name__ == "__main__":
    datos = cargar_datos_corto("alumnos.txt")  # Se cargan los datos
    for alumno in datos.values():
        if alumno.carrera != "Profesor":
            corregir_alumno(alumno)
            inscripcion_valida(alumno, datos)
            corregir_nota(alumno)
