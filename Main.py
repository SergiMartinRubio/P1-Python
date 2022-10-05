from random import randint, randrange, random
import random
import funcions, janken, triarNum, penjat

           

continuar = True
while(continuar):
    print("-------------------")
    print("1- Adivina Numero")
    print("2- Pedra Paper Tisores")
    print("3- El Penjat")
    print("4- Sortir")
    print("-------------------")
    opcioJoc = funcions.introduirNum(1,4)
        
    if(opcioJoc==1):
        triarNum.jocTriarNum()          
    elif(opcioJoc==2):
        janken.pedraPaperTisora()
    elif(opcioJoc==3):
        penjat.penjat()
    elif(opcioJoc==4):
        continuar = False
        print("Fins Aviat!!!")
    else:
        print("La opcio triada es incorrecta, torna a intentar-ho")