# Importando a biblioteca
import cv2

# Criar os classificadores
classificador_faces = cv2.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
classificador_olhos = cv2.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_eye.xml')

# Carregando a imagem e convertendo para cinza
imagem = cv2.imread('angelina-jolie.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detectar faces usando o classificador
faces_detectadas = classificador_faces.detectMultiScale(imagem_cinza)

# Percorrer as faces detectadas
for (x, y, larg, alt) in faces_detectadas:
    cv2.rectangle(imagem, (x, y), (x + larg, y + alt), (255, 0, 255), 2)
    # Selecionar uma regiao da imagem
    regiao = imagem[y:y + alt, x:x + larg]
    # Converter para cinza
    regiao_cinza = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
    # Rodar o classificador
    olhos_detectados = classificador_olhos.detectMultiScale(regiao_cinza, minSize=(80, 80))
    # Percorrer a lista de olhos detectados
    for (ox, oy, olarg, oalt) in olhos_detectados:
        cv2.rectangle(regiao, (ox, oy), (ox + olarg, oy + oalt), (0, 255, 0), 2)

# Exibir a imagem
cv2.imshow('Imagem', imagem)
cv2.waitKey()
