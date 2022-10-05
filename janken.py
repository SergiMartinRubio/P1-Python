from random import randint, randrange, random
import random
import funcions
#Funcion que asigna un punto a el ganador y muestra un mensaje
def jankenAsignarPunts(numeroTriat,numeroAleatori):
    #If que comprueban los movimientos y suma al ganador
    if(numeroTriat==1 and numeroAleatori==2):
        print("La maquina ha guanyat un punt")
        puntsMaquina+=1
    elif(numeroTriat==1 and numeroAleatori==3):
        print("Has guanyat un punt")
        punts+=1
    elif(numeroTriat==2 and numeroAleatori==1):
        print("Has guanyat un punt")
        punts+=1
    elif(numeroTriat==2 and numeroAleatori==3):
        print("La maquina ha guanyat un punt")
        puntsMaquina+=1
    elif(numeroTriat==3 and numeroAleatori==1):
        print("La maquina ha guanyat un punt")
        puntsMaquina+=1
    elif(numeroTriat==1 and numeroAleatori==2):
        print("Has guanyat un punt")
        punts+=1
    else:
        print("Empat")
        
#Funcion para llamar al juego de piedra papel tijeras
def pedraPaperTisora():
    #mostramos las normas y inicializamos variables necesarias para el juego
    print("Has triat el joc de pedra peper i tisores, has de arribar a 3 punts abans que la maquina per guanyar")
    sortirJoc=False
    punts=0
    puntsMaquina=0
    
    while(not sortirJoc):
        print("Pedra paper tisores 1 2 3 Ja")
        numeroAleatori = randint(1, 3)
        print("------------------")
        print("1-Pedra")
        print("2-Paper")
        print("3-Tisores")
        print("------------------")
        numeroTriat = funcions.introduirNum(1,3)
        movimientos = ["Pedra", "Paper", "Tisores"]
        #1 = Pedra
        #2 = Paper
        #3 = Tisores
        #Mostramos por texto la jugada del usuario y la de la maquina
        print(f"{movimientos[numeroTriat-1]} VS {movimientos[numeroAleatori-1]}")
        jankenAsignarPunts(numeroTriat,numeroAleatori)
       
       #Comprueba el ganador, sale del juego y muestra un mensaje dependiendo quien ha ganado
        if(punts>=3 or puntsMaquina>=3):
            sortirJoc="True"
            if(punts>puntsMaquina):   
                print("Has guanyat")
            else:
                print("Ha guanyat la maquina")
        else:
            input("Pulsa enter per continuar...")  
   