import pytesseract

# check for path of tesseract.exe file your system

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2

img = cv2.imread('vehicle.jpg')
######################################################################################################
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x=1
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

contours, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Find the contour with the largest area, which is likely the license plate
max_area = 0
best_cnt = None
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > max_area:
        max_area = area
        best_cnt = cnt

# Draw a bounding box around the license plate
x,y,w,h = cv2.boundingRect(best_cnt)
plate = img[y:y+h,x:x+w]
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# Apply OCR to recognize the characters in the license plate
text = pytesseract.image_to_string(plate)
# Display results
cv2.imshow('Original Image', img)
cv2.imshow('License Plate', plate)
#####################################################################################################3
#cv2.imshow('sample image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#text=pytesseract.image_to_string(img)
print(text)


