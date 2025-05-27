inFp = None
inStr = ""
lineNum = 1 

inFp = open("C:/Users/HIMART/OneDrive/바탕 화면/week10_python__hw/data1.txt", "r", encoding="utf-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (lineNum, inStr), end="") 
    lineNum += 1  

inFp.close()