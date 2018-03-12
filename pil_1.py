#coding=utf8
from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR/tessdata"'
text=pytesseract.image_to_string(Image.open('dufu.jpg'),lang='chi_sim',config=tessdata_dir_config)
print(text)