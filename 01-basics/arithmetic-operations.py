#arithmetic operations
a=int(input("enter a num1:"))
b=int(input("enter a num2:"))
operation=int(input("choose operation(1:add,2:sub,3:mul,4:div):"))
if operation==1:
    print(a+b)
elif operation==2:
    print(a-b)
elif operation==3:
    print(a*b)
elif operation==4:
    if b==0:
        print("cannot divide by zero")
    else:
        print(a/b)
else:
    print("invalid operation number")
