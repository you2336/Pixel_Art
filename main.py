import bmp_Creater as BC
import bmp_to_png as btp

from tkinter import *
import datetime

if __name__ == '__main__':

    c_table = []
    button= []
    color_code = "#000000"
    def RGB_convert(i):
        return(hex(i))
        
    def clicked(event):
        print('クリックしました')
        event.widget.config(bg=color_code)

    def print_b():
        c_table.clear()
        pixels=[0x12, 0x13, 0x14, 0x15,
                0x08, 0x09, 0x10, 0x11,
                0x04, 0x05, 0x06, 0x07,
                0x00, 0x01, 0x02, 0x03,]

        for i in range(4):
            for j in range(4):
                today = datetime.datetime.utcnow().date()
                #c_table.append((button[i*4+j].cget('background')))
                
                c_table.append(int(button[i*4+j].cget('background')[1:3],16))
                c_table.append(int(button[i*4+j].cget('background')[3:5],16))
                c_table.append(int(button[i*4+j].cget('background')[5:7],16))
                c_table.append(0)
                

        for i in range(4):
            for j in range(4):
                print(str(i*4+j).rjust(2),end='  ')
                for k in range(4):
                    print(str(c_table[i*4**2+j*4+k]).rjust(3),end=" ")
                #print("",end=": ")
            print('')
        BC.writeBmp("images/bmp/"+str(today)+'.bmp', 4, 4, c_table, pixels)
        
        btp.btp()
        #print(c_table[0:4],c_table[4:8],c_table[8:12],c_table[12:16],)
        
        
    def slider_scroll(i):
        global color_code
        
        color_code="#"
        for j in RGB:
            pass
            color_code+=str(RGB_convert(j.get()))[2:].rjust(2,'0')
            
        #print(color_code)
        frame2.config(bg=color_code)

    ccode = "#000000"
    root = Tk() # この下に画面構成を記述
    
    # ----------- ①Window作成 ----------- #
    root.title('tkinterの使い方')   # 画面タイトル設定
    #root.geometry('500x500')       # 画面サイズ設定
    root.attributes('-fullscreen', True)
    root.resizable(False, False)   # リサイズ不可に設定
 
 
    # ----------- ②Frameを定義 ----------- #
    frame1 = Frame(root, width=600, height=600, borderwidth=2, relief='solid')
    frame2 = Frame(root, width=300, height=300, borderwidth=1, relief='solid', bg='#000000')
    print_b = Button(root, width=38, height=8, borderwidth=1,text="PRINT",command=print_b)
    
    # Frameサイズを固定
    frame1.propagate(False)

 
    # Frameを配置（grid）
    frame1.place(x = 110, y = 140)
    frame2.place(x = 800, y = 140)
    print_b.place(x = 1130, y = 140)

 
 
    # ---------- ③Widget配置  ----------- #
    # label(フレーム1左上)

    RGB = []
    high=0
    for i in range(4):
        for j in range(4):
            button.append(Button(frame1,width=20, height=10,command=clicked,bg='#ffffff'))
            button[(i*4)+j].place(x = j*149,  y = high)
            button[(i*4)+j].bind("<ButtonPress>", clicked)
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

 
 
    root.mainloop()


