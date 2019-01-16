#Author guo
import tesserocr
from PIL import Image
#图形二维码识别
image=Image.open('CheckCode.jpg')
image=image.convert('L')#图片转化为灰度图
threshold=128#二值化阈值
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')#转换为点值图
result=tesserocr.image_to_text(image)#识别过程OCR
print(result)