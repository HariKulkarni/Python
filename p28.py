#prog to read the string and count the no of vowels
string=input("enter any string")
vowels=0
cons=0
digi=0
for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' ):
            vowels=vowels+1
        elif(i=="1" or i=="2" or i=="3"):
            digi=digi+1
        else:
            cons=cons+1
print(f"no of vowels={vowels}")
print(f"no of cons={cons}")
print(f"no of digits={digi}")

