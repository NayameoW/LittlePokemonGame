from tkinter import *

win = Tk()
win.title(string="NB")
b = Label(win, text="Python NB", font=("Times", 16, "bold"))

b.pack()
Button(win, padx="2i", text="close", command=win.quit).pack()

win.mainloop()
