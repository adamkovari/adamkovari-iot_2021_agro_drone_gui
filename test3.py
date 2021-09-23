import tkinter as tk

def input( prompt=''):
    win= tk.Tk()

    win.geometry('%dx%d+%d+%d' % (300, 220, 1300, 500))
    win.resizable(False, False)
    win.title('Input')


    label= tk.Label(win, text=prompt)
    label.pack(padx=15, pady=15)

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput, width=200)
    entry.pack(padx=15, pady=15)

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit, width=200)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()

    return userinput

def infiniti( window):
    while True:
        inp = input("input", window)
        if inp == "repa":
            print("repa")
        else:
            print("ketto")
