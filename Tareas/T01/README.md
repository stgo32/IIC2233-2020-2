# Tarea 01: DCCumbre Olímpica :trophy:


### Cosas implementadas y no implementadas :white_check_mark: :x:

1. **Programación:**
    1. Diagrama: hecha completa
    2. Definición de clases, atributos y métodos: hecha completa
    3. Relaciones entre clases: hecha completa
2. **Partidas:**
    1. Crear partida: hecha completa
    2. Guardar: hecha completa
3. **Acciones:**
    1. Delegaciones: hecha completa
    2. Depotistas: los deportistas sí pueden lesionarse, pero se lesionan en validez_competencia por simplicidad. Lo demás hecho completo.
    3. Competencia: hecha completa
4. **Consola:**
    1. Menú inicio: hecha completa
    2. Menú principal: hecha completa
    3. Menú entrenador: hecha completa
    4. Menú entrenar: hecha completa (en clase Usuario)
    5. Opciones mínimas: hecha completa
    6. Robustez: hecha completa
5. **Manejo de archivos:**
    1. Archivos CSV: hecha completa
    2. parametros.py: hecha completa
    3. resultados.txt: hecha completa
      

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos, todos contenidos en ```T01```:
1. ```archivosExternos.py```
2. ```campeonato.py```
3. ```delegaciones.py```
4. ```deportes.py```
5. ```deportistas.py```
6. ```entrenadores.py```
7. ```menus.py```
8. ```parametros.py```
9. ```resultados.txt```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```abc```:  ```ABC, abstractmethod```  en  ```delegaciones.py,  deportes.py y entrenadores.py``` 
2. ```random```: ```uniform,  choice```  en  ```delegaciones.py y deportes.py```
3. ```sys```:  ```exit```  en  ```menus.py```   


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```archivosExternos```: hecha para manejar archivos csv y txt.
2. ```campeonato```: contiene la clase ```Campeonato```, y se utiliza para manejar todo lo relacionado con la competencia. 
3. ```delegaciones```: contiene las clases ```Delegacion, IEEEsparta y DCCrotona```, las últimas dos heredan de la primera. Controlan el accionar de cada delegacion.
4. ```deportes```: contiene las clases ```Deporte,  Atletismo,  Ciclismo,  Gimnasia  y  Natacion```. Las últimas cuatro heredan de la primera. Simulan los cuatro deportes de la competencia.
5. ```deportistas```: contiene la clase ```Deportista```. Utilizada para instanciar los deportistas participantes.
6. ```entrenadores```: contiene las clases ```Entrenador,  Usuario  y  Oponente```. Las últimas dos heredan de la primera. Utilizadas para que cada delegación tenga un entrenador que pueda tomar decisiones.
7. ```menus```: Contiene la clase ```Menu```. Utilizada para el funcionamiento general del programa y los diferentes menús.
8. ```parametros```: Contiene los parámetros del programa.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Primero se elige delegación propia y después el nombre del oponente. 
2. Al momento de elegir a un deportista para que compita imprime a todo el equipo aunque hallan deportistas lesionados, si están lesionados pregunta si aún así desea continuar.
3. DCCrotona al realizar la habilidad especial recibe la medalla en **atletismo** por defecto y se elige a cualquier deportista del equipo para que le aumente la moral.
4. En mostrar estado se redondean algunos floats por estética, a nivel de código éstos **no** cambian.
5. Para que el deportista se lesione la probabilidad debe ser **menor** al riesgo.
