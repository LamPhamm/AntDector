import cv2

img1 = cv2.resize(cv2.imread('assets/ants1.jpg',0),(0,0),fx=0.3,fy=0.3)
img2 = cv2.resize(cv2.imread('assets/ants2.jpeg',0),(0,0),fx=0.3,fy=0.3)

#Display image
cv2.imshow('Image 1',img1)
cv2.imshow('Image 2',img2)
cv2.waitKey(0) #Wait infinite amount of time
cv2.destroyAllWindows() #Press any key, or x button to close