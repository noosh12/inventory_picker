#!/usr/bin/env python3

import tkinter as tk


def get_key(event):
    global code

    code += event.char
    label['text'] = code

    if event.keysym == 'Return':
        print('result:', code)
        # showinfo('Code', code)
        label['text'] = code
        code = ''

# --- main ---

root = tk.Tk()
root.geometry('400x100')

# global variables
code = ''

label = tk.Label(root, text="Waiting for input...")
label.pack()

root.bind('<Key>', get_key)

root.mainloop()