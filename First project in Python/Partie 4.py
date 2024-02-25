from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import numpy as np

####### Question 13. La fonction inverser(img) #######

def inverser(img):
    nb_lignes,nb_colonnes,_ = img.shape # get the dimensions of the numpy array
    image_sortie = np.copy(img) #get a copy of img
    # # on parcourt la matrice img
    for ligne in range(nb_lignes):
        for col in range(nb_colonnes):
                image_sortie[ligne,col] =255-image_sortie[ligne,col]
    Image.fromarray(img).save("image_entree.gif") # On sauvegarde les images pour pouvoir les afficher
    Image.fromarray(image_sortie).save("image_sortie.gif")

####### Question 14. La fonction flipH(img) #######

def flip(img):
    flip_img = img.transpose(method=Image.FLIP_LEFT_RIGHT) # la transposée de la matrice img
    flip_img.save("flip.gif")
    return flip_img

####### Question 15. La fonction poserV(img1,img2) #######

def poserV(img1,img2):
    array3=list(img1)+list(img2) # numpy array to list and concatenation
    AfficherImage(array3)

####### Question 16. La fonction poserH(img1,img2) #######

def poserH(img1,img2):
    img=[]
    for i in range(len(img1)):
        img.append(list(img1[i]+list(img2)[i]))
    return img