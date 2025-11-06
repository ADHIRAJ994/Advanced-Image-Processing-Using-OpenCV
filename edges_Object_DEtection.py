import cv2 as cv

img = cv.imread('lena.jpg',1)
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# ret,thresh = cv.threshold(imgGray,127,255,0)
edges = cv.Canny(imgGray,100,200) # Used for edge detection
countors,hierachy = cv.findContours(edges,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
# contours means outline of any object in the image which is useful for detecting objects in an image.

#print("Number of countors = "+ str(len(countors)))
cv.drawContours(img,countors,-1,(0,255,0),3)
cv.imshow('Image',img)
#cv.imshow('THresh_Image',thresh)

cv.waitKey()
cv.destroyAllWindows()