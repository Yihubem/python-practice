A=int(input("입력한 수식 계산 2. 두 수 사이의 합계:"))

if A==1:   
    print("결과:", eval(input("수식을 입력하세요")))
elif A==2:
    B=int(input("첫번째 숫자를 입력하세요:"))
    C=int(input("두번째 숫자를 입력하세요"))
    오름차순=sorted([B,C])
    result=((오름차순[1]*(오름차순[1]+1))-((오름차순[0]-1)*오름차순[0]))/2
    print(f"{B}부터 {C}까지의 합은 = {result}")
else:
    print("1과 2중에서 설정하세요")