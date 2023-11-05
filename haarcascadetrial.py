import pytesseract
import numpy as np
import csv
from datetime import datetime

# check for path of tesseract.exe file your system

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2

img = cv2.imread('dataset/numberplate3.jpg')
#
######################################################################################################
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #RGB che color grey madhe convert hote
x=1

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
gray=blurred

# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# gray = clahe.apply(gray)


thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# kernel = np.ones((5, 5), np.uint8)
# dilated_image = cv2.dilate(thresh, kernel,1)

# gray = cv2.convertScaleAbs(dilated_image,2,0)

#threshold value fix hote
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

#contours, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# read haarcascade for number plate detection
cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# Detect license number plates
plates = cascade.detectMultiScale(gray, 1.2, 5)
print('Number of detected license plates:', len(plates))

# loop over all plates
for (x,y,w,h) in plates:
   #
   # draw bounding rectangle around the license number plate
   cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
   gray_plates = gray[y:y+h, x:x+w]
   color_plates = img[y:y+h, x:x+w]
   #grey_plate variable me cut ki hui plate stored hhai

# Apply OCR to recognize the characters in the license plate
text = pytesseract.image_to_string(gray_plates, config='--psm 10', lang='hin+eng')
import re
pattern= re.compile(r'^[A-Z]{3}\d{3}$')
print("licence plate: ", text)
# Display results
cv2.imshow('Original Image', img)
cv2.imshow('Extracted License Plate', gray_plates)
#####################################################################################################3
#cv2.imshow('sample image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#text=pytesseract.image_to_string(img)
print(text)

now =datetime.now()
current_date= now.strftime("%Y-%m-%d")

#csvwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
f= open(current_date+ '.csv','w+', newline='')
lnwrite = csv.writer(f)

current_time = now.strftime("%H-%M")
lnwrite.writerow([text, current_time])
f.close()


