import cv2
import numpy as np

# Cargar la imagen subida
imagen = cv2.imread('foto.jpg')

if imagen is None:
    print("Error: No se encontró la imagen 'foto.jpg'. Asegúrate de subirla y nombrarla igual.")
else:
    # Extraer el canal verde (el color rosa tiene poco verde, así que oscurece el fondo y resalta el texto)
    b, g, r = cv2.split(imagen)

    # Aumentar contraste
    canal_verde_contrastado = cv2.equalizeHist(g)

    # Convertir a blanco y negro puro para aislar las letras
    _, resultado_binary = cv2.threshold(
        canal_verde_contrastado, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Guardar los archivos resultantes
    cv2.imwrite('resultado_canal_verde.jpg', g)
    cv2.imwrite('resultado_contraste.jpg', canal_verde_contrastado)
    cv2.imwrite('resultado_revelado.jpg', resultado_binary)

    print("¡Listo! Se guardó la imagen 'resultado_revelado.jpg'.")
