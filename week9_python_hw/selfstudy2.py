from tkinter import *
import random 

btnList = [None] * 9
fnameList = [
    "froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif",
    "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"
]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

random.shuffle(fnameList)

window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file="C:/Users/HIMART/OneDrive/바탕 화면/python_picture/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()