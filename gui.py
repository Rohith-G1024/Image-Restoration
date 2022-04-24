import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from load_model import Denoise

class Restore:
    def __init__(self, view,size):
        self.view = view
        self.filepath = None
        self.size = ((size[0]-50), abs(size[1]-50))
        self.model = Denoise()

    def selectImage(self):
        file = filedialog.askopenfilename(
            initialdir = "Cifar10 data",
            title = "Select Image",
            filetype = (("JPG File","*.jpg"),("PNG File","*.png"),("All  Files","*.txt")))
        self.displayImage(file)

    
    def displayImage(self,file):
        img = Image.open(file)
        if img.size != (32,32):
            print("changed")
            img = img.resize((32,32))
            img.save(file)
            img = Image.open(file)
        img = img.resize(self.size)
        img = ImageTk.PhotoImage(img)
        self.view.configure(image = img)
        self.view.image = img
        self.filepath = file

    def denoise(self):
        self.model.deNoise(self.filepath)
        self.displayImage("restored.jpg")

    def colorize(self):
        pass


main =tk.Tk()
frame = tk.Frame(main)
main.title("Image Restoration")
size = (400,300)
main.geometry(f"{size[0]}x{size[1]}")
frame.pack(side=tk.BOTTOM,padx = 10, pady = 15)
view = tk.Label()
view.pack()
obj = Restore(view,size)
btn1 = tk.Button(frame, text = "Select Image", command=obj.selectImage)
btn1.pack(side=tk.LEFT,padx=10)

colorize = tk.Button(frame, text = "Colorize Image", command = obj.colorize)
colorize.pack(side=tk.LEFT,padx=10)

restore = tk.Button(frame,text="Restore Image",command=obj.denoise)
restore.pack(side=tk.LEFT,padx=10)

main.mainloop()

