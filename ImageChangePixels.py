from tkinter import filedialog
from PIL import Image
import tkinter as tk
import cv2,os,re


global Var0,Var1,Var2,Var3,Var4,Var22,Var33,Var44,NR,NG,NB,R,G,B,Logic

def find_file(*args):
    pathw = tk.Tk()
    pathw.withdraw()
    file_path = filedialog.askopenfilename(title = 'Open file', defaultextension='.png', filetypes = (('PNG file','*.png'),('JPG file','*.jpg'),('JPEG file','*.jpeg')))
    Var0.set(file_path)

def save_file(*args):
    global Var1
    pathw = tk.Tk()
    pathw.withdraw()
    file_path = filedialog.asksaveasfilename(title = 'Save file', defaultextension='.png', filetypes = (('PNG file','*.png'),('JPG file','*.jpg'),('JPEG file','*.jpeg')))
    Var1.set(file_path)

def Change_image(path_in,path_out,nr,ng,nb,r,g,b,logic):
    im = Image.open(path_in)
    pixels = im.load()
    width, height = im.size
    for i in range(0,width):
        for k in range(0,height):
            if(logic == "<"):
                if(pixels[i,k] < (int(r),int(g),int(b))):
                    pixels[i,k] = (int(nr),int(ng),int(nb))
                    pass
                pass
            if(logic == ">"):
                if(pixels[i,k] > (int(r),int(g),int(b))):
                    pixels[i,k] = (int(nr),int(ng),int(nb))
                    pass
                pass
            if(logic == "="):
                if(pixels[i,k] == (int(r),int(g),int(b))):
                    pixels[i,k] = (int(nr),int(ng),int(nb))
                    pass
                pass
            pass
    im.save(path_out)
    im.close()
    cv2.imshow("",cv2.imread(path_out))

def focusin2(*args):
    global Var2
    if(len(Var2.get()) > 0): Var2.set("")
    pass
def focusin3(*args):
    global Var3
    if(len(Var3.get()) > 0): Var3.set("")
    pass
def focusin4(*args):
    global Var4
    if(len(Var4.get()) > 0): Var4.set("")
    pass
def focusout2(*args):
    global Var2
    if(len(Var2.get()) < 3): Var2.set("R:"+Var2.get())
    pass
def focusout3(*args):
    global Var3
    if(len(Var3.get()) < 3): Var3.set("G:"+Var3.get())
    pass
def focusout4(*args):
    global Var4
    if(len(Var4.get()) < 3): Var4.set("B:"+Var4.get())
    pass

def focusin22(*args):
    global Var22
    if(len(Var22.get()) > 0): Var22.set("")
    pass
def focusin33(*args):
    global Var33
    if(len(Var33.get()) > 0): Var33.set("")
    pass
def focusin44(*args):
    global Var44
    if(len(Var44.get()) > 0): Var44.set("")
    pass
def focusout22(*args):
    global Var22
    if(len(Var22.get()) < 3): Var22.set("R:"+Var22.get())
    pass
def focusout33(*args):
    global Var33
    if(len(Var33.get()) < 3): Var33.set("G:"+Var33.get())
    pass
def focusout44(*args):
    global Var44
    if(len(Var44.get()) < 3): Var44.set("B:"+Var44.get())
    pass

def Change():
    global Var0,Var1,Var2,Var3,Var4,Var22,Var33,Var44,NR,NG,NB,R,G,B,Logic
    if(Var2.get()[0] != 'R'): Var2.set("R:"+Var2.get())
    if(Var3.get()[0] != 'G'): Var3.set("G:"+Var3.get())
    if(Var4.get()[0] != 'B'): Var4.set("B:"+Var4.get())
    if(Var22.get()[0] != 'R'): Var22.set("R:"+Var22.get())
    if(Var33.get()[0] != 'G'): Var33.set("G:"+Var33.get())
    if(Var44.get()[0] != 'B'): Var44.set("B:"+Var44.get())
    NR,NG,NB,R,G,B = Var2.get()[2:],Var3.get()[2:],Var4.get()[2:],Var22.get()[2:],Var33.get()[2:],Var44.get()[2:]
    L = Logic.get()
    try:
        Change_image(Var0.get(),Var1.get(),NR,NG,NB,R,G,B,L)
    except:
        pass
    
    

root = tk.Tk()
root.minsize(370,150)
root.maxsize(370,150)
root.title("BackgroundChange")
root.config(bg = "#273746")
root.iconbitmap("brush_icon.ico")

Var0 = tk.StringVar()
Var1 = tk.StringVar()
VarN = tk.StringVar()
Var2 = tk.StringVar()
Var3 = tk.StringVar()
Var4 = tk.StringVar()
Var22 = tk.StringVar()
Var33 = tk.StringVar()
Var44 = tk.StringVar()

Logic = tk.StringVar()
Option = ["<",">","="]

Var0.set("Input path")
Var1.set("Output path")
Var2.set("R:")
Var3.set("G:")
Var4.set("B:")
Var22.set("R:")
Var33.set("G:")
Var44.set("B:")

E0 = tk.Entry(root, textvariable = Var0, bg = "#d35400")
E1 = tk.Entry(root, textvariable = Var1, bg = "#d35400")
E2 = tk.Entry(root, textvariable = Var2,width=10, bg = "#b03a2e")
E3 = tk.Entry(root, textvariable = Var3,width=10, bg = "#196f3d")
E4 = tk.Entry(root, textvariable = Var4,width=10, bg = "#21618c")
E22 = tk.Entry(root, textvariable = Var22,width=10, bg = "#b03a2e")
E33 = tk.Entry(root, textvariable = Var33,width=10, bg = "#196f3d")
E44 = tk.Entry(root, textvariable = Var44,width=10, bg = "#21618c")
OpM = tk.OptionMenu(root, Logic, *Option)
OpM.config(bg ="#a04000", fg= "#FFFFFF", relief="flat",highlightbackground="#273746")
B0 = tk.Button(root, text = "Change", bg ="#a04000", command=Change)

E0.bind("<Button-1>", find_file)
E1.bind("<Button-1>", save_file)

E2.bind("<FocusIn>", focusin2)
E2.bind("<FocusOut>", focusout2)
E3.bind("<FocusIn>", focusin3)
E3.bind("<FocusOut>", focusout3)
E4.bind("<FocusIn>", focusin4)
E4.bind("<FocusOut>", focusout4)

E22.bind("<FocusIn>", focusin22)
E22.bind("<FocusOut>", focusout22)
E33.bind("<FocusIn>", focusin33)
E33.bind("<FocusOut>", focusout33)
E44.bind("<FocusIn>", focusin44)
E44.bind("<FocusOut>", focusout44)

E0.place(x=40,y=30)
E1.place(x=40,y=70)
E22.place(x=185,y=30)
E33.place(x=185,y=70)
E44.place(x=185,y=110)
E2.place(x=270,y=30)
E3.place(x=270,y=70)
E4.place(x=270,y=110)
OpM.place(x=120,y=107)
B0.place(x=40,y=110)

root.mainloop()


