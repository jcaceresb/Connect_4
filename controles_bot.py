import random

def jugada_bot2():
  return random.randrange(1,8)

def jugada_bot(t,x):
  cond2 = False
  colum = 0
  while True:
    for fila in range(5,2,-1):
      for col in range(0,4):
        if t[fila][col] == x and t[fila-1][col+1] == x and t[fila-2][col+2] == x and t[fila-3][col+3] == " " and t[fila-2][col+3] != " ":
          cond2 = True
          colum = col + 3
          break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(5,2,-1):
      for col in range(3,7):
        if t[fila][col] == x and t[fila-1][col-1] == x and t[fila-2][col-2] == x and t[fila-3][col-3] == " " and t[fila-2][col-3] != " ":
          cond2 = True
          colum = col - 3
          break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(5,2,-1):
      for col in range(0,4):
        if t[fila][col] == x and t[fila-1][col+1] == x and t[fila-2][col+2] == " " and t[fila-3][col+3] == x and t[fila-1][col+2] != " ":
          cond2 = True
          colum = col + 2
          break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(5,2,-1):
      for col in range(3,7):
        if t[fila][col] == x and t[fila-1][col-1] == x and t[fila-2][col-2] == " " and t[fila-3][col-3] == x and t[fila-1][col-2] != " ":
          cond2 = True
          colum = col - 2
          break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(5,2,-1):
      for col in range(0,4):
        if t[fila][col] == x and t[fila-1][col+1] == " " and t[fila-2][col+2] == x and t[fila-3][col+3] == x and t[fila][col+1] != " ":
          cond2 = True
          colum = col + 1
          break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(5,2,-1):
      for col in range(3,7):
        if t[fila][col] == x and t[fila-1][col-1] == " " and t[fila-2][col-2] == x and t[fila-3][col-3] == x and t[fila][col-1] != " ":
          cond2 = True
          colum = col - 1
          break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(5,2,-1):
      for col in range(0,4):
        if t[fila][col] == " " and t[fila-1][col+1] == x and t[fila-2][col+2] == x and t[fila-3][col+3] == x:
          if fila == 5:
            cond2 = True
            colum = col
            break
          elif t[fila+1][col] != " ":
            cond2 = True
            colum = col
            break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(5,2,-1):
      for col in range(3,7):
        if t[fila][col] == " " and t[fila-1][col-1] == x and t[fila-2][col-2] == x and t[fila-3][col-3] == x:
          if fila == 5:
            cond2 = True
            colum = col
            break
          elif t[fila+1][col] != " ":
            cond2 = True
            colum = col
            break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(len(t)-1,-1,-1):
      for col in range(0,4):
        if t[fila][col] == x and t[fila][col+1] == x and t[fila][col+2] == x and t[fila][col+3] == " ":
          if fila == 5:
            cond2 = True
            colum = col+3
            break
          elif t[fila+1][col+3] != " ":
            cond2 = True
            colum = col+3
            break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(len(t)-1,-1,-1):
      for col in range(0,4):
        if t[fila][col] == x and t[fila][col+1] == x and t[fila][col+2] == " " and t[fila][col+3] == x:
          if fila == 5:
            cond2 = True
            colum = col+2
            break
          elif t[fila+1][col+2] != " ":
            cond2 = True
            colum = col+2
            break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(len(t)-1,-1,-1):
      for col in range(0,4):
        if t[fila][col] == x and t[fila][col+1] == " " and t[fila][col+2] == x and t[fila][col+3] == x:
          if fila == 5:
            cond2 = True
            colum = col+1
            break
          elif t[fila+1][col+1] != " ":
            cond2 = True
            colum = col+1
            break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for fila in range(len(t)-1,-1,-1):
      for col in range(0,4):
        if t[fila][col] == " " and t[fila][col+1] == x and t[fila][col+2] == x and t[fila][col+3] == x:
          if fila == 5:
            cond2 = True
            colum = col
            break
          elif t[fila+1][col] != " ":
            cond2 = True
            colum = col
            break
      if cond2 == True:
        break
    if cond2 == True:
      break

    for col in range(0,len(t)+1):
      for fila in range(len(t)-1,2,-1):
        if t[fila][col] == x and t[fila-1][col] == x and t[fila-2][col] == x and t[fila-3][col] == " ":
          cond2 = True
          colum = col
          break
      if cond2 == True:
        break
    break

  return cond2, colum
