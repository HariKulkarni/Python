#write the prog to find sum of odd and even no
num=int(input("enter the no"))
sume=0
sumo=0
for i in range(1,num+1):
         if (i%2==0):
                 sume=sume+i
         elif(i%2!=0):
                sumo=sumo+i

print(f"sum of even no={sume}")
print(f"sum of odd no={sumo}")
     
     
