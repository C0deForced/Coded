from PIL.Image import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\shoot\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import cv2
image = cv2.imread('test2.jpg')
text = pytesseract.image_to_string(image)
print(text)
