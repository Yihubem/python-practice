for dan in range(2, 10):
    print("#  {}단".format(dan), end="\t")
print()

for i in range(1, 10):        
    for dan in range(2, 10):   
        print("{}X{}={}".format(dan, i, dan*i), end="\t")
    print()