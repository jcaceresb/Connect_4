def mostrar(x):
  for i in range(0,len(x)): #Imprime el tablero igual a tablero de connect 4
    print(x[i])

def comprobar(t,n):
  while True: #Para que continue comprobando co todas las opciones
    cond1 = False #La condicion que cambiará si hay una jugada ganadora
    for i in range(0,len(t)): #Comprobación horizontal
      for fila in range(0,4):
        if t[i][fila] == n and t[i][fila+1] == n and t[i][fila+2] == n and t[i][fila+3] == n: #Posiciones
          cond1 = True #Si gana, cambia la condicion y termina el for
          break

    if cond1 == True:
      break #Si gana, termina el while general
  
    for i in range(0,7): #Comprobación vertical
      for col in range(0,3):
       if t[col][i] == n and t[col+1][i] == n and t[col+2][i] == n and t[col+3][i] == n: #Posiciones
          cond1 = True
          break

    if cond1 == True:
     break

    for i in range(0,3): #Comprobación en diagonal 1
      for diag in range(0,4):
        if t[i][diag] == n and t[i+1][diag+1] == n and t[i+2][diag+2] == n and t[i+3][diag+3] == n: #Posiciones
          cond1 = True
          break
      
    if cond1 == True:
      break

    for i in range(0,3): #Comrpobación en diagonal 2
      for diag in range(3,7):
        if t[i][diag] == n and t[i-1][diag-1] == n and t[i-2][diag-2] == n and t[i-3][diag-3] == n: #Posiciones
          cond1 = True
          break

    break
  return cond1 #Devuelve el valor de "cond1"

def jugar(jug,val): #Para cada turno de jugador
  preg = jug + ", introduzca un número (1-7): " #Define la pregunta usando el nombre
  while True: #Ciclo infinito para obligar al jugador a tener una jugada válida
    num = int(input(preg)) #Pregunta el lugar de la casilla
    if tablero[0][num-1] == 0: #Si el tablero presenta la casilla superior vacía (espacio para la ficha), acepta y rompe el while
      break
  for i in range(0,len(tablero)): #Recorre el tablero
    if tablero[i][num-1] != 0: # Cae hasta que encuentra una ficha y se pone un sitio anterior
      tablero[i-1][num-1] = val
      break
    elif i == 5:
      tablero[i][num-1] = val #Cae hasta el final del tablero si la columna está vacía

def tablero_lleno(t): #Funcion para definir el tablero lleno
  lleno = True
  for i in range(0,len(t)): #Recorre todo el tablero
    for j in range(0,7):
      if t[i][j] == 0: #Si hay al menos un hueco, indica que no está lleno
        lleno = False
        break
  return lleno #devuelve el valor de lleno

print("BENVENIDOS A CONNECT 4") #Introduccion del juego
print()
print("Hecho por: Jose Caceres, Augusto Bracamonte y Vasco Bustamante")
print()
jugador1 = input("Jugador 1, introduce tu nombre: ") #Introducción del nombre de los jugadores
print()
jugador2 = input("Jugador 2, introduce tu nombre: ")
print()

tablero = [[0,0,0,0,0,0,0], #Define el tablero
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

mostrar(tablero) #Muestra el tablero inicial
print()

while True: #Turnos infinitos hasta que alguien gane
  
  jugar(jugador1,1) #Turno del jugador 1 con ficha "1"

  print()

  mostrar(tablero) #Muestra el tablero luego de la jugada

  comprobacion = comprobar(tablero,1) #Comprueba con las fichas del jugador 1
  if comprobacion == True: 
    ganador = jugador1 #Si gana, declara al jugador 1 como ganador y se rompe el while
    break

  tab_lleno = tablero_lleno(tablero) #Comprueba si el tablero esta lleno
  if tab_lleno == True:
    ganador = "Empate" #Si el tablero esta lleno declara al ganador como empate y rompe el while
    break

  print()

  jugar(jugador2,2) #Turno del jugador 2 con ficha "2"

  print()

  mostrar(tablero) #Muestra el tablero luego de la jugada

  comprobacion = comprobar(tablero,2) #Comprueba con las fichas del jugador 2
  if comprobacion == True: 
    ganador = jugador2 #Si gana, declara al jugador 2 como ganador y se rompe el while
    break

  tab_lleno = tablero_lleno(tablero) #Comprueba si el tablero esta lleno
  if tab_lleno == True:
    ganador = "Empate" #Si el tablero esta lleno declara al ganador como empate y rompe el while
    break

  print()

print()
print("JUEGO TERMINADO") #Termina el juego
print()
print("Ganador:",ganador) #Se menciona al jugador ganador
print()
print("GRACIAS POR JUGAR") #Gracias por jugar y escuchar nuestra explicación :D
