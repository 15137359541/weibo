from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR/tessdata"'

#二值图处理
def binarizing(img,threshold):
    pixdata=img.load()
    print(pixdata)
    #加载的图片宽和高
    w,h=img.size
    print (w,h)
    for y in range(h):
        for x in range(w):
            # print(pixdata[x,y])
            if pixdata[x,y]<threshold:
                pixdata[x,y]=0
            else:
                pixdata[x,y]=255
    return img
###########去除干扰线算法
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            # print(pixdata[x, y - 1])
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img


if __name__=="__main__":
    img=Image.open('D:\learning\img\验证码/6.jpg')
    #原图片展示
    # img.show()
    #保存图片
    # img.save("new_3.png")
    # 必须转化为灰度图，否则，后面会报错TypeError: '<' not supported between instances of 'tuple' and 'int'
    img_grey=img.convert('L')
    # img_grey.show()
    #保存图片
    # img_grey.save("new_3_grey.png")
    #调用函数，以190像素为界限
    new_img=binarizing(img_grey,190)
    new_img.save("c.jpg")

    new_img1=depoint(new_img)
    new_img1.save("d.jpg")

    #识别图片
    code=pytesseract.image_to_string(new_img1,config=tessdata_dir_config)
    print(code)