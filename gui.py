import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

class Restore:
    def __init__(self, view,size):
        self.view = view
        self.filepath = None
        self.size = ((size[0]-50), abs(size[1]-50))

    def selectImage(self):
        file = filedialog.askopenfilename(
            initialdir = os.getcwd(),
            title = "Select Image",
            filetype = (("JPG File","*.jpg"),("PNG File","*.png"),("All  Files","*.txt")))
        img = Image.open(file)
        img = img.resize(self.size)
        img = ImageTk.PhotoImage(img)
        self.view.configure(image = img)
        self.view.image = img
        self.filepath = file

    def fixImage(self):
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
btn1 = tk.Button(frame, text = "Select Image to Restore", command=obj.selectImage)
btn1.pack(side=tk.LEFT,padx=10)

restore = tk.Button(frame,text="Restore Image",command=obj.fixImage)
restore.pack(side=tk.LEFT,padx=17)

main.mainloop()

