import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

class Restore:
    def __init__(self, view):
        self.view = view
        self.filepath = None

    def selectImage(self):
        file = filedialog.askopenfilename(
            initialdir = os.getcwd(),
            title = "Select Image",
            filetype = (("JPG File","*.jpg"),("PNG File","*.png"),("All  Files","*.txt")))
        img = Image.open(file)
        img = ImageTk.PhotoImage(img)
        self.view.configure(image = img)
        self.view.image = img
        self.filepath = file

    def fixImage(self):
        pass


main =tk.Tk()
frame = tk.Frame(main)
main.title("Image Restoration")
main.geometry("450x450")
frame.pack(side=tk.BOTTOM,padx = 10, pady = 15)
view = tk.Label()
view.pack()
obj = Restore(view)
btn1 = tk.Button(frame, text = "Select Image to Restore", command=obj.selectImage)
btn1.pack(side=tk.LEFT,padx=10)

restore = tk.Button(frame,text="Restore Image",command=obj.fixImage)
restore.pack(side=tk.LEFT,padx=17)

main.mainloop()

