from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR/tessdata"'
image =Image.open('D:\learning\img/2.png')
# image=image.convert("L")
img_size=image.size
image.crop((50,50,300,300))
image.save("e.png")
print(img_size)


# code = pytesseract.image_to_string(image=image,config=tessdata_dir_config)
# print(code)