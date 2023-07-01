import tkinter as tk
import serial

def generar_codigo_hamming():
    numero = int(entry_numero.get())
    # Generar código de Hamming
    codigo_hamming = generar_hamming(numero)
    # Enviar el código a Arduino a través de comunicación serial
    enviar_a_arduino(codigo_hamming)

def generar_hamming(numero):
    # Aquí puedes implementar el algoritmo de generación de código Hamming
    # Según tus necesidades específicas

    # Ejemplo de implementación:
    codigo_hamming = numero + 10  # Simplemente agrega 10 al número

    return codigo_hamming

def enviar_a_arduino(codigo_hamming):
    # Configuración de la comunicación serial con el Arduino
    puerto_serial = serial.Serial('/dev/ttyACM0', 9600)  # Ajusta el puerto y la velocidad según tu Arduino

    # Envío del código Hamming al Arduino
    puerto_serial.write(str(codigo_hamming).encode())

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Generador de código Hamming")

frame = tk.Frame(ventana)
frame.pack(pady=20)

label_numero = tk.Label(frame, text="Número:")
label_numero.pack()

entry_numero = tk.Entry(frame)
entry_numero.pack()

boton_generar = tk.Button(frame, text="Generar código Hamming", command=generar_codigo_hamming)
boton_generar.pack()

ventana.mainloop()