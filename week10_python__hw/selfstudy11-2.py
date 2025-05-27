inFp = None
inList, inStr = [], ""

inFp = open("C:/Users/HIMART/OneDrive/바탕 화면/week10_python__hw/data1.txt", "r", encoding="utf-8") 

inList = inFp.readlines()

lineNum = 1  

for inStr in inList:
    print("%d: %s" % (lineNum, inStr), end="")  
    lineNum += 1

inFp.close()