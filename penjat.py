from random import randint, randrange, random
import random,funcions

#funcion que devuelve una linea aleatoria de un fichero
def escogerPalabra(txt):
    #Abrimos el archivo y dividimos en lineas
    lines = open(txt).read().splitlines()
    #Elegimos una de esas lineas utilizando una funcion predeterminada 
    return random.choice(lines)  
   
def penjat():
    #Mensaje de eplicacion de las normas y iniciamos variables
    print("Has triat el joc del penjat, has d'esbrinar la paraula abans que s'acabin els torns")
    sortirJoc=False
    
    
    palabraAleatoria = escogerPalabra("paraules.txt")
    #Calculamos los intentos multiplicando por 2 la longitud de las palabras
    intents=(len(palabraAleatoria)*2)
    
    #separamos cada letra y lo introducimos dentro de un array
    listaPalabraOriginal = [*palabraAleatoria]
    #mediante un for creamos un array de la misma longitud que la palabra original pero con "-" en cada posicion
    listaPalabraAcertar = ['-' for i in range(len(palabraAleatoria))]

    while(not sortirJoc):
        
        print(f"Intents Restants: {intents}")
        #for que imprime la lista con las letras que acertamos
        for letra in listaPalabraAcertar:
            print(f"{letra}", end =" ")
        print("")
        #pedimos un input de una letra
        lletraIntento = funcions.introduirLLetra()
        #restamos el intento
        intents-=1
        
        #si la letra esta dentro del array 
        if(lletraIntento in listaPalabraOriginal):
            #ejecutamos un bubcle donde comprobamos donde esta la letra y aplicamos el acierto
            for x in range(len(listaPalabraOriginal)):
                if(lletraIntento == listaPalabraOriginal[x]):
                    listaPalabraAcertar[x] = lletraIntento
           
        #Cuando hemos encontrado todas las letras terminamos el juego y ponemos el mensaje de victoria
        if(listaPalabraOriginal == listaPalabraAcertar):
            sortirJoc = True
            print(f"Has esbrinat la paraula: {palabraAleatoria}")
            input("Pulsa ENTER per continuar...")
        
        #en el caso que se nos terminen los intentos salimos del juego mostrando mensaje de derrota
        if(intents<=0):
            sortirJoc = True
            print(f"T'has quedat sense intents, la paraula era: {palabraAleatoria}")
            input("Pulsa ENTER per continuar...")
