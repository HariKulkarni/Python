#prog to find sum of digits
num=int(input("enter the number="))
sum=0
while num>0:
    d=num%10
    num=int(num/10)
    sum=sum+d
print(f"sum of digits is ={sum}")


    
