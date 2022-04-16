import cv2
import os

images = [image for image in os.listdir("data/Images") if image.endswith('.jpg')]
# print(images[0])
for i in range(len(images)):
	originalImage = cv2.imread(f"data/Images/{images[i]}")
	grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
	blurImage = cv2.blur(grayImage,(10,10))
	cv2.imwrite(f"data/train_data/{images[i]}",blurImage)



# from PIL import Image
# img = Image.open("image.jpg")
# img.convert("1").save("result.jpg")

# originalImage = cv2.imread("image.jpg")
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("blacknwhite.jpg",grayImage)
# blurImage = cv2.blur(grayImage,(10,10))
# cv2.imwrite("blurphoto.jpg",blurImage)

# cv2.imshow("sevage 9s",blurImage)
# cv2.waitKey(0)

#generating data
	#take photo and b/w it and blur it
#training

#1 denoising
#2 inpainting
#3 b/w 
#4 colorising 