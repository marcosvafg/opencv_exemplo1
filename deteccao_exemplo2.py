# Importando a biblioteca
import cv2

# Criando o classificador
classificador = cv2.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

# Carregando a imagem, redimensionando e convertendo para cinza
imagem = cv2.imread('imagem_2.jpg')
imagem = cv2.resize(imagem, (1000, 600))
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detectar faces usando o classificador
faces_detectadas = classificador.detectMultiScale(imagem_cinza, scaleFactor=1.2)

# Quantas faces foram detectadas?
print(len(faces_detectadas))
print(faces_detectadas)

# Percorrer as faces detectadas
for (x, y, larg, alt) in faces_detectadas:
    cv2.rectangle(imagem, (x, y), (x + larg, y + alt), (255, 0, 255), 2)

# Exibindo a imagem
cv2.imshow(f'{len(faces_detectadas)} faces detectadas', imagem)
cv2.waitKey()
