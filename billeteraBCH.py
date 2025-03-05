#! /usr/bin/env python
import tkinter as tk
import random
import pyperclip
from mnemonic import Mnemonic

# Función para simular el lanzamiento de un dado de 6 caras
def lanzar_dado():
    return random.randint(0, 5)  # Convertir a rango 0-5

# Función para generar las 12 palabras usando los dados
def generar_palabras():
    mnemo = Mnemonic("spanish")

    palabras_lista = []
    
    for _ in range(12):  # Generar 12 palabras
        dado_resultado = 0
        for _ in range(11):  # Lanzar el dado 11 veces para obtener un número entre 0 y 2047
            dado_resultado = dado_resultado * 6 + lanzar_dado()
        
        dado_resultado = dado_resultado % 2048  # Asegurar que el número esté en el rango válido
        palabras_lista.append(mnemo.wordlist[dado_resultado])  # Obtener la palabra BIP-39
    
    # Mostrar las palabras enumeradas en la interfaz
    palabras_con_numeros = "\n".join([f"{i+1}. {palabra}" for i, palabra in enumerate(palabras_lista)])
    resultado_texto.delete(1.0, tk.END)  # Limpiar cualquier texto anterior
    resultado_texto.insert(tk.END, palabras_con_numeros)  # Insertar las nuevas palabras enumeradas

# Función para copiar las palabras generadas al portapapeles
def copiar_al_portapapeles():
    # Obtener solo el texto generado (sin saltos de línea extra al final)
    palabras_generadas = resultado_texto.get(1.0, tk.END).strip()
    pyperclip.copy(palabras_generadas)  # Copiar las palabras al portapapeles
    copiar_button.config(text="¡Copiado!", bg="#4CAF50", fg="white")
    ventana.after(1500, lambda: copiar_button.config(text="Copiar", bg="#008CBA", fg="white"))  # Volver a la etiqueta original

# Crear la ventana de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Generador de Billetera de Bitcoin Cash")
ventana.geometry("650x350")  # Ajustar el tamaño de la ventana
ventana.configure(bg="#2C3E50")  # Fondo oscuro elegante
ventana.resizable(False, False)

# Crear un título
titulo_label = tk.Label(ventana, text="Generador de 12 Palabras (BIP-39)", font=("Arial", 16, "bold"), fg="white", bg="#2C3E50")
titulo_label.pack(pady=15)

# Crear un botón para generar las palabras
generar_button = tk.Button(ventana, text="Generar Palabras", command=generar_palabras, font=("Arial", 12, "bold"), bg="#008CBA", fg="white", padx=10, pady=5, relief="raised")
generar_button.pack(pady=10)

# Crear el frame para contener la barra de desplazamiento
frame_resultado = tk.Frame(ventana)
frame_resultado.pack(pady=15)

# Crear una barra de desplazamiento vertical
scrollbar = tk.Scrollbar(frame_resultado, orient="vertical")

# Crear un área de texto para mostrar las palabras generadas
resultado_texto = tk.Text(frame_resultado, height=6, width=60, wrap="word", font=("Arial", 12, "bold"), bg="white", fg="#2C3E50", padx=10, pady=10, yscrollcommand=scrollbar.set)
resultado_texto.pack(side="left", padx=5)
scrollbar.config(command=resultado_texto.yview)
scrollbar.pack(side="right", fill="y")

# Botón para copiar las palabras
copiar_button = tk.Button(ventana, text="Copiar", command=copiar_al_portapapeles, font=("Arial", 12, "bold"), bg="#008CBA", fg="white", padx=10, pady=5, relief="raised")
copiar_button.pack(pady=5)

# Iniciar la interfaz gráfica
ventana.mainloop()
