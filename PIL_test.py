from PIL import Image
import time

# 画像データを生成
size = (40, 40)
Pixel_table = [(255, 255, 255,   0),(255,   0,   0, 255),(255, 255, 255, 255),(255, 255, 255, 255),
               (255, 255, 255,   0),(255, 255, 255,   0),(255, 255, 255,   0),(255, 255, 255, 255),
               (255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),
               (255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),
               ]

img = Image.new("RGBA",size,  (255, 255, 255, 255))
#img.putpixel((10, 10), (255, 0, 0, 255))
for i in range(4):
    for j in range(4):
        #img.putpixel((j, i), Pixel_table[i*4+j])
        for k in range(i*10,i*10+10):
            for l in range(j*10,j*10+10):
                img.putpixel((l, k), Pixel_table[i*4+j])
img.save("image/"+str(int(time.time()))+".png", quality=95)