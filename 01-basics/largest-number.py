#largest of three numbers
a=float(input("enter num1:"))
b=float(input("enter num2:"))
c=float(input("enter num3:"))
if a>=b and a>=c:
    print("largest num is:",a)
elif b>=a and b>=c:
    print("largest num is:",b)
else:
    print("largest num is:",c)

