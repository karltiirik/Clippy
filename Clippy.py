from tkinter import *
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
    root.overrideredirect(True)

    clippy_image = PhotoImage(file='Images\\Clippy.gif')
    Label(root, image=clippy_image, compound=CENTER).grid()
    Label(root, text="ID is " + text, background="#FFFFCC").place(x=45, y=20)
    root.after(3000, root.destroy)
    root.mainloop()


if __name__ == "__main__":
    random_id = EST_id_gen.gen_est_id()
    add_to_clipboard(random_id)