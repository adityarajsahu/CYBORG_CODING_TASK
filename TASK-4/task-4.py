import cv2

img1 = cv2.imread('image-1.png')
img2 = cv2.imread('image-2.png')
img3 = cv2.imread('image-3.png')

grayscaled1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
retval1, threshold1 = cv2.threshold(grayscaled1,100,255,cv2.THRESH_BINARY)

contours1, hierarchy1 = cv2.findContours(threshold1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours in Image-1 = "+ str(len(contours1)))

cv2.drawContours(img1, contours1, -1, (255,255,255), 1)
#cv2.imshow('threshold-1',threshold1)
cv2.imshow('IMAGE-1',img1)



grayscaled2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled2,45,255,cv2.THRESH_BINARY)

contours2, hierarchy2 = cv2.findContours(threshold2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours in Image-2 = "+ str(len(contours2)))

cv2.drawContours(img2, contours2, -1, (255,255,255), 1)
#cv2.imshow('threshold-2',threshold2)
cv2.imshow('IMAGE-2',img2)



grayscaled3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
retval3, threshold3 = cv2.threshold(grayscaled3,30,255,cv2.THRESH_BINARY)

contours3, hierarchy3 = cv2.findContours(threshold3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours in Image-3 = "+ str(len(contours3)))

cv2.drawContours(img3, contours3, -1, (255,255,255), 1)
#cv2.imshow('threshold-3',threshold3)
cv2.imshow('IMAGE-3',img3)

cv2.waitKey(0)