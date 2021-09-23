from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import Tk, Label, LabelFrame, Entry, Button
import time
import PIL.Image
import sys

import test
from detect_bright_spots import image_analysis
import threading
from threading import Thread
import cv2
from pynput.keyboard import Key, Controller
import keyboard

# root = Tk()
#
# myLabel1 = Label(root, text = "hello world!").grid(row=0, column= 0)
# myLabel2 = Label(root, text = "hello world!").grid(row=1, column= 5)
#
# my_img = ImageTk.PhotoImage(Image.open("images/lights_01.png"))
# label = Label(image=my_img).grid(row=2, column=1)
#
# root.mainloop()

sample_image_list = []
sample_image_label_list =[]

# image_label
label_width = 110
label_height = label_width
label_row_pixel = 130
label_row_num = 3
label_col_pixel = label_row_pixel
label_col_num = 3


#image_resize
image_width = label_row_pixel
image_height = label_col_pixel

first_image_x_coord = 150
first_image_y_coord = 50


#console OUT
console_out = ""


#console IN
console_in = ""


def sample_images_list_initialize():
    for i in range(label_row_num):
        row = []
        for j in range(label_col_num):
            row.append( ImageTk.PhotoImage(PIL.Image.open("images/grey.png").resize((image_width,image_height))))
        sample_image_list.append(row)


def sample_images_initialize(image_frame):
    x = first_image_x_coord
    y = first_image_y_coord
    for i in range(label_row_num):
        row = []
        for j in range(label_col_num):
            label = ttk.Label(image_frame, image=sample_image_list[i][j])
            label.place(x=x+j*label_width, y=y+i*label_height, width=label_width, height=label_height)
            row.append(label)
        sample_image_label_list.append(row)


def kep_betoltes(row,col,img,image_frame):
    x = first_image_x_coord
    y = first_image_y_coord
    #print(row,col)
    sample_image_label_list[row][col].place_forget()
    label = ttk.Label(image_frame, image=img)
    label.place(x=x+col*label_width, y=y+row*label_height, width=label_width, height=label_height)
    window.update()
    return


def kepelemzes(img, image_label):
    analyzed_image = image_analysis(img)
    kepelemzes_eredmeny_betoltese(analyzed_image, image_label)
    return


def kepelemzes_eredmeny_betoltese(img, image_label):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = PIL.Image.fromarray(image)

    image = ImageTk.PhotoImage(image=image)
    label = tk.Label(image_label, image=image)
    label.place(x=680, y=20, width='500', height='400')
    image_label.configure(image=image)
    image_label.image = image
    return
    #print(img)
    #img.show()
    # img = Image.fromarray(img)
    image.save("test.png")#

    # image = ImageTk.PhotoImage(PIL.Image.open("images/lights_01.png").resize((image_width, image_height)))
    # # # # # print(img)

    # # window.update()
    #
    # label = ttk.Label(image_label, image=image)
    # label.place(x=680,y=460,width=460,height=360)
    # window.update()
    # # label.pack()
    return


# def felszallas(img):
#     print(img)
#     label = tk.Label(image_frame, image=img)
#     label.place(x=680, y=40, width=460, height=360)
#     window.update()
#     return


def permetezes():
    #permet
    return


def veszleszallas():
    #veszle
    return


#########################################
#nem kell
def kepek_betoltese(img,image_frame):
    #kep betoltes
    for i in range(label_row_num):
        for j in range(label_col_num):
            kep_betoltes(i,j,img,image_frame)
            time.sleep(0.1)

    return


#class PrintLogger
class PrintLogger(): # create file like object
    def __init__(self, listbox): # pass reference to text widget
        self.listbox = listbox # keep ref

    def write(self, text):
        if text[0] == '<':
            self.listbox.insert(tk.END, text)  # write text to textbox
            self.listbox.see("end")
        else:
            self.listbox.insert(tk.END,">>  " + text) # write text to textbox
            self.listbox.see("end")

            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass


def press_string(msg):
    keyboard = Controller()
    keyboard.type(msg)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    return


def msg_console_in(entry_in, userinput, prompt=''):
    print(entry_in.get())
    # print(sys.argv)

    # press_string(entry_in.get())

    userinput = userinput.get()

    entry_in.delete(0, tk.END)
    # press_string(entry_in.get())
    return userinput


style = Style(theme='darkly')
window = style.master
window.geometry("1200x800")
window.resizable(False,False)
window.title('Mezőgazdasági drón')

sample_img = ImageTk.PhotoImage(PIL.Image.open("images/lights_01.png").resize((image_width,image_height)))
sample_img2 = PIL.Image.open("images/lights_01.png")
sample_img3 = ImageTk.PhotoImage(PIL.Image.open("images/grey.png").resize((1,1)))
# sample_img2 = ImageTk.PhotoImage(PIL.Image.open("images/lights_01.png").resize((460,360)))

# image_frame = ttk.Labelframe(window, text='Drón által készített képek').place(x=30, y=20, width='600', height='400')
# analysis_frame = ttk.Labelframe(window, text='Képelemzés eredménye').place(x=660, y=20, width='500', height='400')

analysis_label = ttk.Label(window, image=sample_img3)
analysis_label.place(x=700, y=20, width='500', height='400')

button_frame = ttk.Labelframe(window, text='Vezérlő gombok').place(x=30, y=440, width='600', height='350')
console_out_frame = ttk.Labelframe(window, text='Console OUT').place(x=660, y=440, width='500', height='150')
console_in_frame = ttk.Labelframe(window, text='Console IN').place(x=660, y=590, width='500', height='200')

#btn_take_off = ttk.Button(button_frame, text="Felszállás", style='success.TButton', command=lambda: felszallas(sample_img)).place(x=90, y=480, width='150', height='50')
btn_spray = ttk.Button(button_frame, text="Permetezés", style='success.TButton', command=lambda: permetezes()).place(x=250, y=480, width='150', height='50')
btn_emergency = ttk.Button(button_frame, text="Vészleállás", style='danger.TButton', command=lambda: veszleszallas()).place(x=410, y=480, width='150', height='50')
btn_images = ttk.Button(button_frame, text="Képek betöltése", style='success.TButton', command=lambda: kepek_betoltese(sample_img,window)).place(x=90, y=540, width='150', height='50')
btn_analysis = ttk.Button(button_frame, text="Képanalízis betöltése", style='success.TButton', command=lambda: kepelemzes(sample_img2, analysis_label)).place(x=250, y=540, width='150', height='50')

listbox_out = tk.Listbox(console_out_frame, fg="blue", font="Helvetica")
listbox_out.place(x=670, y=460, width=480, height=110)

event_obj = threading.Event()

entry_in = tk.Entry(console_in_frame)
entry_in.place(x=670, y=610, width=480, height=110)

btn_send = ttk.Button(console_in_frame, text='Küldés', style='info.TButton', command=lambda: event_obj.set())
btn_send.place(x=835, y=740, width=150, height=30)

sample_images_list_initialize()
sample_images_initialize(window)

pl = PrintLogger(listbox_out)
sys.stdout = pl

thread_drone = Thread(target=test.infiniti, args=(entry_in, window, sample_image_label_list, event_obj, )).start()

thread_gui = Thread(target=window.mainloop()).start()

