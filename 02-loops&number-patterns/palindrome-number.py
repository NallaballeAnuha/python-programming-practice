#check whether a number is a palindrome
num=int(input("enter a number:"))
original_num=num
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
if original_num==reversed_num:
    print("its a palindrome")
else:
    print("its not a palindrome")
