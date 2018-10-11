# Imporrtando a biblioteca
import cv2

# Criando um classificador usando haarcascade
classificador = cv2.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

# Carregar a imagem e converter para cinza
imagem = cv2.imread('imagem_1.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detectar faces usando o classificador
faces_detectadas = classificador.detectMultiScale(imagem_cinza)

# Quantas faces foram detectadas?
print(len(faces_detectadas))
print(faces_detectadas)

# Percorrer as faces detectadas
for (x, y, larg, alt) in faces_detectadas:
    cv2.rectangle(imagem, (x, y), (x + larg, y + alt), (255, 0, 255), 2)

# Exibir a imagem
cv2.imshow('Imagem', imagem)
cv2.waitKey()
