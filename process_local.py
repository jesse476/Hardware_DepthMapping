
#ECE196 Depth Mapping Project
#Author: Will Chen
#Prerequisite: You need to install OpenCV before running this code
#The code here is an example of what you can write to print out 'Hello World!'
#Now modify this code to process a local image and do the following:
#1. Read geisel.jpg
#2. Convert color to gray scale
#3. Resize to half of its original dimensions
#4. Draw a box at the center the image with size 100x100
#5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
#All the above steps should be in one function called process_image()

# TODO: Import OpenCV
import cv2

# TODO: Edit this function
def process_image():
	img=cv2.imread("image.jpg",0);
	cv2.imshow('Original Image',img)
	cv2.waitKey(0)
	newimg=cv2.resize(img, (0,0), fx=0.5, fy=0.5)
	cv2.imshow('Resized Image',newimg)
	cv2.waitKey(0)
	moment=cv2.moments(newimg)
	x=int(moment ["m10"]/moment["m00"])
	y=int(moment ["m01"]/moment["m00"])
	cv2.rectangle(newimg, (x-50,y-50), (x+50,y+50), (255, 255, 255),3)
	cv2.imshow('Square at center',newimg)
	cv2.waitKey(0)
	return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return
    
# TODO: Call process_image function.
def main():
    #hello_world()
    process_image()
    return

if(__name__ == '__main__'):
    main()