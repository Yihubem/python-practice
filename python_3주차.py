A=int(input("입력 진수 결정(16/10/8/2): "))
B=input("값 입력")
if A==16:
    num=int(B, 16)
if A==10:
    num=int(B, 10)
if A==8:
    num=int(B, 8)
if A==2:
    num=int(B, 2)
print("16진수 ==>", hex(num))
print("10진수 ==>", num)
print("8진수 ==>", oct(num))
print("2진수 ==>", bin(num))