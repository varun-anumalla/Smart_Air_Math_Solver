import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\91984\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

img = cv2.imread("processed.png")

text = pytesseract.image_to_string(img)

print(repr(text))