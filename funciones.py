def crear_tablero():
    import numpy as np
    tablero= np.full((10,10),"[ ]")
    return tablero

def crear_barco(eslora , tablero):
    import random
    while True:
     horizontal = random.choice([True, False])
     validez=True
     barco=[]
     x = random.randrange(0,10)
     y = random.randrange(0,10)
     if horizontal == True and x+eslora<10:
         for i in range(eslora):
             barco.append((x+i,y))
             if tablero[y][x+i]!="[ ]":         #Hacer con ands
                 validez=False
                 break
             if y < 9 and tablero[y + 1][x + i] != "[ ]":
                 validez = False
                 break
             if y > 0 and tablero[y - 1][x + i] != "[ ]":
                 validez = False
                 break
             if i == 0 and x > 0 and tablero[y][x - 1] != "[ ]":
                 validez = False
                 break
             if i == eslora - 1 and (x + eslora) < 10 and tablero[y][x + eslora] != "[ ]":
                 validez = False
                 break            
         if validez:
             return barco
     elif horizontal == False and y+eslora<10:
         for i in range(eslora):
             barco.append((x,y+i))
             if tablero[y+i][x]!="[]":
                 validez=False
                 break
             if x < 9 and tablero[y + i][x + 1] != "[ ]":
                 validez = False
                 break
             if x > 0 and tablero[y + i][x - 1] != "[ ]":
                 validez = False
                 break
             if i == 0 and y > 0 and tablero[y - 1][x] != "[ ]":
                 validez = False
                 break
             if i == eslora - 1 and (y + eslora) < 10 and tablero[y + eslora][x] != "[ ]":
                 validez = False
                 break
         if validez:
             return barco
         
def meter_barco(barco,tablero):
    for i in barco:
        tablero[i[1]][i[0]]="O"
    return tablero

def mostrar_tablero(tablero):
    print("\n      " + "".join(f"{col:<4}" for col in range(1, 11)) + "\n   " + "-" * 43)
    for i, fila in enumerate(tablero, start=1):
        render = [c if c == "[ ]" else c.center(3) for c in fila]
        print(f"{i:2d} | {' '.join(render)} |")
        
    print("   " + "-" * 43 + "\n")

