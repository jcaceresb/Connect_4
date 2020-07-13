import controles   #Importa las funciones de "controles.py"
import base_bot    #Importa las funciones de "base_bot.py"

def mostrar(x,y):
  for i in range(0,len(x)): #Imprime el tablero igual a tablero de connect 4
    print(x[i])
  print(y)

def jugar(jug,val): #Para cada turno de jugador
  preg = jug + ", introduzca un número (1-7): " #Define la pregunta usando el nombre
  while True: #Ciclo infinito para obligar al jugador a tener una jugada válida
    num = int(input(preg)) #Pregunta el lugar de la casilla
    if tablero[0][num-1] == " ": #Si el tablero presenta la casilla superior vacía (espacio para la ficha), acepta y rompe el while
      break
  for i in range(0,len(tablero)): #Recorre el tablero
    if tablero[i][num-1] != " ": # Cae hasta que encuentra una ficha y se pone un sitio anterior
      tablero[i-1][num-1] = val
      break
    elif i == 5:
      tablero[i][num-1] = val #Cae hasta el final del tablero si la columna está vacía

print("BENVENIDOS A CONNECT 4") #Introduccion del juego
print()
print("Hecho por: Jose Caceres, Augusto Bracamonte y Vasco Bustamante")
print()
print("MODOS DE JUEGO:")
print()
print("JUGADOR VS IA: 1")
print("JUGADOR VS JUGADOR: 2")
print()
while True:
  modo = int(input("¿Qué modo jugarás? (1-2): "))
  if modo == 1 or modo == 2:
    break
print()

tablero = [[" "," "," "," "," "," "," "], #Define el tablero
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "]]

numeros = ["1","2","3","4","5","6","7"]

if modo == 2:
  print("Has seleccionado JUGADOR VS JUGADOR")
  print()
  jugador1 = input("Jugador 1, introduce tu nombre: ") #Introducción del nombre de los jugadores
  print()
  jugador2 = input("Jugador 2, introduce tu nombre: ")
  print()

  mostrar(tablero,numeros) #Muestra el tablero inicial
  print()

  cont = 0   #Variable que contará el número de turnos hasta el final del juego

  while True: #Turnos infinitos hasta que alguien gane
  
    jugar(jugador1,"o") #Turno del jugador 1 con ficha "1"

    print()

    mostrar(tablero,numeros) #Muestra el tablero luego de la jugada

    comprobacion = controles.comprobar(tablero,"o") #Comprueba con las fichas del jugador 1
    if comprobacion == True: 
      ganador = jugador1 #Si gana, declara al jugador 1 como ganador y se rompe el while
      break

    tab_lleno = controles.tablero_lleno(tablero) #Comprueba si el tablero esta lleno
    if tab_lleno == True:
      ganador = "Empate" #Si el tablero esta lleno declara al ganadorcomo empate y rompe el while
      break

    print()

    jugar(jugador2,"+") #Turno del jugador 2 con ficha "2"

    print()

    mostrar(tablero,numeros) #Muestra el tablero luego de la jugada

    comprobacion = controles.comprobar(tablero,"+") #Comprueba con las fichas del jugador 2
    if comprobacion == True: 
      ganador = jugador2 #Si gana, declara al jugador 2 como ganador y se rompe el while
      break

    tab_lleno = controles.tablero_lleno(tablero) #Comprueba si el tablero esta lleno
    if tab_lleno == True:
      ganador = "Empate" #Si el tablero esta lleno declara al ganador como empate y rompe el while
      break

    print()

else:
  print("Has seleccionado JUGADOR VS IA")
  print()
  print("DIFICULTAD:")
  print()
  print("MEDIA: 1")
  print("LEYENDA: 2")
  print()
  while True:
    dificultad = int(input("¿Qué modo jugarás? (1-2): "))
    if dificultad == 1 or dificultad == 2:
        break
  print()

  if dificultad == 2:
    print("Has seleccionado DIFICULTAD LEYENDA")
    print()
    jugador1 = input("Jugador 1, introduce tu nombre: ") #Introducción del nombre de los jugadores
    print()

    mostrar(tablero,numeros) #Muestra el tablero inicial
    print()

    while True: #Turnos infinitos hasta que alguien gane
  
      jugar(jugador1,"o") #Turno del jugador 1 con ficha "o"
      
      print()

      mostrar(tablero,numeros) #Muestra el tablero luego de la jugada

      comprobacion = controles.comprobar(tablero,"o") #Comprueba con las fichas del jugador 1
      if comprobacion == True: 
        ganador = jugador1 #Si gana, declara al jugador 1 como ganador y se rompe el while
        break

      tab_lleno = controles.tablero_lleno(tablero) #Comprueba si el tablero esta lleno
      if tab_lleno == True:
        ganador = "Empate" #Si el tablero esta lleno declara al ganador como empate y rompe el while
        break

      print()

      base_bot.jugar_bot_leyenda(tablero,"+","o") #Turno de la IA con ficha "+"

      print()

      mostrar(tablero,numeros) #Muestra el tablero luego de la jugada

      comprobacion = controles.comprobar(tablero,"+") #Comprueba con las fichas del jugador 2
      if comprobacion == True: 
        ganador = "IA" #Si gana, declara a la IA como ganadora y se rompe el while
        break

      tab_lleno = controles.tablero_lleno(tablero) #Comprueba si el tablero esta lleno
      if tab_lleno == True:
        ganador = "Empate" #Si el tablero esta lleno declara al ganador como empate y rompe el while
        break

      print()

  else:
    print("Has seleccionado DIFICULTAD MEDIA")
    print()
    jugador1 = input("Jugador 1, introduce tu nombre: ") #Introducción del nombre de los jugadores
    print()

    mostrar(tablero,numeros) #Muestra el tablero inicial
    print()

    cont = 0   #Variable que contará el número de turnos hasta el final del juego

    while True: #Turnos infinitos hasta que alguien gane
  
      jugar(jugador1,"o") #Turno del jugador 1 con ficha "o"

      print()

      mostrar(tablero,numeros) #Muestra el tablero luego de la jugada

      cont = cont + 1

      comprobacion = controles.comprobar(tablero,"o") #Comprueba con las fichas del jugador 1
      if comprobacion == True: 
        ganador = jugador1 #Si gana, declara al jugador 1 como ganador y se rompe el while
        break

      tab_lleno = controles.tablero_lleno(tablero) #Comprueba si el tablero esta lleno
      if tab_lleno == True:
        ganador = "Empate" #Si el tablero esta lleno declara al ganador como empate y rompe el while
        break

      print()

      base_bot.jugar_bot_media(tablero,"+","o") #Turno de la IA con ficha "+"

      print()

      mostrar(tablero,numeros) #Muestra el tablero luego de la jugada

      comprobacion = controles.comprobar(tablero,"+") #Comprueba con las fichas del jugador 2
      if comprobacion == True: 
        ganador = "IA" #Si gana, declara a la IA como ganadora y se rompe el while
        break

      tab_lleno = controles.tablero_lleno(tablero) #Comprueba si el tablero esta lleno
      if tab_lleno == True:
        ganador = "Empate" #Si el tablero esta lleno declara al ganador como empate y rompe el while
        break

      print()

print()
print("JUEGO TERMINADO") #Termina el juego
print()
print("Ganador:",ganador) #Se menciona al jugador ganador
print()

if modo == 1:
  if dificultad == 1:
    if ganador != "IA":
      print("FELICIDADES, ESTAS EN EL TOP")
      controles.rank_media(ganador,cont)
    print()
    print("MEJORES PUNTUACIONES (DIFICULTAD MEDIA)")
    print()
    print("Gana en el menor número de jugadas para aparecer")
    print()
    archivo3 = open("ranking_media.txt","r")
    for puesto in archivo3:
      datos = puesto.split(" ")
      print("Nombre: " + datos[0], end="   ")
      print("Puntaje: "+(str(int(datos[1])))+"\n")
    archivo3.close()
  else:
    if ganador != "IA":
      print("FELICIDADES, GANASTE A LA IA EN MODO LEYENDA")
      controles.rank_leyen(ganador)
    print("GANADORES (DIFICULTAD LEYENDA)")
    print()
    print("Gana en dificultad leyenda para aparecer")
    print()
    archivo3 = open("ranking_leyenda.txt","r")
    for puesto in archivo3:
      datos = puesto.split(" ")
    archivo3.close()
    for i in range(0,len(datos)):
      print("Nombre: " + datos[i])

print()
print("GRACIAS POR JUGAR") #Gracias por jugar y escuchar nuestra explicación :D
