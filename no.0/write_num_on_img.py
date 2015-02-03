#!/usr/bin/python
#encoding=utf-8

from PIL import Image, ImageDraw, ImageFont

def write_num_on_img(filePath, num):
    img = Image.open(filePath)
    #img.size返回一个元组(width, height)
    size = img.size
    draw = ImageDraw.Draw(img)
    #colour设置数字的颜色，这里是红色
    colour = (255, 0, 0)
    ttfont = ImageFont.truetype('ahronbd.ttf', 50)
    #关键函数，参数包括，文字的位置，内容，颜色，字体
    draw.text((size[0]-30, 0), str(num), fill=colour, font=ttfont)
    #显示一幅已载入的图像
    img.show()
    img.save('changed.jpg')

if __name__ == '__main__':
    write_num_on_img("test.jpg", 4)
