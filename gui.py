import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

def selectImage():
    file = filedialog.askopenfilename(
        initialdir = os.getcwd(),
        title = "Select Image",
        filetype = (("JPG File","*.jpg"),("PNG File","*.png"),("All  Files","*.txt")))
    img = Image.open(file)
    img = ImageTk.PhotoImage(img)
    view.configure(image = img)
    view.image = img

def fixImage():
    pass


main =tk.Tk()
frame = tk.Frame(main)
main.title("Image Restoration")
main.geometry("450x450")
frame.pack(side=tk.BOTTOM,padx = 10, pady = 15)
view = tk.Label()
view.pack()

btn1 = tk.Button(frame, text = "Select Image to Restore", command=selectImage)
btn1.pack(side=tk.LEFT,padx=10)

restore = tk.Button(frame,text="Restore Image",command=fixImage)
restore.pack(side=tk.LEFT,padx=17)

main.mainloop()

