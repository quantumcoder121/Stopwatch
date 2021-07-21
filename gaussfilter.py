import cv2 as cv

print(" ")
print("Gaussian Filter")
inputfile = str(input("Enter input filename or path: "))
img1 = cv.imread(inputfile)

img1gaussfilter = cv.GaussianBlur(img1, (5, 5), 0)
outputfile = str(input("Enter output filename or path: "))
cv.imwrite(outputfile, img1gaussfilter)

cv.imshow("Gaussian Filter applied on " + inputfile, img1gaussfilter)
cv.imshow("Original image: " + inputfile, img1)

cv.waitKey(0)
cv.destroyAllWindows()
