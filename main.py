import cv2 as cv
import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = cv.imread('./prueba.png')
imgrgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

hImg, wImg, _ = img.shape
boxes = pyt.image_to_boxes(imgrgb) 

for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int((b[4]))
    cv.rectangle(imgrgb, (x, hImg - y), (w, hImg- h), (0,0,255), 1)

cv.imshow('Lorem Ipsum', imgrgb)

cv.waitKey(0)