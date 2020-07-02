def mostrar(x):
  for i in range(0,len(x)):
    print(x[i])

def comprobar(t,n):
  while True:
    cond1 = False
    for i in range(0,len(t)):
      for fila in range(0,4):
        if t[i][fila] == n and t[i][fila+1] == n and t[i][fila+2] == n and t[i][fila+3] == n:
          cond1 = True
          break

    if cond1 == True:
      break
  
    for i in range(0,7):
      for col in range(0,3):
       if t[col][i] == n and t[col+1][i] == n and t[col+2][i] == n and t[col+3][i] == n:
          cond1 = True
          break

    if cond1 == True:
     break

    for i in range(0,3):
      for diag in range(0,4):
        if t[i][diag] == n and t[i+1][diag+1] == n and t[i+2][diag+2] == n and t[i+3][diag+3] == n:
          cond1 = True
          break
      
    if cond1 == True:
      break

    for i in range(0,3):
      for diag in range(3,7):
        if t[i][diag] == n and t[i-1][diag-1] == n and t[i-2][diag-2] == n and t[i-3][diag-3] == n:
          cond1 = True
          break

    break
  return cond1

def jugar(jug,val):
  preg = jug + ", introduzca un número (1-7): "
  while True:
    num = int(input(preg))
    if tablero[0][num-1] == 0:
      break
  for i in range(0,len(tablero)):
    if tablero[i][num-1] != 0:
      tablero[i-1][num-1] = val
      break
    elif i == 5:
      tablero[i][num-1] = val

def tablero_lleno(t):
  lleno = True
  for i in range(0,len(t)):
    for j in range(0,7):
      if t[i][j] == 0:
        lleno = False
        break
  return lleno

print("BENVENIDOS A CONNECT 4")
print()
print("Hecho por: Jose Caceres, Augusto Bracamonte y Vasco Bustamante")
print()
jugador1 = input("Jugador 1, introduce tu nombre: ")
print()
jugador2 = input("Jugador 2, introduce tu nombre: ")
print()

tablero = [[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

mostrar(tablero)
print()

while True:
  
  jugar(jugador1,1)

  print()

  mostrar(tablero)

  comprobacion = comprobar(tablero,1)
  if comprobacion == True:
    ganador = jugador1
    break

  tab_lleno = tablero_lleno(tablero)
  if tab_lleno == True:
    ganador = "Empate"
    break

  print()

  jugar(jugador2,2)

  print()

  mostrar(tablero)

  comprobacion = comprobar(tablero,2)
  if comprobacion == True:
    ganador = jugador2
    break

  tab_lleno = tablero_lleno(tablero)
  if tab_lleno == True:
    ganador = "Empate"
    break

  print()

print()
print("JUEGO TERMINADO")
print()
print("Ganador:",ganador)
print()
print("GRACIAS POR JUGAR")