import controles_bot

def jugar_bot_leyenda(tab,val,val2):   #Jugada del bot en modo "LEYENDA"
  print("Turno de la IA")
  rpta, fila = controles_bot.jugada_bot(tab,val) #Busca jugada ganadora con sus fichas
  if rpta == True:
    fila = fila + 1 #Transforma el valor recibido a coordenadas para que juege el bot
  else:
    rpta, fila = controles_bot.jugada_bot(tab,val2) #Busca jugada para bloquear a jugador
    if rpta == True:
      fila = fila + 1 #Transforma el valor recibido a coordenadas para que juege el bot
    else:
      while True:
        fila = controles_bot.jugada_bot2() #Numero aleatorio entre 1 a 7
        if tab[0][fila-1] == " ": #Si el tablero presenta  la casilla superior vacía (espacio para la ficha), acepta y rompe el while
          break
  for i in range(0,len(tab)): #Recorre el tablero
    if tab[i][fila-1] != " ": # Cae hasta que encuentra una ficha y se pone un sitio anterior
      tab[i-1][fila-1] = val
      break
    elif i == 5:
      tab[i][fila-1] = val

def jugar_bot_media(tab,val,val2):  #Jugada del bot en modo "MEDIA"
  print("Turno de la IA")
  rpta, fila = controles_bot.jugada_bot(tab,val2) #Busca jugada a bloquear dek jugador
  if rpta == True:
    fila = fila + 1
  else:
    while True:
      fila = controles_bot.jugada_bot2()   #Numero aleatorio entre 1 y 7
      if tab[0][fila-1] == " ": #Si el tablero presenta  la casilla superior vacía (espacio para la ficha), acepta y rompe el while
        break
  for i in range(0,len(tab)): #Recorre el tablero
    if tab[i][fila-1] != " ": # Cae hasta que encuentra una ficha y se pone un sitio anterior
      tab[i-1][fila-1] = val
      break
    elif i == 5:
      tab[i][fila-1] = val
