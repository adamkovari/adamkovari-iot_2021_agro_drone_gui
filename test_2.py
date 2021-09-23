import os
import tkinter as tk

cmd = os.popen("your console command").read()

r = tk.Tk()
tk.Label(r,text = cmd).grid(row=0,column=0)
r.mainloop()