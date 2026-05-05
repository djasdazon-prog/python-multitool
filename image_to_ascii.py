from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

# Activar ANSI en Windows
os.system("")

ASCII_CHARS = "@#W$9876543210?!abc;:+=-,._ "

def resize_image(image, new_width=100):
    w, h = image.size
    return image.resize((new_width, int(h / w * new_width * 0.55)))

def elegir_imagen():
    root = tk.Tk()
    root.withdraw()  # ocultar ventana principal

    file_path = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[
            ("Imágenes", "*.png *.jpg *.jpeg *.bmp *.webp"),
            ("Todos los archivos", "*.*")
        ]
    )

    return file_path

def convertir_ascii_color(path):
    img = Image.open(path).convert("RGB")
    img = resize_image(img)

    pixels = list(img.getdata())
    w = img.width

    for i in range(0, len(pixels), w):
        linea = ""
        for j in range(w):
            r, g, b = pixels[i + j]

            gray = (r + g + b) // 3
            idx = gray * len(ASCII_CHARS) // 256
            char = ASCII_CHARS[idx]

            linea += f"\033[38;2;{r};{g};{b}m{char}"

        print(linea + "\033[0m")

# ===== MAIN =====
print("=== ASCII COLOR DESDE CUALQUIER IMAGEN ===")

ruta = elegir_imagen()

if ruta:
    print(f"\nConvirtiendo: {ruta}\n")
    convertir_ascii_color(ruta)
else:
    print("No seleccionaste ninguna imagen.")