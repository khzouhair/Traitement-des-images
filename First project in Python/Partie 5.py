from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

####### Question 22. Donnez les valeurs des expressions suivantes #######
""">>>print(M[0][1][1])
….........
>>>print(M[1][0][1])
…........
>>>print(M[2][1][0])"""

def Exemple():
    n = 3
    m = 6
    M = [[[210, 100, 255], [100, 50, 255], [90, 90, 255], [90, 90, 255], [90, 90, 255], [90, 80, 255]],
         [[190, 255, 89], [201, 255, 29], [200, 255, 100], [100, 255, 90], [20, 255, 200], [100, 255, 80]],
         [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]]]
    plt.imshow(M)
    plt.axis("off")
    plt.show()
    print(M[0][1][1])

    print(M[1][0][1])

    print(M[2][1][0])

####### Question 24. La fonction def initImageRGB(imageRGB) #######

def initImageRGB(imageRGB):
    # On charge l'image et on la transforme en tableau contenant les couleurs
    image_entre = Image.open('chemin')
    image = np.asarray(image_entre)
    h, w, _ = image.shape
    image_sortie = np.copy(image)
    for ligne in range(h):
        for col in range(w):
            for i in range(3):
        # initialisation d'un tableau RGB aléatoire avec randrange
                image_sortie[ligne, col, i] = randrange(100)
    print(image_sortie)

####### Question 25. La fonction def symetrie(img) #######

def symetrieH(img):
    imgsym=img.copy() # get a copy of img
    # on parcourt la matrice imgsym
    for i in range(len(imgsym)):
        for j in range(len(imgsym[i])):
            for k in range(len(imgsym[i][j])):
                imgsym[i][j][k]=imgsym[-i][j][k] # symetrie par rapport a l'axe x
    return imgsym

def symetrieV(img):
    imgsym=img.copy()
    for i in range(len(imgsym)):
        for j in range(len(imgsym[i])//2):
            for k in range(len(imgsym[i][j])):
                imgsym[i][j][k], imgsym[i][-j][k]=imgsym[i][-j][k], imgsym[i][j][k] # symetrie par rapport a l'axe y
    return imgsym

####### Question 26. La fonction def grayscale(imageRGB) #######

def grayscale(imageRGB):
    return [[int(min(pix)+max(pix))/2 for pix in i ]for i in imageRGB] # partie entière du maximum et minimum de chaque pixel est la valeur du pixel en niveau de gris