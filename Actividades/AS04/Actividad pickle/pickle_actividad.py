import pickle


def desencriptar(password):
    nueva = ""
    for letra in password:
        nueva += str(chr(ord(letra)-4))
    return nueva


def encriptar(password):
    nueva = ""
    for letra in password:
        nueva += str(chr(ord(letra)+3))
    return nueva


def cargar_instancia(ruta):
    with open(ruta, 'rb') as archivo:
        usuarios = pickle.load(archivo)
    return usuarios


class Usuario:
    def __init__(self, nombre, peliculas, indices, password):
        # agregarle los atributos
        self.nombre = nombre
        self.peliculas = peliculas
        self.password = password
        self.indices = indices
        self.clave_encriptada = False

    def __repr__(self):
        return f"| Nombre: {self.nombre:13s} | Password: {self.password:13s}  | Peliculas Favoritas: {self.peliculas} |"

    def __getstate__(self):
        nuevo = self.__dict__.copy()
        clave_encriptada = encriptar(nuevo['password'])
        nuevo.update({'password': f'{clave_encriptada}', 'clave_encriptada': f'{True}'})
        # nuevo.update({'clave_encriptada': f'{True}'})
        print('SERIALIZANDO')
        self.__dict__ = nuevo
        if self.nombre == 'cruz':
            print(clave_encriptada)
            print(self.__dict__)
        return self.__dict__

    def __setstate__(self, state):
        if state['clave_encriptada'] == 'True':
            print('DESERIALIZANDO')
            clave_desencriptada = desencriptar(state['password'])
            state.update({'password': f'{clave_desencriptada}', 'clave_encriptada': f'{False}'})
            # state.update({'clave_encriptada': f'{False}'})
            print(state['nombre'])
            print(state['password'])
        self.__dict__ = state
        return self.__dict__


def guardar_instancia(ruta, data):
    with open("archivo_encriptado.bin", "wb") as file:
        pickle.dump(data, file)

if __name__ == "__main__":

    data = cargar_instancia("info_personas.bin")
    
    se_desencripto = False
    desencripto_falso = False
    for usuario in data:
        if usuario.nombre == "cruz" and usuario.password == "nosoyunrobot":
            se_desencripto = True

        if usuario.nombre == "tocococa" and usuario.password != "luchojara":
            desencripto_falso = True
    
    for usuario in data:
        print(usuario)
        print()

    if not se_desencripto:
        print("No desencriptaste los usuarios que se tenian que desencriptar")

    if desencripto_falso:
        print("Desencriptaste un usuario que no tenia la contraseña encriptada")
    
    guardar_instancia("archivo_encriptado.bin", data)

    data_post_encripcion = cargar_instancia("archivo_encriptado.bin")

    serealizado = False
    for usuario in data_post_encripcion:
        if usuario.nombre == "cruz" and usuario.password == "mnrnxtmqnans":
            serealizado = True

    if not serealizado:
        print("No encriptaste de forma correcta la clave")

