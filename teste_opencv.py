# Importando a bilioteca
import cv2

# Verificando a versao do OpenCV
print(cv2.__version__)

# Carregando a primeira imagem
imagem = cv2.imread('angelina-jolie.jpg')
# Mostrando a imagem original
cv2.imshow('Original', imagem)

# Transformar a imagem em tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# Mostrar a imagem cinza
cv2.imshow('Cinza', imagem_cinza)

# Esperar uma tecla para fechar
cv2.waitKey()
