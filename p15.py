#write the prog to print odd no
min=int(input("enter the starting range"))
max=int(input("enter the ending range"))
c=0
for num in range(min,max+1):
    if (num%2!=0):
        c=c+1
        print(num)
print(f"total no of odd no={c}")
