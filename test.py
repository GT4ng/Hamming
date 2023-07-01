import tkinter as tk
from tkinter import messagebox

def generar_codigo_hamming():
    numero = ""

    for entry in entries:
        try:
            digito = entry.get()
            numero += str(int(digito))
        except ValueError:
            # Manejar la entrada no válida
            pass
    
    if len(numero) == 7:
        codigo_hamming = calcular_codigo_hamming(numero)
        messagebox.showinfo("Resultado", "Código Hamming: {}".format(codigo_hamming))
    else:
        messagebox.showerror("Error", "Debe ingresar un número de 7 dígitos")
def calcular_codigo_hamming(numero):
    paridad = sum(map(int, numero)) % 2
    codigo_hamming = numero + str(paridad)
    
    return codigo_hamming

ventana = tk.Tk()
ventana.title("Generador de código Hamming")

entries = []
for i in range(7):
    label = tk.Label(ventana, text="Dígito {}: ".format(i+1))
    label.grid(row=i, column=0, sticky="e")
    
    entry = tk.Entry(ventana, width=2)
    entry.grid(row=i, column=1)
    entries.append(entry)

generar_boton = tk.Button(ventana, text="Generar código Hamming", command=generar_codigo_hamming)
generar_boton.grid(row=7, column=0, columnspan=2)
ventana.mainloop()