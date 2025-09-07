import cv2
img= cv2.imread("C:\\Users\\reddi\\OneDrive\\Desktop\\iva lab\\dog.jpg")
cv2.namedWindow('sample Image',cv2.WINDOW_NORMAL)
cv2.imshow('sample Image',img)
cv2.waitKey(0)
cv2.imwrite("output.image.jpg",img)
print("image saved successfully")
cv2.destroyAllWindows( ṃ̇)