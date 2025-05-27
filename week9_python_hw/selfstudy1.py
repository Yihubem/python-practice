from tkinter import *
window = Tk()
window.title("냥이들 ^^")  # 윈도우 타이틀 설정

# 이미지 객체 2개
photo1 = PhotoImage(file="C:/Users/HIMART/OneDrive/바탕 화면/python_picture/cat1.gif")
photo2 = PhotoImage(file="C:/Users/HIMART/OneDrive/바탕 화면/python_picture/cat2.gif")

# 레이블 2개 생성
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

# 좌우 배치
label1.pack(side = LEFT)
label2.pack(side = LEFT)

window.mainloop()