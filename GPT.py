from PIL import Image
import numpy as np

# 新しい画像を作成（RGBA モードを使用）
width, height = 100, 100
image = Image.new("RGBA", (width, height))

# ビット単位で画像を生成
for y in range(height):
    for x in range(width):
        # ランダムなRGB値とアルファ値（透明度）を生成
        red = np.random.randint(0, 256)
        green = np.random.randint(0, 256)
        blue = np.random.randint(0, 256)
        alpha = np.random.randint(0, 256)

        # ピクセルの色と透明度を設定
        image.putpixel((x, y), (red, green, blue, alpha))

# 画像を保存
image.save("output.png")