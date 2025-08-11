# Level 
num1 = int(input("Entre your first number : "))
num2 = int(input("Entre your second number : "))
operation = input("Entre the operation to be carried "
                 "(Add,Sub,Multiply,Divide,Power,Square root) :")
if(operation=="Add"):
    print(num1+num2)
elif(operation=="Sub"):
    print(num1-num2)
elif(operation=="Multiply"):
    print(num1*num2)
elif(operation=="Divide"):
    print(num1/num2)
elif(operation=="Power"):
    print(num1**num2)
elif(operation=="Square root"):
    print(num1**0.5)
    print(num2**0.5)
else:
    print("Sorry operation not detected")





    
