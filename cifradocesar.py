import pyfiglet

#codigos de colores
cierre = '\033[39m'  
ligth_verde="\033[1;32m"

#banner de color verde
baner = (pyfiglet.figlet_format("CIFRADO CESAR"))
print(ligth_verde,baner,cierre)


alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

while True:
    print("\n[1]Cifrar texto\n[0]Salir\n")
    #Usamos la variable opcion como string para que sea mas facil trabajar con las condicionales
    opcion = input("Elija una opción >> ")

    if opcion == "1":
      
        texto_plano = input("\nEscriba su texto a cifrar: ")
        texto_plano = texto_plano.upper()
        #En caso se introduzca un string como n° clave, se ejecuta la excepcion
        try:
            k = int(input("Escriba el número de clave >> "))
        except ValueError:
            print("\nLa clave debe ser un número!")
            break

        #Lista donde almacenaremos el texto ya cifrado    
        texto_cifrado = []

        #longitud del alfabeto
        len_alfabeto = len(alfabeto)
       
        

        for i in texto_plano:
            try:
                indice = alfabeto.index(i)
            except ValueError:
                print("El texto a cifrar solo debe contener letras!")
                break
                
            newindice = indice+k
            
            #en caso el valor del indice sobrepase la longitud del alfabeto se ejecutara el if
            if newindice > len_alfabeto:
                newindice = (newindice) - len_alfabeto
            texto_cifrado.append(alfabeto[newindice])
            
            
        #convertir la lista "palabracifrada" en cadena con el metodo "".join()
        texto_cifrado ="".join(texto_cifrado)  
        
        print(ligth_verde,texto_cifrado,cierre)
        
    elif opcion == "0":
        break

    else:
        print("Elija una opción correcta!")



    
