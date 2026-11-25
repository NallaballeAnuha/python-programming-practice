#factorial of a number
num=int(input("enter a number:"))
if num<0:
    print("factorial is not defined for negative numbers")
elif num==0:
    print("factorial of 0 is 1")
else:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f"factorial of {num} is {fact}")