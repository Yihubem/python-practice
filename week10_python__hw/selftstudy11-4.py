inFp, outFp = None, None
inStr = ""

srcFile = input("소스 파일명을 입력하세요 : ")    
dstFile = input("타깃 파일명을 입력하세요 : ")    

inFp = open(srcFile, "r", encoding="utf-8", errors="ignore")
outFp = open(dstFile, "w", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("--- %s 파일이 %s 파일로 복사되었음 ---" % (srcFile, dstFile))