import os

images = [image for image in os.listdir() if image.endswith('.jpg')]
for i in range(len(images)):

    os.rename(images[i],str(i)+".jpg")