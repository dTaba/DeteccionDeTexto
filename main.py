import cv2 as cv
import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = cv.imread('./index.png')
imgrgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

hImg, wImg, _ = img.shape
boxes = pyt.image_to_boxes(imgrgb)
print(boxes)

for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int((b[4]))
    cv.rectangle(imgrgb, (x, hImg - y), (w, hImg- h), (0,0,255), 3)
    cv.putText(imgrgb, b[0], (x, hImg- y +30), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

cv.imshow('Lorem Ipsum', imgrgb)

cv.waitKey(0)