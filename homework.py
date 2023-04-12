import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog

file_working = ''
windows = []

class CreateTkWindow:
    def save_as_file_(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_box.get('1.0', END))

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('txt')
        self.window.geometry('600x400')

        menu_main = Menu(self.window)
        self.window.config(menu=menu_main) 

        filemenu = Menu(menu_main, tearoff=0)
        filemenu.add_command(label="open...", command=open_file)
        filemenu.add_command(label="new", command=new_file)
        filemenu.add_command(label="save...", command=self.save_as_file_)

        menu_main.add_cascade(label='file', menu=filemenu)

        self.text_box = Text(self.window)
        self.text_box.pack()


def open_file():
    window_not_main = CreateTkWindow()
    window_not_main.window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    print(window_not_main.window.filename)
    file_working = window_not_main.window.filename
    if file_working:
        with open(file_working, 'r') as file:
            text = file.read()
            window_not_main.text_box.insert('1.0', text)
            window_not_main.text_box.pack()
    windows.append(window_not_main)

def new_file():
    new_window = CreateTkWindow()
    windows.append(new_window)

window_main = CreateTkWindow()
windows.append(window_main)

while True:
    windows[-1:][0].window.mainloop()
    