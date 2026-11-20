num1=int(input("num(1/2): "))
num2=int(input("num(2/2: "))
for x in range (num1,num2,2):
    if x %2 ==1 :
        print(x,end="\t")