from tkinter import *
from tkinter import messagebox

# 방향키 keycode 참고
# 왼쪽: 37, 위쪽: 38, 오른쪽: 39, 아래쪽: 40

def keyEvent(event):
    if event.state & 0x0001:  # Shift 키가 눌렸는지 확인
        key_name = ""
        if event.keycode == 37:
            key_name = "Shift + 왼쪽 화살표"
        elif event.keycode == 38:
            key_name = "Shift + 위쪽 화살표"
        elif event.keycode == 39:
            key_name = "Shift + 오른쪽 화살표"
        elif event.keycode == 40:
            key_name = "Shift + 아래쪽 화살표"

        if key_name != "":
            messagebox.showinfo("키보드 이벤트", "눌린 키 : " + key_name)

window = Tk()
window.bind("<Key>", keyEvent)  # 모든 키 입력 감지
window.mainloop()