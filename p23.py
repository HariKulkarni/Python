#prog to reverse a given no
num=int(input("enter the number"))
temp=num
r=0
while num>0:
    d=num%10
    r=(r*10)+d
    num=int(num/10)
print(f"given no is={temp}")
print(f"reverse no is={r}")

    
