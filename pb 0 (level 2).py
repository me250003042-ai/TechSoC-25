# Level 2
num = float(input("Entre your first number : "))
operation = input("Entre the operation to be carried\n"
           "Natural log,Log base 10,Exponential,Power with decimal exponents:")
if(operation=="Natural log"):
    i=1
    a = 0
    while(i<100):
        a += (-1)**(i+1)*(((num-1)**i)/i)
        i+=1
    print(a)
elif(operation=="Log base 10"):
    i=1
    a = 0
    while(i<100):
        a += (-1)**(i+1)*(((num-1)**i)/i)
        i+=1
    print(a/2.30258509299) # 2.30258509299 is ln(10)
elif(operation=="Exponential"):
    print(2.718281828**num)
elif(operation=="Power with decimal exponents"):
    num1 = int(input("Entre the base for this operation:"))
    print(num1**num)
else:
    print("Sorry this operation cannot be performed")
    
    

