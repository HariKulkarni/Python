#prog to find a given no is palindrome or not
num=int(input("enter the number"))
temp=num
r=0
while num>0:
    d=num%10
    r=(r*10)+d
    num=int(num/10)
if temp==r:
    print(f"given no is={temp} is a palindrome no")
else:
    print(f"given no is={temp} is  not a palindrome no")


    
