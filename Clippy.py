from tkinter import *
from tkinter import ttk
import os
import EST_id_gen


def add_to_clipboard(text):
    """ Adds text to clipboard. Inspiration http://stackoverflow.com/a/9409898 """
    command = 'echo ' + text + '| clip'
    os.system(command)
    draw_clippy(text)


def draw_clippy(text):
    """ Draws Clippy with a speech bubble containing input text"""
    root = Tk()
    root.geometry('211x180-40-60')
    root.title("Clippy")
    root.resizable(width=FALSE, height=FALSE)
    #root.overrideredirect(True) # Removes window title bar and frame
    #root.attributes("-alpha", 0.5) # makes the whole thing transparent


    clippy_top = PhotoImage(file='Images\Clippy_top.png')
    clippy_bottom = PhotoImage(file='Images\Clippy_bottom.png')

    ttk.Label(root, image=clippy_top, compound=CENTER, text="ID is " + text).grid()
    ttk.Label(root, image=clippy_bottom).grid()

    root.mainloop()

if __name__ == "__main__":
    random_id = EST_id_gen.gen_est_id()
    add_to_clipboard(random_id)