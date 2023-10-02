#prog to find factorial of given no using while loop
num=int(input("enter any no"))
fact=1
n=num
while (num>0):
    fact=fact*num
    num=num-1
print(f"factorial of {n} is",fact)

