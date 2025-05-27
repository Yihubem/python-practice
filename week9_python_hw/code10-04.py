from tkinter import *
window = Tk()

photo = PhotoImage(file="C:/Users/HIMART/OneDrive/바탕 화면/week9_python_hw/dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()