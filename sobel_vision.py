import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    imagen = cv2.imread("imagenes/road_sample.jpg")

    if imagen is None:
        print("Error: No se pudo cargar la imagen")
        return

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    suavizada = cv2.GaussianBlur(gris, (5, 5), 0)

    sobel_x = cv2.Sobel(suavizada, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(suavizada, cv2.CV_64F, 0, 1, ksize=3)

    magnitud = np.sqrt(sobel_x**2 + sobel_y**2)
    magnitud = np.uint8(255 * magnitud / np.max(magnitud))

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.title("Imagen Original")
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.title("Escala de Grises")
    plt.imshow(gris, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.title("Sobel Horizontal")
    plt.imshow(np.abs(sobel_x), cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.title("Sobel Vertical")
    plt.imshow(np.abs(sobel_y), cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.title("Magnitud del Gradiente")
    plt.imshow(magnitud, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
