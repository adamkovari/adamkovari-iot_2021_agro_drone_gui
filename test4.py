from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import cv2
import PIL
from PIL import ImageTk,Image
import time

def repa( image):
    label.configure(image=image)
    label.image = image
    return

style = Style()

window = style.master
window.geometry("400x400")
image = cv2.imread(r"C:\Users\Adam\Desktop\kep.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = PIL.Image.fromarray(image).resize((130,130))

sample_img = ImageTk.PhotoImage(PIL.Image.open("images/lights_01.png").resize((130,130)))

image = ImageTk.PhotoImage(image=image)
label = ttk.Label(window, text='python is great', style='Inverse.TLabel')
label.place(x=0,y=0,width=300,height=300)

tk.Button(window, text="ok", command=lambda: repa(image)).pack()

window.mainloop()