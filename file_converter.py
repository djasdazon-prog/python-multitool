import subprocess
import tkinter as tk
from tkinter import filedialog
import os

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta ventana principal

    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[
            ("Todos los archivos", "*.*"),
            ("Audio", "*.mp3 *.wav *.ogg"),
            ("Video", "*.mp4 *.avi *.mkv"),
            ("Imagen", "*.png *.jpg *.jpeg *.jfif")
        ]
    )

    return archivo

def convertir():
    archivo = seleccionar_archivo()

    if not archivo:
        print("❌ No seleccionaste ningún archivo")
        return

    print("Archivo seleccionado:", archivo)

    formato = input("Formato de salida (mp3/mp4/png/jpg/etc): ")
    salida = "resultado." + formato

    try:
        subprocess.run(
            ["ffmpeg", "-i", archivo, salida],
            check=True
        )
        print("✔ Conversión completada:", salida)
    except subprocess.CalledProcessError:
        print("❌ Error al convertir")

convertir()