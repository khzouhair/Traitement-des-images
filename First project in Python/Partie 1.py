from matplotlib import pyplot as plt

####### Question1. La fonction AfficherImg(Img) #######

def AfficherImage(img):
    plt.axis("off") # to remove x and y axis
    plt.imshow(img, interpolation='nearest')# creates an image from a 2-dimensional numpy array
    # Interpolation is a method for generating points between given points
    # determines the “nearest” neighbouring pixel, and assumes the intensity value of it
    plt.imshow(img, cmap = "gray") # 
    plt.show()# opens one or more interactive windows that display your figure

####### Question2. La fonction ouvrirImage(Img) #######

def ouvrirImage(chemin):
    img=plt.imread(chemin) # converts an image to a numpy array
    return img

####### Question3. La fonction saveImage(Img) #######

def saveImage(img):
    plt.imsave("image.jpg",img)# to save the image