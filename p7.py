a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
smallest=0
if a<b and a<c:
    smallest=a
elif b<a:
    smallest=b
else:
    smallest=c
print(smallest, "is the smallest of 3 no")
