import qrcode

# Pedir el enlace al usuario
url = input("Ingresa el enlace que quieres convertir en QR: ")

# Crear el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Generar imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar archivo
nombre_archivo = "codigo_qr.png"
img.save(nombre_archivo)

print(f"QR generado correctamente y guardado como {nombre_archivo}")