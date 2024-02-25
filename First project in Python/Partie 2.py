import numpy as np
from matplotlib import pyplot as plt

####### Question 4. Créer une image noir #######

def image_noire(h, l):
    img = np.zeros((h,l), dtype = np.uint8)# creates a numpy array of zeros
    #uint8: datatype is 8-bit unsigned integer (0 to 255)
    return img

####### Question 5. Créer une image blanche #######

def image_blanc(h, l):
    img = np.ones((h,l), dtype = np.uint8)# creates a numpy array of zeros
    #uint8: datatype is 8-bit unsigned integer (0 to 255)
    return img

####### Question 6. Créer une image noir et blanc #######

def creerImgBlancNoir(h,l):
    M=[[0]*l for i in range(h)] # creates a numpy array of zeros
    for i in range(h): 
        for j in range(l): 
            M[i][j]=(i+j)%2 # each pixel of the image is equal to i+j modulo 2
    return M

####### Question 7. Négatif #######

def negatif(img):
    # on parcourt la matrice img
    for i in range(len(img)):
        for j in range(len(img[0])):
    # inversion des valeurs de la matrice img (0 devient 1 et 1 devient 0)        
            if (img[i][j]==1): 
                img[i][j]=0
            else:
                img[i][j]=1
    return img