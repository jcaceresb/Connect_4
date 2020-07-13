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
        if t[i][diag] == n and t[i+1][diag-1] == n and t[i+2][diag-2] == n and t[i+3][diag-3] == n: #Posiciones
          cond1 = True
          break

    break
  return cond1 #Devuelve el valor de "cond1"

def tablero_lleno(t): #Funcion para definir el tablero lleno
  lleno = True
  for i in range(0,len(t)): #Recorre todo el tablero
    for j in range(0,7):
      if t[i][j] == " ": #Si hay al menos un hueco, indica que no está lleno
        lleno = False
        break
  return lleno #devuelve el valor de lleno

def rank_media(gan,num):  #Funcion para evaluar si entras al top en modo medio
  nombres = []
  puntajes = []
  archivo = open("ranking_media.txt","r")
  for puesto in archivo:   #Recibe el nombre y puntajes existentes
    datos = puesto.split(" ")
    nombres.append(datos[0])
    puntajes.append(int(datos[1]))
  archivo.close()

  if num <= puntajes[4]:   #Evalua hasta donde puedes posicionarte
    if num <= puntajes[3]:
      if num <= puntajes[2]:
        if num <= puntajes[1]:
          if num <= puntajes[0]:
            nombres[4] = nombres[3]
            puntajes[4] = puntajes[3]
            nombres[3] = nombres[2]
            puntajes[3] = puntajes[2]
            nombres[2] = nombres[1]
            puntajes[2] = puntajes[1]
            nombres[1] = nombres[0]
            puntajes[1] = puntajes[0]
            puntajes[0] = num
            nombres[0] = gan
          else:
            nombres[4] = nombres[3]
            puntajes[4] = puntajes[3]
            nombres[3] = nombres[2]
            puntajes[3] = puntajes[2]
            nombres[2] = nombres[1]
            puntajes[2] = puntajes[1]
            puntajes[1] = num
            nombres[1] = gan
        else:
          nombres[4] = nombres[3]
          puntajes[4] = puntajes[3]
          nombres[3] = nombres[2]
          puntajes[3] = puntajes[2]
          puntajes[2] = num
          nombres[2] = gan
      else:
        nombres[4] = nombres[3]
        puntajes[4] = puntajes[3]
        puntajes[3] = num
        nombres[3] = gan
    else:
      puntajes[4] = num
      nombres[4] = gan

  archivo2 = open("ranking_media.txt","w+") #Si entras, reeescribe el top
  for i in range(0,len(nombres)):
    if i != len(nombres)-1:
      archivo2.write(nombres[i]+" "+str(puntajes[i])+"\n")
    else:
      archivo2.write(nombres[i]+" "+str(puntajes[i]))
  archivo2.close()

def rank_leyen(gana):   #Funcion para el TOP si ganas a la IA en "LEYENDA"
  nombres=[]
  archivo = open("ranking_leyenda.txt","r") #Lee todos los nombres
  for puesto in archivo:
    datos = puesto.split(" ")
  archivo.close()
  datos.append(gana)   #Añade tu nombre

  archivo2 = open("ranking_leyenda.txt","w+")   #Reescribe todos los nombres con el del jugador reciente incluido
  for i in range(0,len(datos)):
    if i != len(datos)-1:
      archivo2.write(datos[i]+" ")
    else: 
      archivo2.write(datos[i])
  archivo2.close()
