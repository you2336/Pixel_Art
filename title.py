from tkinter import *
from tkinter import ttk
import play


def main():
    #１Pixelのサイズ
    PixelSize = 1
    #縦横のPixel数
    len = 16
    #カラーテーブル
    color_table=[]
    
    button= []
    color_code = "#000000"
    def RGB_convert(i):
        return(hex(i))
    
    def play_b():
        root.destroy() 
        play.main(len, PixelSize)  
        
    def close_b():
        root.destroy()   

            
        #print(color_code)
        #frame2.config(bg=color_code)

    ccode = "#000000"
    root = Tk() # この下に画面構成を記述
    
    # ----------- ①Window作成 ----------- #
    root.title('PINGcreater')   # 画面タイトル設定
    #root.geometry('500x500')       # 画面サイズ設定
    root.attributes('-fullscreen', True)
    root.resizable(False, False)   # リサイズ不可に設定
 
 
    # ----------- ②Frameを定義 ----------- #
    title = Label(text="PixelArt Creater")
    playbutton = Button(root, width=38, height=8, borderwidth=1,text="作成開始",command=play_b, bg='#BBBBBB')
    closebutton = Button(root, width=38, height=8, borderwidth=1,text="終了",command=close_b, bg='#BBBBBB')
    list_name = Label(root, text="ひとつピクセルの細かさ")
    pixelSize_label = Label(root, text="ひとつピクセルの大きさ")
    
    pixelsubtlety_list = [2,4,6,8,10,12,14,16]  #初期値
    pixelsubtlety = ttk.Combobox(
    master=root,
    values= pixelsubtlety_list,                   #設定
    )
    pixelsize_list = [2,4,6,8,10,12,14,16]  #初期値
    pixelsize_ = ttk.Combobox(
    master=root,
    values=pixelsize_list,                   #設定
    )
    
    
    # Frameサイズを固定
    #frame1.propagate(False)

    # Frameを配置（grid）
    title.pack()
    playbutton.pack()
    closebutton.pack()
    list_name.pack()   
    #Comboboxを表示
    pixelsubtlety.pack()
    pixelSize_label.pack()
    pixelsize_.pack()

                                    
 
    root.mainloop()


if __name__ == '__main__':
    main()