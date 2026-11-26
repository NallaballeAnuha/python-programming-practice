#whether a number is armstrong number
num=int(input("enter a number:"))
digits=len(str(num))
temp=num
total=0
while temp>0:
    digit=temp%10
    total+=digit**digits
    temp//=10
if total==num:
    print("its an armstrong number")
else:
    print("its not an armstrong number")