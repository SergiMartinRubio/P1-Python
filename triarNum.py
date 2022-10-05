from random import randint, randrange, random
import random, funcions

#funcion para llamar el inicio del juego de elegir numero
def jocTriarNum():
    #explicamos las normas y inicializamos las variables
    print("Has triat el joc d'adivina el numero, tens tres intents d'esbrinar un numero del 1 al 10")
    sortirJoc=False
    vidas=3
    numeroAleatori = randint(1, 10)
    #bucle donde se localiza el juego
    while(not sortirJoc):
        #mostramos las vidas cada turno y pedimos un numero del 1 al 10
        print(f"Tens {vidas} vides")
        numeroTriat = funcions.introduirNum(1,10)
        #comprobamos el numero que ha introducido el usuario y respondemos acorde a lo introducido
        if(numeroTriat==numeroAleatori):
            sortirJoc="True"
            print(f"Has Guanyat en {3-vidas +1} intents")
        elif(numeroTriat<numeroAleatori):
            print("El teu numero es mes petit que el numero aleatori")
            vidas-=1
        elif(numeroTriat>numeroAleatori):
            print("El teu numero es mes gran que el numero aleatori")
            vidas-=1
        #si se nos acaban las vidas salimos del juego y mostramos mensaje personalizado
        if(vidas<=0):
            sortirJoc="True"
            print("No has esbrinat el numero")
 