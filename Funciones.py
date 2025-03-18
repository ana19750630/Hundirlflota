import pprint
from colorama import init, Fore, Back ##colorama es una biblioteca de Python que permite dar color
                                        ## a los textos en la terminal

# Inicializar colorama para asegurarnos de que funcione en todas las plataformas
init(autoreset=True)

# Creación de un tablero 10x10 con espacios vacíos representados por el carácter " "
tablero = [[" " for _ in range(10)] for _ in range(10)]

# Insertar el barco de 4 casillas en horizontal en las posiciones [1][0], [1][1], [1][2], [1][3]
tablero[1][0] = "B"
tablero[1][1] = "B"
tablero[1][2] = "B"
tablero[1][3] = "B"

# Insertar el barco de 3 casillas en vertical en las posiciones [3][3], [4][3], [4][4], [4][5]
tablero[4][3] = "B"
tablero[4][4] = "B"
tablero[4][5] = "B"

##Definimos un diccionario de barco1
barco1 = {"coord":[(1, 0), (1, 1), (1, 2), (1, 3)], ## diccionario
          "vidas": 4} 

##Definimos un diccionario de barco2
barco2 = {"coord":[(4, 3), (4, 4), (4, 5)], ## diccionario barco2
          "vidas": 3}

# Crear un tablero de disparos que el jugador verá
tablero_disparos = [[" " for _ in range(10)] for _ in range(10)]

# Función para imprimir el tablero de disparos (lo que el jugador ve)
def mostrar_tablero():
    for fila in tablero_disparos:
        print(Back.BLACK + Fore.WHITE + " ".join(fila))



##funcion para disparar en el tablero.
def disparo(tablero, tablero_disparos ,i,j):
    if 0 <= i <= 10: 
        if tablero[i][j] =='B':
            print("Tocado")
            print("Sigue jugando")
            tablero[i][j]= "x"
            tablero_disparos[i][j] = "X"  # Actualizamos el tablero de disparos
            ##print(tablero)
            return True
            
        elif tablero[i][j] == " ":
            print("agua")
            tablero[i][j] = "0"
            tablero_disparos[i][j] = "0"  # Marcamos la casilla como agua
            ##print(tablero)
            return False
        else:
            print("ya has disparado antes")
            return False
    else:
        print( "fuera del rango, numeros ente 0 y 9")   
        
##Bucle de juego
while True:
    mostrar_tablero()

    i = int(input("introduce la fila"))
    j = int(input("introduce la columna"))
    acertado = disparo(tablero, tablero_disparos,i,j)
    ##pprint.pprint(mostrar_tablero)

    if acertado== True:
        coordenadas_barco= barco1["coord"]
        if (i,j) in coordenadas_barco:
            barco1["vidas"] = barco1 ["vidas"]-1
            if barco1["vidas"] == 0: 
                print("Hundido")
        coordenadas_barco2= barco2["coord"]
        if (i,j) in coordenadas_barco2:
            barco2["vidas"] = barco2 ["vidas"]-1
            if barco2["vidas"] == 0:
                print("Hundido")
    if barco1["vidas"]==0 and barco2["vidas"]==0:
        print("Has acabado la partida")
        break
    