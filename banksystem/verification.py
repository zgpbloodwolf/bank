# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, \
            ImageFilter
import random
class Verification():
    def __init__(self):
        self.verification_code=''
    def verif(self):
        # 画面的背景色
        imgbackgroundc = (255, 255, 255)
        width = 110
        height = 30
        # 创建一张图片
        img = Image.new("RGB", (width, height),
                        imgbackgroundc)
        draw = ImageDraw.Draw(img)
        for i in range(0, 100):
            xy = (random.randrange(0, width),
                  random.randrange(0, height))
            fill = (random.randrange(0, 255),
                    random.randrange(0, 255),
                    random.randrange(0, 255))
            draw.point(xy, fill=fill)
        str = '123456789QWERTYUIPASDFGHJKLZXCVBNMqwertyuipasdfghjklzxcvbnm'
        rand_str = ''
        for i in range(0, 4):
            rand_str += random.choice(str)
        font = ImageFont.truetype('simsun.ttc', 20)
        self.verification_code = rand_str
        fontcolor0 = (
        random.randrange(0, 255), random.randrange(0, 255),
        random.randrange(0, 255))
        fontcolor1 = (
        random.randrange(0, 255), random.randrange(0, 255),
        random.randrange(0, 255))
        fontcolor2 = (
        random.randrange(0, 255), random.randrange(0, 255),
        random.randrange(0, 255))
        fontcolor3 = (
        random.randrange(0, 255), random.randrange(0, 255),
        random.randrange(0, 255))
        draw.text((5, 2), rand_str[0], font=font,
                  fill=fontcolor0)
        draw.text((25, 2), rand_str[1], font=font,
                  fill=fontcolor1)
        draw.text((50, 2), rand_str[2], font=font,
                  fill=fontcolor2)
        draw.text((75, 2), rand_str[3], font=font,
                  fill=fontcolor3)
        del draw
        params = [
            1 - float(random.randint(1, 2)) / 100,
            0,
            0,
            0,
            1 - float(random.randint(1, 10)) / 100,
            float(random.randint(1, 2)) / 500,
            0.001,
            float(random.randint(1, 2)) / 500
        ]
        img = img.transform((width, height),
                            Image.PERSPECTIVE, params)
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        img.save("a.png", "PNG")
        return img