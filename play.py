from tkinter import *
from PNGcreater import create_PNG
import title


def main(len, PixelSize):
    #１Pixelのサイズ
    #PixelSize = 10
    #縦横のPixel数
    #len = 16
    #カラーテーブル
    color_table=[]
    button= []

    color_code = "#000000"
    def RGB_convert(i):
        return(hex(i))
        
    def clicked(event):
        #print('クリックしました')
        global color_code
        #global var
        event.widget.config(bg=color_code)
        print(event.widget['fg']+"852")
        print(777)
        """
        if var.get():
            event.widget.config(bg=color_code)
        """
            

    def print_b():
        global hoge_table
        color_table.clear()
        for i in button:
            color_table.append((         
            int(i["bg"][1:3],16),
            int(i["bg"][3:5],16),
            int(i["bg"][5:7],16),
            int(255)
            )
            )
            
        #print(color_table)
        
        #len, PixelSize, Pixel_table
        create_PNG(len, PixelSize, color_table)
 
               
    
    def back_b():
        root.destroy()   
        title.main()
        
    def slider_scroll(i):
        global color_code
        
        color_code="#"
        for j in RGB:
            pass
            #color_code+=str(RGB_convert(j.get()))[2:].rjust(2,'0')
            
        #print(color_code)
        frame2.config(bg=color_code)
        #print(color_code)


    ccode = "#000000"
    root = Tk() # この下に画面構成を記述
    
    # ----------- ①Window作成 ----------- #
    root.title('PINGcreater')   # 画面タイトル設定
    #root.geometry('500x500')       # 画面サイズ設定
    root.attributes('-fullscreen', True)
    root.resizable(False, False)   # リサイズ不可に設定
 
 
    # ----------- ②Frameを定義 ----------- #
    frame1 = Frame(root, width=600, height=600, borderwidth=2, relief='solid')
    frame2 = Frame(root, width=300, height=300, borderwidth=1, relief='solid', bg='#000000')
    printbutton = Button(root, width=38, height=8, borderwidth=1,text="画像作成",command=print_b, bg='#BBBBBB')
    backbutton = Button(root, width=38, height=8, borderwidth=1,text="タイトルへ戻る",command=back_b, bg='#BBBBBB')
    
    # Frameサイズを固定
    frame1.propagate(False)

    # Frameを配置（grid）
    frame1.place(x = 110, y = 140)
    frame2.place(x = 800, y = 140)
    printbutton.place(x = 1130, y = 140)
    backbutton.place(x = 1130, y = 300)
 
    # ---------- ③Widget配置  ----------- #
    # label(フレーム1左上)

    RGB = []
    pixel_size = int(600/len)
    high = 0
    for i in range(len):
        for j in range(len):
            button.append(Button(frame1,width=pixel_size, height=pixel_size,command=clicked,bg='#ffffff'))
            button[(i*len)+j].place(x = j*pixel_size,  y = i*pixel_size)
            button[(i*len)+j].bind("<ButtonPress>", clicked)
        high += 145

    for i in range(3):    
        RGB.append(Scale(root,
                    command = slider_scroll,
                    orient=HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 600,           # 全体の長さ
                    width = 30,             # 全体の太さ
                    sliderlength = 30,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 255,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=32,         # 目盛りの分解能(初期値0で表示なし)
                    #variable=slider_scroll,
                           ))
        RGB[i].place(x = 800, y = 470+i*100)                                        
 
    var = BooleanVar()
    che = Checkbutton( text = '透明ピクセル', variable = var )
    che.place( x = 1000, y = 800 )

    root.mainloop()
    
if __name__ == '__main__':
    main(3,3)

