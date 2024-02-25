from matplotlib import pyplot as plt

####### Question 9. La luminance #######

def luminance(img):
    s=0 
    # on parcourt la matrice img
    for i in range(len(img)):
        for j in range(len(img[0])):
            s+=img[i][j] # la somme de tous les valeurs de la matrice img
    return s/(len(img)*len(img[0])) # la moyenne de tous les pixels de l’image

####### Question 10. La fonction d'entête def constrast(Img) #######

def contrast(img):
    t=0 # initialiser le contrast par la valeur 0
    # on parcourt la matrice img
    for i in range(len(img)):
        for j in range(len(img[0])):
            t+=(1/(len(img)*len(img[0])))*((img[i][j]-luminance(img)^2)) # calculer le contrast de l'image
    return t

####### Question 11. def profondeur(Img)  #######

def profondeur(img):
    max=img[0][0] # initialize the variable max with the value of the element in the 1st ligne and column
    # on parcourt de la matrice img
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (max<img[i][j]).all:
                max=img[i][j]
    return max

####### Question 12. def Ouvrir(Img) #######

def ouvrirImage(chemin):
    img=plt.imread(chemin)
    return img