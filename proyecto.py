from funciones import crear_tablero , crear_barco , mostrar_tablero , meter_barco
import numpy as np
import os
import time
tablero_jugador1= crear_tablero()
tablerod_jugador1= crear_tablero()
tablero_rival= crear_tablero()
tablerod_rival= crear_tablero()

barco = crear_barco(4,tablero_jugador1)
tablero_jugador1=meter_barco(barco,tablero_jugador1)
barco = crear_barco(3,tablero_jugador1)
tablero_jugador1=meter_barco(barco,tablero_jugador1)
barco = crear_barco(3,tablero_jugador1)
tablero_jugador1=meter_barco(barco,tablero_jugador1)
barco = crear_barco(2,tablero_jugador1)
tablero_jugador1=meter_barco(barco,tablero_jugador1)
barco = crear_barco(2,tablero_jugador1)
tablero_jugador1=meter_barco(barco,tablero_jugador1)
barco = crear_barco(2,tablero_jugador1)
tablero_jugador1=meter_barco(barco,tablero_jugador1)

barco = crear_barco(4,tablero_rival)
tablero_rival=meter_barco(barco,tablero_rival)
barco = crear_barco(3,tablero_rival)
tablero_rival=meter_barco(barco,tablero_rival)
barco = crear_barco(3,tablero_rival)
tablero_rival=meter_barco(barco,tablero_rival)
barco = crear_barco(2,tablero_rival)
tablero_rival=meter_barco(barco,tablero_rival)
barco = crear_barco(2,tablero_rival)
tablero_rival=meter_barco(barco,tablero_rival)
barco = crear_barco(2,tablero_rival)
tablero_rival=meter_barco(barco,tablero_rival)

turno_jugador=True
os.system('cls' if os.name == 'nt' else 'clear')
mostrar_tablero(tablerod_jugador1) 
mostrar_tablero(tablero_jugador1) 
mostrar_tablero(tablero_rival) 
while True:
    existeplayer = "O" in tablero_jugador1
    existerival = "O" in tablero_rival
    if existeplayer== False:
        print("has perdido")
        break
    elif existerival== False:
        print("has ganado")
        break
    else:
        if turno_jugador==True:
            disparox=int(input("elige coordenada x (del 1 al 10) : "))-1
            disparoy=int(input("elige coordenada y (del 1 al 10) : "))-1
            if  disparox < 0 or disparox >= 10 or disparoy < 0 or disparoy >= 10   :
                print ("zona no valida")
                continue
            else:
                if tablero_rival[disparoy][disparox] != "[ ]" and tablero_rival[disparoy][disparox] != "O" :
                    print ("zona no valida")
                    continue
                elif  tablero_rival[disparoy][disparox] == "[ ]":
                    tablerod_jugador1 [disparoy][disparox] ="X"
                    tablero_rival [disparoy][disparox] ="X"
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ("has fallado")
                    mostrar_tablero(tablerod_jugador1)
                    mostrar_tablero(tablero_jugador1)
                    turno_jugador=False
                    continue
                elif  tablero_rival[disparoy][disparox] == "O":
                    tablerod_jugador1 [disparoy][disparox] ="I"
                    tablero_rival [disparoy][disparox] ="I"
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print ("has acertado")
                    mostrar_tablero(tablerod_jugador1)
                    mostrar_tablero(tablero_jugador1)             
                    continue
        elif turno_jugador==False:
            disparox=numero = np.random.randint(0, 10)
            disparoy=numero = np.random.randint(0, 10)
            if  tablero_jugador1[disparoy][disparox] == "[ ]":
                tablero_jugador1 [disparoy][disparox] ="X"
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("fallo del rival",disparox,disparoy)
                mostrar_tablero(tablerod_jugador1)
                mostrar_tablero(tablero_jugador1)
                time.sleep(1.5)
                turno_jugador=True
                continue
            elif  tablero_jugador1[disparoy][disparox] == "O":
                tablero_jugador1 [disparoy][disparox] ="I"
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("impacto del rival",disparox,disparoy) 
                mostrar_tablero(tablerod_jugador1)
                mostrar_tablero(tablero_jugador1)
                time.sleep(1.5)          
                continue
            elif  tablero_jugador1[disparoy][disparox] != "[ ]" and tablero_jugador1[disparoy][disparox] != "O" :
                continue