#sum of digits of a number
num=int(input("enter a number:"))
num=abs(num)
total=0
while num>0:
    total+=num%10
    num//=10
print(total)