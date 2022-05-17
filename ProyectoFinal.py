#Proyecto para colocar bordes a imagenes simples
import cv2 #Importar la libreria
 
img = cv2.imread('lil.jpg') #Leer la imagen que debe estar en la misma carpeta del archivo
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Para comvertir la imagen a una tonalidad gris
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #Convierte la imagen a una imagen binarisada
 
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #se usa para encontrar los bordes de la imagen
cv2.drawContours(img,contours,-1,(200,0,155),3) #Dibujar los contornos de la imagen 
 
cv2.imshow("img", img) #Muestra la imagen
cv2.waitKey(0)