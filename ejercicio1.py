import cv2 #leer libreria
from cv2 import imshow #Leer el metodo imshow
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

#Lectura de imagen
img= cv2.imread('lil.jpg',0) #Aqui se usa el metodo imread para leer la imagen que vamos a cargar, en este caso cargamos la imagen lil 
imshow('Imagen Original',img) #Usamos el metodo imshow para mostrar una ventana donde le pasamos dos parametros que seria la imagen leida y un nombre


cv2.waitKey(0) #Cronometro creado en milisegundos en este sentido es para esperar una tecla
cv2.destroyAllWindows() #Destruir la ventana 