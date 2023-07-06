import tkinter as tk


class HammingGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Hamming")
        
        self.label_datos = tk.Label(root, text="Ingrese el código de 7 dígitos a enviar:")
        self.label_datos.pack()
        
        self.entry_datos = tk.Entry(root)
        self.entry_datos.pack()
        
        self.button_calcular = tk.Button(root, text="Calcular Hamming", command=self.calcular_hamming)
        self.button_calcular.pack()
        
        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

    def calcular_hamming(self):
        datos = self.entry_datos.get()
        if len(datos) != 7:
            self.label_resultado.config(text="La cantidad de bits no es suficiente. Intente nuevamente.")
            return
        
        datos_list = []
        for i in range(len(datos)):
            datos_list.append(int(datos[i]))
        
        hamming = Hamming()
        hamming.datosList = datos_list
        hamming.paridad()
        hamming.calcHamming()

        resultado = "Mensaje completo con bits de paridad:\n" + str(hamming.hammingX)
        self.label_resultado.config(text=resultado)


class Hamming:

    def __init__(self):
        self.datosList = []
        self.hammingX = []

    def paridad(self):
        p = "X"
        for i in range(11):
            cont = i - 3
            if i == 0 or i == 1 or i == 3 or i == 7:
                self.hammingX.append(p)
                if i == 7:
                    self.hammingX.append(self.datosList[cont])
            else:
                if cont < 7:
                    aux1 = self.datosList[cont]
                    self.hammingX.append(aux1)

    def logica(self):
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        if indicador == 0:
            for i in range(1, 11):
                if i % 2 == 0:
                    p1 = p1 + self.hammingX[i]
            if p1 % 2 == 0:
                self.hammingX[indicador] = 0
            elif p1 % 2 != 0:
                self.hammingX[indicador] = 1

        if indicador == 1:
            p2 = self.hammingX[2] + self.hammingX[5] + self.hammingX[6] + self.hammingX[9] + self.hammingX[10]
            if p2 % 2 == 0:
                self.hammingX[indicador] = 0
            elif p2 % 2 != 0:
                self.hammingX[indicador] = 1

        if indicador == 3:
            p3 = self.hammingX[4] + self.hammingX[5] + self.hammingX[6]
            if p3 % 2 == 0:
                self.hammingX[indicador] = 0
            elif p3 % 2 != 0:
                self.hammingX[indicador] = 1

        if indicador == 7:
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

p1 = HammingGUI()



       