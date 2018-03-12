from PIL import Image
im = Image.open("D:\OPPOfind7\img/壁纸2.jpg")
#查看图片的宽和高
img_size = im.size
print(img_size)


'''
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
'''
# 截取图片中一块宽和高都是200的
x=100
y=100
w=200
h=200
region = im.crop((x,y,x+w,y+h))
region.save("f.jpg")

# 截取图片中一块宽和高都是100的
x=100
y=100
w=100
h=100
region = im.crop((x,y,x+w,y+h))
region.save("g.jpg")

# 把图片平均分成4块
# 第1块
w = img_size[0] / 2.0
h = img_size[1] / 2.0
x = 0
y = 0
region = im.crop((x, y, x + w, y + h))
region.save("./crop_average-1.jpg")

# 第2块
x = w
y = h
region = im.crop((x, y, x + w, y + h))
region.save("./crop_average-2.jpg")

# 第3块
x = 0
y = h
region = im.crop((x, y, x + w, y + h))
region.save("./crop_average-3.jpg")

# 第4块
x = w
y = 0
region = im.crop((x, y, x + w, y + h))
region.save("./crop_average-4.jpg")

#进行图片的左旋转45操作
img_rotate=im.rotate(45)
img_rotate.save('./rotate-l45.jpg')
#在上面旋转图的基础上右旋转30度
img_rotate1=img_rotate.rotate(-30)
img_rotate1.save("./rotate-r30.jpg")