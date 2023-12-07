from PIL import Image
import time

def create_PNG(len, PixelSize, Pixel_table):
    #１Pixelのサイズ
    #PixelSize = 10
    #縦横のPixel数
    #len = 100
    # 画像データを生成
    size = (len*PixelSize, len*PixelSize)
    """
    Pixel_table = [(255, 255, 255,   0),(255,   0,   0, 255),(255, 255, 255, 255),(255, 255, 255, 255),
                (255, 255, 255,   0),(255, 255, 255,   0),(255, 255, 255,   0),(255, 255, 255, 255),
                (255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),
                (255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),(255, 255, 255, 255),
                ]
    """

    #白紙の画像を作成、後で編集
    img = Image.new("RGBA",size,  (255, 255, 255, 255))
    #img.putpixel((10, 10), (255, 0, 0, 255))
    #対応するPixelに塗り替える
    for i in range(len):
        for j in range(len):
            #img.putpixel((j, i), Pixel_table[i*4+j])
            for k in range(i*PixelSize,i*PixelSize+PixelSize):
                for l in range(j*PixelSize,j*PixelSize+PixelSize):
                    img.putpixel((l, k), Pixel_table[i*len+j])
    #保存
    img.save("image/"+str(int(time.time()))+".png", quality=95)