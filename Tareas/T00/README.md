# Tarea T00: DCCombateNaval :ship:


## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

1. **Inicio del Programa:**
    1. Menú de inicio: hecha completa.
    2. Funcionalidades: hecha completa.
    3. Puntajes: hecha completa.
2. **Flujo del Juego**: 
    1.  Menú de juego: hecha completa. 
    2.  Tablero: hecha completa.
    3.  Turnos: hecha completa.
    4.  Bombas: en casos **muy puntuales** algunas bombas especiales a veces tiran un error de que algunas variables se usan antes de ser referenciadas, pero en general funcionan perfecto.
    5.  Barcos: hecha completa.
    6.  Oponente: hecha completa
3. **Término del Juego:**
    1.  Fin del juego: hecha completa.
    2.  Puntajes: hecha completa.
4. **Archivos:**
    1.  Manejo de archivos: hecha completa.
5. **General:**
    1.  Menús: hecha completa.
    2.  Parámetros hecha completa.
    3.  Módulos: hecha completa.
    4.  PEP8: hecha completa.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se deben utilizar los siguientes archivos, todos ubicados en la carpeta ```T00```:
1. ```bombas.py```
2. ```coordenadas.py```
3. ```jugador.py```
4. ```parametros.py```
5. ```partida.py```
6. ```puntajes.py```
7. ```puntajes.txt```
8. ```tablero.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()``` en  el módulo ```jugador.py```.
2. ```sys```: ```exit()``` en los módulos ```main.py``` y ```partida.py```.


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```bombas```: Contiene 4 funciones, correspondientes a los cuatro tipos de bombas del juego.
2. ```coordenadas```: Contiene 2 funciones, ambas para cambiar el formato de la coordenada.
3. ```jugador```: Contiene 3 clases: ```Jugador```, ```Usuario``` y ```Oponente```, la primera es super clase de las otras dos.
4. ```partida```: Contiene 3 funciones enfocadas en el funcionamiento de cada partida.
5. ```puntajes```: Contiene 4 funciones que operan en los puntajes del juego.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Cada vez que hunde un barco muestra de nuevo el tablero y pide **de inmediato** la siguiente bomba sin pasar por el Menú de Juego, ya que el jugador accedió a disparar, por lo que está dispuesto a disparar de nuevo si acierta el disparo. 
2. Supuse que las bombas especiales **si** pueden ser lanzadas en una coordenada ya descubierta siempre y cuando descubran al menos una nueva.
3. El parámetro ```abcdario``` inicialmente se encontraba en ```parametros.py```, al darme cuenta que este archivo no podía ser modificado lo ubiqué en ```coordenadas.py``` porque ahí es donde es usado más veces.
4. En ```puntajes.txt``` aún están los puntajes de las partidas que jugué.


PD: A errar un disparo le llamé **agua**. A hundir un barco le llamé **fuego**.
