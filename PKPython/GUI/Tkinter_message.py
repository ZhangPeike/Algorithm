#!/usr/bin/python3
import tkinter as tk
root=tk.Tk()
# label=tk.Label(root,text="Hello world, hello tkinter!")
# label.pack()
saying="Whaterver you do will be insignificant but it is important that you do it! \n(Mahatma Gandhi)"
message=tk.Message(root, text=saying)
message.config(bg='lightblue',font=('times',22,'italic'))
message.pack()
root.mainloop()