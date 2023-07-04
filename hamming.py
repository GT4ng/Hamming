#Prueba


class Hamming:
    
    #Inicia el codigo insertando los 7 bits
    #Los bits a insertar solo son 0 o 1. Cualquier caracter que no sean esos valores no se aceptara

    def __init__(self):
        self.datos = input("Ingrese el codigo de 7 digitos a enviar: ")
        self.datosList = []
        tamaño = len(self.datos)
        if(tamaño == 7):
            for i in range(tamaño):
                self.datosList.append(int(self.datos[i]))
        else:
            print("La cantidad de bits no es el suficiente. Intente nuevamente :)")
        print("El codigo ingresado es: ")
        print(self.datosList)
        print("\n")

    #paridad(): Ingresa los bits de Paridad al codigo
    #           A los 7 bits que se insertaron se le agregan los bits de paridad

    def paridad(self):
        p = "X"
        self.hammingX = []
        for i in range(11):
            cont = i-3
            if(i == 0 or i== 1 or i ==3 or i==7):
                self.hammingX.append(p)
                if(i == 7):
                    self.hammingX.append(self.datosList[cont])
            else:
                if(cont < 7):
                    aux1 = self.datosList[cont]
                    self.hammingX.append(aux1)
        print("El codigo ingresado es: ")
        print(self.hammingX)
        print("\nColocando los bits de paridad: ")
        print(len(self.hammingX))
        print("\n")

    #logica(): Calcula los bits de paridad y se les asigna el bit correspondiente
    #          los valores "X" se reemplazan basados en la teoria de si existe
    #          paridad con los bits contados en todo el array

    def logica(self):
        self.p = 0
        indicador = 0
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        if(indicador == 0):

            for i in range(1,11):
                if(i%2 == 0):
                    p1 = p1 + self.hammingX[i]
            if(p1%2 == 0):
                self.hammingX[indicador] = 0
            elif(p1%2 != 0):
                self.hammingX[indicador] = 1
            indicador = indicador + 1

        if(indicador == 1):
            
            p2 = self.hammingX[2] + self.hammingX[5] + self.hammingX[6] + self.hammingX[9] + self.hammingX[10]
            if(p2%2 == 0):
                self.hammingX[indicador] = 0
            elif(p2%2 != 0):
                self.hammingX[indicador] = 1
            indicador = indicador + 2

        if(indicador == 3):

            p3 = self.hammingX[4] + self.hammingX[5] + self.hammingX[6]
            if(p3%2 == 0):
                self.hammingX[indicador] = 0
            elif(p3%2 != 0):
                self.hammingX[indicador] = 1
            indicador = indicador + 4   

        if(indicador == 7):

            p4 = self.hammingX[8] + self.hammingX[9] + self.hammingX[10]
            if(p4%2 == 0):
                self.hammingX[indicador] = 0
            elif(p4%2 != 0):
                self.hammingX[indicador] = 1
            indicador = indicador + 4       

        print("El mensaje completo con bits de paridad: ")
        print(self.hammingX)
        print("\n")

#calcHamming(): Ejecuta el calculo de bits

    def calcHamming(self):
        for i in range(11):
            identificador = self.hammingX[i]
            if(identificador == "X"):
                self.logica()
                self.p = self.p + 1

#introError(): Segun el mensaje obtenido con el codigo hamming se le asigna
#              el valor "n" indica la posicion del bit que se va a cambiar

    def introError(self):
        n = int(input("introduzca la posicion del bit en la que desea introducir el error: "))
        print("\n")
        if(n>0 or n<11):
            valor = self.hammingX[n-1]
            if(valor == 1):
                self.hammingX[n-1] = 0
            else:
                self.hammingX[n-1] = 1        
        else:
            print("Por favor introduzca una posicion valida")
        print("Codigo con error: ")
        print(self.hammingX)

# Se inicia la clase y se ejecuta en orden descendente
prueba1 = Hamming()
prueba1.paridad()
prueba1.calcHamming()
prueba1.introError()