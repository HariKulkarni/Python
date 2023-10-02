#find sum of given nums
max=3
i=1
sum=0
while i<=max:
    n=int(input("Enter any num"))
    sum=sum+n
    i+=1
    ch=input("want to continue..[q/c]")
    if ch=='q':
        break
print(f"sum of all nums={sum}")
