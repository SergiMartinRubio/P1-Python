#Funcion que comprueba el input del usuario para que sea valido, en este caso un numero entre el min y max
def introduirNum(min,max):
    isnum=False
    while(not isnum):
        num = input("Introdueix un numero ")
        #comprueba que sea numerico
        if(num.isnumeric() == True):
            #comprueba que el numero introducido esta entre los deseados
            if(int(num)>=min and int(num)<=max):
                #sale del bucle
                isnum= True 
            else:
                print(f"Introdueix un numero entre el {min} i el {max}")
        else:
            print("Intrudueix un numero")
    #devuelve el numero pasado a int
    return int(num)

#Funcion que comprueba el input del usuario para que sea valido, en este caso para que sea una letra y un solo caracter
def introduirLLetra():
    isalpha=False
    while(not isalpha):
        lletra = input("Introdueix una LLetra: ")
        #comprueba que el caracter sea una letra
        if(lletra.isalpha() == True):
            #compreba que sea solamente 1 caracter
            if(len(lletra)==1):
                isalpha = True
            else:
                print("Volem solament una lletra")
        
    return lletra.lower()
