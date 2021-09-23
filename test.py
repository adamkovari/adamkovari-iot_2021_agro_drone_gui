import tkinter as tk
from tkinter import ttk
import threading
import PIL


def kep_betoltes(row,col,img,image_frame,sample_image_label_list):
    x = 150
    y = 50
    #print(row,col)
    sample_image_label_list[row][col].place_forget()
    label = ttk.Label(image_frame, image=img)
    label.place(x=x+col*110, y=y+row*110, width=110, height=110)
    return



def input(entry, event_obj):
    event_obj.wait()

    return entry.get()


def infiniti(entry, image_frame, sample_image_lable_list, event_obj):
    while True:
        inp = input(entry, event_obj)
        entry.delete(0, tk.END)
        event_obj.clear()
        if inp == "repa":
            sample_img = PIL.ImageTk.PhotoImage(PIL.Image.open("images/lights_01.png").resize((110, 110)))
            kep_betoltes(1,1, sample_img, image_frame, sample_image_lable_list)
        else:
            print("ketto")
